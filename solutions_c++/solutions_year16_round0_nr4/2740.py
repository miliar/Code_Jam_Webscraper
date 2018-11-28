#include <bits/stdc++.h>
typedef long long int ll;
#define fio ios_base::sync_with_stdio(false)
using namespace std;

int main() {
	fio;
	ll t,k,c,s;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		cin>>k>>c>>s;
		ll ans[k],pre=k;
		for(int j=0;j<k;j++) ans[j] = j+1;
		for(int i=2;i<=c;i++)
		{
			for(int j=0;j<k;j++) 
				ans[j] += j*pre;
			pre*=k;
		}
		cout<<"Case #"<<z<<": ";
		for(int i=0;i<k;i++)
			cout<<ans[i]<<" ";
		cout<<"\n";
	}
	return 0;
}