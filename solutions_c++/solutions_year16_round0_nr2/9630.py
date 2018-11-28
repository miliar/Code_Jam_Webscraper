#include <bits/stdc++.h>
using namespace std;
string pila;
int N;
int memo[1<<12];
int cicles[1<<12];
vector<int> adj[1<<12];
bool mark[1<<12];
int dist[1<<12];

int dp(int bitmask){
  cout<<"B: "<<bitmask<<endl;
  if(!bitmask)return 0;
  if(cicles[bitmask])return 100000000;
  cicles[bitmask]=1;
  if(memo[bitmask]!=-1)return memo[bitmask];
  int ans=100000000;
  int inv_bit=0;
  for(int i=0;i<N;i++){
    inv_bit=(inv_bit<<1)|(((~((1<<i)&bitmask))>>i)&1);
    cout<<bitmask<<" "<<i<<" "<<inv_bit<<endl;
    ans=min(ans,1+dp((bitmask&~((1<<(i+1))-1))|inv_bit));
  }
  cicles[bitmask]=0;
  return memo[bitmask]=ans;
}

main(){
  int T,cases=1,bitmask,inv_bit;
  scanf("%d",&T);
  queue<int> cola;
  while(T--){
    for(int i = 0; i < (1<<12); i++){
       memo[i] = -1;
       cicles[i] = 0;
       dist[i] = 0;
       mark[i] = 0;
    }
    if(cases!=1)printf("\n");
    cin>>pila;
    N = pila.size();
    for(int j=0;j<(1<<N);j++){
       bitmask=j;
       inv_bit=0;
      for(int i=0;i<N;i++){
       inv_bit=(inv_bit<<1)|(((~((1<<i)&bitmask))>>i)&1);
       adj[j].push_back((bitmask&~((1<<(i+1))-1))|inv_bit);
      }
    }
    bitmask=0;
    for(int i=pila.size()-1;i>=0;i--)
      bitmask=(bitmask<<1)|(pila[i]=='+'?0:1);
    cola.push(bitmask);
    mark[bitmask]=1;
    while(!cola.empty()){
      int v=cola.front();cola.pop();
      for(int i=0;i<adj[v].size();i++){
        if(!mark[adj[v][i]]){
          cola.push(adj[v][i]);
          mark[adj[v][i]]=1;
          dist[adj[v][i]]+=dist[v]+1;
        }
      }
    }
    printf("Case #%d: %d",cases++,dist[0]);
    memset(adj,0,sizeof adj);
  }
}