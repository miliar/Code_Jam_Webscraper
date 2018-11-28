#include<iostream>

using namespace std;

int main(){
  int T;
  cin>>T;
  for(int i=1;i<=T;i++){
    cout<<"Case #"<<i<<": ";
    int N,P;
    cin>>N>>P;
    for(int j=0;j<1<<N;j++){
      int r=j;
      int b=0;
      for(int k=0;k<N;k++){
	b<<=1;
	b|=r!=0;
	r=(r-1)/2;
      }
      if(b>=P){
	cout<<j-1<<' ';
	goto l1;
      }
    }
    cout<<(1<<N)-1<<' ';
  l1:
    for(int j=(1<<N)-1;j>=0;j--){
      int r=(1<<N)-j-1;
      int b=0;
      for(int k=0;k<N;k++){
	b<<=1;
	b|=r!=0;
	r=(r-1)/2;
      }
      if((1<<N)-1-b<P){
	cout<<j<<endl;
	goto l2;
      }
    }
    cout<<0<<endl;
  l2:
    ;
  }
  return 0;
}
    
      
