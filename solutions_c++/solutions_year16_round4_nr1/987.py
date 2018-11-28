#include<bits/stdc++.h>
using namespace std;

int a[13][3];
vector<int> G[13];

string change(string s,int n){

  int len=1;
  for(int i=1;i<=n;i++){

    for(int j=0;j<(int)s.size();j+=(len+len)){
      if( s.substr(j,len) > s.substr(j+len,len) ){
        for(int k=0;k<len;k++){
          swap(s[j+k],s[j+len+k]);
        }
      }
    }
    len*=2;
  }
  return s;
}

void init(int A,int B){
  for(int i=0;i<13;i++){
    a[i][0]=a[i][1]=a[i][2]=0;
    G[i].clear();
  }

  if(A>B)swap(A,B);
  a[1][A]=a[1][B]=1;
  G[1].push_back(A);
  G[1].push_back(B);
  
  for(int i=2;i<=12;i++){
    G[i].resize( G[i-1].size()*2 );
    vector<int> vec=G[i-1];
    
    
    for(int j=0;j<(int)vec.size();j++){
      G[i][j*2]=vec[j];
      G[i][j*2+1]=(G[i][j*2]+1)%3;
    }
    a[i][0]=a[i-1][0]+a[i-1][2];
    a[i][1]=a[i-1][1]+a[i-1][0];
    a[i][2]=a[i-1][2]+a[i-1][1];
  }
}

int main(){

  
  int Tc;
  cin>>Tc;
  for(int tc=1;tc<=Tc;tc++){
    int N,P,R,S;
    cin>>N>>R>>P>>S;
    char tab[3];
    cout<<"Case #"<<tc<<": ";
    string ans="ZZZZ";

    init(0,1);
    if(P==a[N][0]&&R==a[N][1]&&S==a[N][2]){
      tab[0]='P';tab[1]='R';tab[2]='S';
      string tmp="";
      for(int k=0;k<(int)G[N].size();k++)tmp+=tab[ G[N][k] ];
      tmp=change(tmp,N);
      ans=min(ans,tmp);
    }

    if(S==a[N][0]&&P==a[N][1]&&R==a[N][2]){
      tab[0]='S';tab[1]='P';tab[2]='R';
      string tmp="";
      for(int k=0;k<(int)G[N].size();k++)tmp+=tab[ G[N][k] ];
      tmp=change(tmp,N);
      ans=min(ans,tmp);
    }
    
    if(R==a[N][0]&&S==a[N][1]&&P==a[N][2]){
      tab[0]='R';tab[1]='S';tab[2]='P';
      string tmp="";
      for(int k=0;k<(int)G[N].size();k++)tmp+=tab[ G[N][k] ];
      tmp=change(tmp,N);
      ans=min(ans,tmp);
    }

    
    if(P==a[N][0]&&S==a[N][1]&&R==a[N][2]){
      tab[0]='P';tab[1]='S';tab[2]='R';
      string tmp="";
      for(int k=0;k<(int)G[N].size();k++)tmp+=tab[ G[N][k] ];
      tmp=change(tmp,N);
      ans=min(ans,tmp);
    }

    if(S==a[N][0]&&R==a[N][1]&&P==a[N][2]){
      tab[0]='S';tab[1]='R';tab[2]='P';
      string tmp="";
      for(int k=0;k<(int)G[N].size();k++)tmp+=tab[ G[N][k] ];
      tmp=change(tmp,N);
      ans=min(ans,tmp);
    }
    
    if(R==a[N][0]&&P==a[N][1]&&S==a[N][2]){
      tab[0]='R';tab[1]='P';tab[2]='S';
      string tmp="";
      for(int k=0;k<(int)G[N].size();k++)tmp+=tab[ G[N][k] ];
      tmp=change(tmp,N);
      ans=min(ans,tmp);
    }

    if(ans=="ZZZZ"){
      cout<<"IMPOSSIBLE"<<endl;
    }else{
      cout<<ans<<endl;
    }
  }
  return 0;
}
