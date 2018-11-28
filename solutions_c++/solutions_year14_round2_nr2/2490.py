#include <bits/stdc++.h>
using namespace std;
int main (int argc, char const* argv[])
{
	int a,b,k,t,c=0;
	cin>>t;
	for(int m = 0;m<t;++m){
		c=0;
		cin>>a>>b>>k;
		for(int i = 0; i<a;++i){
			for(int j = 0;j<b;++j){
				if( (i&j) < k) ++c;
			}	
		}
		cout<<"Case #"<<(m+1)<<": "<<c<<endl;
	}
	return 0;
}
