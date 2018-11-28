#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define all(v) (v).begin(),(v).end()

#define VI vector<int>
#define PII pair<int,int>
#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define lint long long int

#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debug2(x,y) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y <<endl; } 
#define debug3(x,y,z) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y << ", " << #z << " = " << z <<endl; } 
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define debugt(t,n) {{cerr <<#t <<" = "; FOR(it,0,(n)) cerr <<t[it] <<", "; cerr <<endl; }}

#define make( x) int (x); scanf("%d",&(x));
#define make2( x, y) int (x), (y); scanf("%d%d",&(x),&(y));
#define make3(x, y, z) int (x), (y), (z); scanf("%d%d%d",&(x),&(y),&(z));
#define make4(x, y, z, t) int (x), (y), (z), (t); scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define makev(v,n) VI (v); FOR(i,0,(n)) { make(a); (v).pb(a);} 
#define IOS ios_base::sync_with_stdio(0)
#define HEAP priority_queue

#define read( x) scanf("%d",&(x));
#define read2( x, y) scanf("%d%d",&(x),&(y));
#define read3(x, y, z) scanf("%d%d%d",&(x),&(y),&(z));
#define read4(x, y, z, t) scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define readv(v,n) FOR(i,0,(n)) { make(a); (v).pb(a);}

using namespace std;

#define max_n 1000005

char s[205][205];

int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};
char move[]={'>','<','v','^'};


void solve(){
	make2(n,m);
	FOR(i,0,n) scanf("%s",s[i]);
	
	bool ans = true;
	int ile = 0;

	FOR(i,0,n){
		FOR(j,0,m){
			if(s[i][j]!='.'){
				bool jest = false;
				FOR(u,0,m) if(s[i][u]!='.' && u!=j) jest = true;
				FOR(u,0,n) if(s[u][j]!='.' && u!=i) jest = true;
				if(!jest) ans = false;
				
				int mymove = 0;
				FOR(k,0,4) if(s[i][j]==move[k]) mymove = k;
				
				int myx = i+dx[mymove], myy = j+dy[mymove];
				bool was = false;
			
				while(myx>=0 && myx < n && myy>=0 && myy<m){
					if(s[myx][myy]!='.') was = true;
					myx += dx[mymove];
					myy += dy[mymove];
				}
				if(!was) ile++;
			}
		}
	}
	if(ans){
		printf("%d\n",ile);
	}
	else printf("IMPOSSIBLE\n");

}


int main(){
	make(t);
	FOR(i,1,t+1){
		printf("Case #%d: ",i);
		solve();
	}
}

