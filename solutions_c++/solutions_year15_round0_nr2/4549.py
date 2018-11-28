#include "bits/stdc++.h"
using namespace std;
int main(){
	freopen("entrada.txt","r",stdin);
	freopen("salida.txt","w",stdout);
	int t;
	cin>>t;
	for (int m = 1; m <= t; ++m)
	{
		long long mx=0;
		int n;
		cin>>n;
		long long v[100];
		for (int i = 0; i < n; ++i)
		{
			cin>>v[i];
			mx=max(mx,v[i]);
		}
		long long r=999999;
		for (int i = 1; i <= mx; ++i)
		{
			long long resp=0;
			for (int j = 0; j < n; ++j)
			{
				resp+=(v[j]/i);
				if(v[j]%i==0)resp--;
			}
			resp+=i;
			r=min(r,resp);
		}
		cout<<"Case #"<<m<<": "<<r<<endl;
	}
	return 0;
}