#include <bits/stdc++.h>
using namespace std;
int main (int argc, char const* argv[])
{
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		vector<int>v(10,0);
		int f = 0;
		long long n;
		cin>>n;
		long long i =1;
		if(n==0)f=1;
		while(!f)
		{
			long long k = n*i;
			while(k)
			{
				v[k%10]++;
				k/=10;
			}
			f =1;
			for(int ii=0;ii<10;ii++)
			{
				if(v[ii]==0)
				{
					f = 0;
					break;
				}
			}
			i++;
		}
		i--;
		if(!n)
		cout<<"Case #"<<tc<<": "<<"INSOMNIA\n";
		else cout<<"Case #"<<tc<<": "<<(n*i)<<'\n';
	}
	return 0;
}
