#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define For(i,N) for(int i=0; i<N; i++)
#define Fore(i,C) for(__typeof((C).begin()) i =(C).begin(); i != (C).end(); ++i)
#define FOR(i,j,k) for(int i=j; i<k; i++)
#define Fors(i,s) for(int i=0; s[i]; i++)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef long long ll;
using namespace std;

int T,N,M;
vector<string> Z;
vector<vector<int> > G;
char buf[100];
int x,y;

string INF;

bool je_cesta(int a, int b){
  For(i,G[a].size()) if(G[a][i] == b) return 1;
  return 0;
}

string over(vector<int> &V){
  vector<int> bol(N,-1);
  int cur = V[0];
  int p = 1;
  bol[cur] = 100;
  string res=Z[cur];
  while(cur != V.back()){
    while(cur != 100 && !je_cesta(cur,V[p])) cur = bol[cur];
    if(cur == 100) return INF;
    bol[V[p]] = cur;
    cur = V[p];
    res += Z[cur];
    p++;
   }
   //printf("%s\n",res.c_str());
  return res;
}

int main(){
  INF = "";
  For(i,100)INF +='9';
  scanf(" %d", &T);
  For(t,T){
    scanf(" %d %d", &N, &M);
    Z.clear(); Z.resize(N);
    G.clear(); G.resize(N);
    For(i,N){ scanf(" %s", buf); Z[i] = buf; }
    For(i,M){ scanf(" %d %d", &x, &y); x--; y--; G[x].pb(y); G[y].pb(x); }
    vector<int> R;
    For(i,N) R.pb(i); 
    string mini=INF; 
    do{
      //For(i,R.size()) printf("%d ",R[i]); printf("\n");
      mini = min( mini, over(R) );
    }while(next_permutation(R.begin(), R.end()));
    printf("Case #%d: %s\n",t+1, mini.c_str());
  }
  return 0;
}