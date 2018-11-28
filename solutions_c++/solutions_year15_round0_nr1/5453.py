#include "bits/stdc++.h"
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("salida.txt","w",stdout);
	int t;
	cin>>t;
	for (int m = 1; m <= t; ++m)
	{
		long long a=0,n,r=0;
		cin>>n;
		string c;
		cin>>c;
		for (int i = 0; i < c.length(); ++i)
		{
			if(r>=i){
				r+=(long long)c[i]-'0';
			}
			else{
				a+=(i-r);
				r+=(i-r)+((long long)c[i]-'0');
			}
		}
		cout<<"Case #"<<m<<": "<<a<<endl;
	}
	return 0;
}