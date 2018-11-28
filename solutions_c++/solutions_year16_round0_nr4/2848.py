#include<bits/stdc++.h>
#include<stdint.h>
#include<sstream>
using namespace std;

int main(){
//	cout<<getBase1(4294967295,10,32);
  int test,k,c,s;
  cin>>test;
  for(int i=1;i<=test;i++){
  	cin>>k>>c>>s;
  	
  	cout<<"Case #"<<i<<": ";
  	for(int j=1;j<=k;j++){
  		cout<<j;
  		if(j != k){
  			cout<<" ";
		}
	}
  	cout<<"\n";
  }
}
