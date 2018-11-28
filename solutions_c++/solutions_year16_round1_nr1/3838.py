#include <iostream>
using namespace std;

int main() {
	int t,p;
	string c,x;
	cin>>t;
	for(int i=1; i<=t; i++){
		cin>>c;
		p=0;
		x[0]=c[0];
		for(int j=1; j<c.length(); j++){
			if(c[j]>=x[0]){
				for(int k=j; k>0; k--){
					x[k]=x[k-1];
				}
				x[0]=c[j];
				p++;
			}else{
				x[j]=c[j];
			}
		}
		
		cout<<"Case #"<<i<<": ";
		for(int j=0; j<c.length(); j++){
			cout<<x[j];
		}
		cout<<endl;
	}
}
