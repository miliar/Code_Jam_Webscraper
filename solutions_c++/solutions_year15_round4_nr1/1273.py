#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}

int N;
int H,W;
int field[101][101];

void solve(){
  cin>>H>>W;
  for(int i=0;i<H;i++){
    for(int j=0;j<W;j++){
      char ch;
      cin>>ch;
      if(ch=='.')field[i][j]=-1;
      else if(ch=='^')field[i][j]=0;
      else if(ch=='>')field[i][j]=1;
      else if(ch=='v')field[i][j]=2;
      else if(ch=='<')field[i][j]=3;
    }
  }
  const int dy[]={-1,0,1,0};
  const int dx[]={0,1,0,-1};
  int res = 0;
  for(int i=0;i<H;i++){
    for(int j=0;j<W;j++){
      if(field[i][j]==-1)continue;
      int ang = field[i][j];
      bool ok=false;
      for(int k=0;k<4;k++){
        int cy=i;
        int cx=j;
        bool match=false;
        while(1){
          cy+=dy[k];
          cx+=dx[k];
          if(!(cy>=0&&cx>=0&&cy<H&&cx<W))break;
          if(field[cy][cx]!=-1){
            ok=true;
            match=true;
          }
        }
        if(k==ang){
          //cout<<i<<" "<<j<<" "<<k<<" "<<match<<endl;
          if(!match){
            res++;
          }
        }
      }
      if(!ok){
        cout<<"IMPOSSIBLE"<<endl;
        return;
      }
    }
  }
  cout<<res<<endl;
}

int main(){
  fastStream();
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    solve();
  }
  
  return 0;
}
