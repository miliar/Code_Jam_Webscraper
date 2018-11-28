#include <vector>
#include <cstdio>
#include <string>
#include <map>
#include <queue>
using namespace std;


#define MAX_L 2000
#define MAX_R 2000
typedef  vector <int> vi;

int L, R;
vi adjL[MAX_L];   //  links  LEFT  vertices  to RIGHT  vertices.
int  matchL[MAX_L], matchR[MAX_R];
bool  visitedL[MAX_L], visitedR[MAX_R];
int  predL[MAX_L], predR[MAX_R ];

struct  State {
int v,d;
State(int v,int d):v(v),d(d){}
};
vi bfs() {
queue <State > q;
fill_n(visitedR , R, false); //  cleaned  for  the  dfs
fill_n(visitedL , L, false);
for(int l = 0; l < L; l++)
if(matchL[l] ==  -1) {
q.push(State(l, 0));
visitedL[l] = true;
}
int  shortest_aug_dist = MAX_L+MAX_R;
vi F;   //  endpoints  of all the  shortest  augmenting  paths.
while (!q.empty ()) {
const  State  cur = q.front ();
q.pop ();
if(cur.d % 2 == 0)
for(int i = 0; i < int(adjL[cur.v].size ()); i++) {
const  int  next = adjL[cur.v][i];
if(matchL[cur.v] == next ||  visitedR[next])
continue;
visitedR[next] = true;
predR[next] = cur.v;
q.push(State(next , cur.d+1));
}
else {
if(cur.d > shortest_aug_dist)
break;   //  stops  bfs
int u = matchR[cur.v];
if(u ==  -1) {
shortest_aug_dist = cur.d;
F.push_back(cur.v);
} else if(! visitedL[u]) {
predL[u] = cur.v;
q.push(State(u, cur.d+1));
}
}
}
fill_n(visitedR , R, false); //  cleaned  for  explore
fill_n(visitedL , L, false);
return F;
}
bool  explore(int r) {
if(visitedR[r])
return  false;
visitedR[r] = true;
int l = predR[r];
if(visitedL[l])
return  false;
visitedL[l] = true;
if(matchL[l] !=  -1 && !explore(predL[l]))
return  false;
matchL[l] = r;
matchR[r] = l;
return  true;
}
int  bipartite_matching () {
fill_n(matchL , L,  -1);
fill_n(matchR , R,  -1);
fill_n(predL , L,  0);
fill_n(predR , R,  0);
vi F;
int sz = 0;
while (!(F = bfs ()). empty ())
for(int i = 0; i < int(F.size ()); i++)
sz +=  explore(F[i]);
return  sz;
}




int main(){
int t;
scanf("%d",&t);

for(int c=1;c<=t;c++){
map<string, int> idL;
map<string, int> idR;
int n;
scanf("%d",&n);
int idLn=0;
int idRn=0;
for(int i=0;i<2000;i++)adjL[i].clear();
for(int i=0;i<n;i++){
char x[21],y[21];
scanf("%s %s",x,y);
string xx(x);
string yy(y);
int ida,idb;
map<string,int>::const_iterator a;
if((a = idL.find(xx))!=idL.end()){
    ida=(*a).second;
    }else{
    ida=idLn;idL[xx]=ida;idLn++;
}
if((a = idR.find(yy))!=idR.end()){
    idb=(*a).second;
    }else{
    idb=idRn;idR[yy]=idb;idRn++;
}
adjL[ida].push_back(idb);
}
L=idLn;
R=idRn;

int r = bipartite_matching ();
printf("Case #%d: %d\n",c,n-r-(L-r)-(R-r));

}
}
