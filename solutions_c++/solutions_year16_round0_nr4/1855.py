#include<iostream>

using namespace std;

int main(){
	int t,k,c,s;
	cin>>t;

	int p=1;
	while(p<=t){
		cin>>k>>c>>s;

		cout<<"Case #"<<p<<": ";
		for(int i=1;i<=k;i++){
			cout<<i<<" ";
		}
		cout<<endl;


		p++;
	}



}