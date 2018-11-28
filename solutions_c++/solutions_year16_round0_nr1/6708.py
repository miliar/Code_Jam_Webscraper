#include<iostream>
using namespace std;
int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    bool used[10]={};
    long long n,c=0,N,a;
    cin>>n;
    if(!n){
      cout<<"Case #"<<i<<": INSOMNIA"<<endl;
      continue;
    }
    for(int j=1;c!=10;j++){
      a=N=n*j;
      while(N){
	if(!used[N%10])c++,used[N%10]=1;
	N/=10;
      }
    }
    cout<<"Case #"<<i<<": "<<a<<endl;
  }
  return 0;
}
