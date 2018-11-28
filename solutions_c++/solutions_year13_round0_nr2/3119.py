#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>

using namespace std;

int Max=2,lawn[111][111];
int N,M;
int Compara[111][111];

bool comparar(int in,int jn){
  int ban=0;
  //cout<<"Vertical UP: ";
  for(int i=in-1;i>=0;i--){
    //cout<<lawn[i][jn]<<" ";
    if(lawn[i][jn]>lawn[in][jn]){
      ban=1;
      break;
    }
  }if(!ban){
    //cout<<endl<<"Vertical DOWN: ";
    for(int i=in+1;i<N;i++){
      //cout<<lawn[i][jn]<<" ";
      if(lawn[i][jn]>lawn[in][jn]){
        ban=1;
        break;
      }
    }
  }if(ban)
    Compara[in][jn]++;
  ban=0;

  //cout<<endl<<"LEFT : ";
  for(int i=jn-1;i>=0;i--){
    //cout<<lawn[in][i]<<" ";
    if(lawn[in][i]>lawn[in][jn]){
      ban=1;
      break;
    }
  }if(!ban){
    //cout<<endl<<"RIGHT : ";
    for(int i=jn+1;i<M;i++){
      //cout<<lawn[in][i]<<" ";
      if(lawn[in][i]>lawn[in][jn]){
        ban=1;
        break;
      }
    }
  }if(ban)
    Compara[in][jn]++;
  /*cout<<endl;
  for(int i=0;i<N;i++){
    for(int j=0;j<M;j++){
      cout<<Compara[i][j]<<" ";
    }
    cout<<endl;
  }
  cout<<endl<<endl;
  */
  if(Compara[in][jn]==2)return false;
  return true;

}

using namespace std;
int main(){
  int T,ncas=0;
  scanf("%d",&T);
  while(T--){
    int tmp;
    scanf("%d %d",&N,&M);
    for(int i=0;i<N;i++){
      for(int j=0;j<M;j++){
        cin>>tmp;
        lawn[i][j]= tmp;
      }
    }

    memset(Compara,0,sizeof(Compara));
    int ban=0;
    for(int i=0;i<N;i++){
      for(int j=0;j<M;j++){
        if(lawn[i][j] == Max)
          continue;
        if(!comparar(i,j)){
          ban=1;
          break;
        }

      }
      if(ban)break;
    }
    if(ban)
      printf("Case #%d: NO\n",++ncas);
    else
      printf("Case #%d: YES\n",++ncas);
      //scanf("%s",lawn[i]);
  }
}
