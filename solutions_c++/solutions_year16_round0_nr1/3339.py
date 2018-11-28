#include <bits/stdc++.h>
typedef long long int ll;
#define fio ios_base::sync_with_stdio(false)
using namespace std;

int main() {
	fio;
	ll t,n,ans;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		cin>>n;
		if(n==0) {cout<<"Case #"<<z<<": INSOMNIA"<<"\n";continue;}
		int seen=0;
		map<char,ll> m;
		for(int i=1;seen<10;i++)
		{
			ans=i*n;
			string s=to_string(ans);
			for(int j=0;j<s.size();j++)
			{
				if(m[s.c_str()[j]]==0) seen++;
				m[s.c_str()[j]]++;
			}
		}
		cout<<"Case #"<<z<<": "<<ans<<"\n";
	}
	return 0;
}