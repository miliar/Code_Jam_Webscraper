#include<iostream>
using namespace std;
typedef long long int ll;
int main()
{	freopen("A-large.in","r",stdin);
	freopen("Alarge.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		bool chk[10]={false};
		ll n,g,j=1,r,f;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA\n";
			continue;
		}
		while(1)
		{
			g=j*n;
			int c=0;
			f=g;
			while(g)
			{
				r=g%10;
				chk[r]=true;
				g/=10;
			}
			j++;
			for(int z=0;z<10;z++)
			{if(chk[z]==true)
			{
				c++;
			}}
			if(c==10)
			break;
		}
		cout<<"Case #"<<i<<": "<<f<<"\n";
	}
}