#include<bits/stdc++.h>
using namespace std;
int H,W,N;

int t[20][20];

bool vd[20][20][4];
int si[100];

int dfs(int y,int x,int dir){
  if(y==0||y==H+1||x==0||x==W+1)return t[y][x];
  if(vd[y][x][dir])return 1e9;
  vd[y][x][dir]=true;
  if(t[y][x]==0){// /
    if(dir==0)return dfs(y,x+1,1);
    if(dir==1)return dfs(y-1,x,0);
    if(dir==2)return dfs(y,x-1,3);
    if(dir==3)return dfs(y+1,x,2);
  }else if(t[y][x]==1){
    if(dir==0)return dfs(y,x-1,3);
    if(dir==1)return dfs(y+1,x,2);
    if(dir==2)return dfs(y,x+1,1);
    if(dir==3)return dfs(y-1,x,0);
  }
}

bool check(){
  memset(vd,false,sizeof(vd));
  int C=1;
  /*
  for(int i=1;i<=W;i++){
    cout<<dfs(1,i,2)<<' '<<si[C]<<endl;
    C++;
  }
  for(int i=1;i<=H;i++){
    cout<<dfs(i,W,3)<<' '<<si[C]<<endl;
    C++;
  }
  for(int i=W;i>=1;i--){
    cout<<dfs(H,i,0)<<' '<<si[C]<<endl;
    C++;
  }
  for(int i=H;i>=1;i--){
    cout<<dfs(i,1,1)<<' '<<si[C]<<endl;
    C++;
  }
  */
  memset(vd,false,sizeof(vd));
  C=1;
  for(int i=1;i<=W;i++){
    if(dfs(1,i,2)!=si[C]){
      return false;
    }
    C++;
  }
  for(int i=1;i<=H;i++){
    if(dfs(i,W,3)!=si[C])return false;
    C++;
  }
  for(int i=W;i>=1;i--){
    if(dfs(H,i,0)!=si[C])return false;
    C++;
  }
  for(int i=H;i>=1;i--){
    if(dfs(i,1,1)!=si[C])return false;
    C++;
  }

  return true;
}

int main(){
  int Tc,tc=1;
  cin>>Tc;
  while(Tc--){
    cin>>H>>W;
    N=H*W;
    for(int i=0;i< H+W ; i++){
      int a,b;
      cin>>a>>b;
      si[a]=b;
      si[b]=a;
    }

    int C=1;
    for(int i=1;i<=W;i++){
      t[0][i]=C++;
    }
    for(int i=1;i<=H;i++){
      t[i][W+1]=C++;
    }
    for(int i=W;i>=1;i--){
      t[H+1][i]=C++;
    }
    for(int i=H;i>=1;i--){
      t[i][0]=C++;
    }
    cout<<"Case #"<<tc++<<":"<<endl;
    bool flg=false;
    for(int i=0;i<(1<<N);i++){
      for(int j=0;j<N;j++){
        int key=(i>>j&1);
        t[ j/W+1 ][ j%W+1 ]=key;
      }
      /*
      if(i==0){
        for(int y=1;y<=H;y++){
          for(int x=1;x<=W;x++){
            if(t[y][x]==0)cout<<'/';
            if(t[y][x]==1)cout<<'\\';
          }
          cout<<endl;
        }
        cout<<check()<<endl;
        cout<<"!"<<endl;
      }
      */
      if(check()){
        for(int y=1;y<=H;y++){
          for(int x=1;x<=W;x++){
            if(t[y][x]==0)cout<<'/';
            if(t[y][x]==1)cout<<'\\';
          }
          cout<<endl;
        }
        flg=true;
        break;
      }
    }
    if(!flg)cout<<"IMPOSSIBLE"<<endl;
  }
}
