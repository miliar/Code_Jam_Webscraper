#include<iostream>
using namespace std;
bool flags[11];
void f(int n){
  while(n){
    flags[n%10]=1;
    n/=10;
  }
}
bool c(void){
  for(int i = 0;i<10;i++){
    if(!flags[i])return 0;
  }
  return 1;
}


int main(void){
  int T;
  int N;
  cin>>T;
  for(int i = 1;i<=T;i++){
    cin>>N;
    if(N==0){
      cout<<"Case #"<<i<<": INSOMNIA"<<endl;
    }else{
      int n = N;
      for(int j = 0;j<10;j++)flags[j]=0;
      int j=0;
      while(!c()){
        j++;
        n=N*j;
        f(n);
      }
      cout<<"Case #"<<i<<": "<<n<<endl;
    }
  }
  return 0;
}
