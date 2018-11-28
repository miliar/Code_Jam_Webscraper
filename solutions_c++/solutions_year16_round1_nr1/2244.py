#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	string a;
	cin>>t;	
	for(int i=1;i<=t;i++){
		cin>>a;
		string res="";
		string aux="";
		res+=a[0];
		for(int j=1;j<a.length();j++){
			if(a[j]<res[0])
				res+=a[j];
			else {
				aux="";
				aux+=a[j];
				aux+=res;
				res=aux;
			}
		}
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
	return 0;
}