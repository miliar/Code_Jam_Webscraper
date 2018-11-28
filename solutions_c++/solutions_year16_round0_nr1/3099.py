#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
map<ll,ll> mm;
int main()
{
	ll t,n,i;
	FILE * pFile;
	pFile = fopen ("output.txt","w");
	//fscanf ("input.txt", "%lld", &t);
	cin>>t;
	ll c=0;
	while(t--)
	{
		c++;
		
		mm.clear();
		cin>>n;
		//fscanf ("input.txt", "%lld", &n);
		//cout<<"Case #"<<c<<": ";
		if(n==0)
		{
			fprintf (pFile, "Case #%lld: INSOMNIA\n",c);
			//cout<<"INSOMNIA"<<endl;
			continue;
		}
		ll s=1;
		ll ans;
		for(i=1;;i++)
		{
			s=n*i;
			while(s)
			{
				mm[s%10]++;
				s/=10;
			}
			if(mm.size()==10)
			{
				ans=n*i;
				break;
			}
		}
		fprintf (pFile, "Case #%lld: %lld\n",c,ans);
		//cout<<ans<<endl;
	}
}
