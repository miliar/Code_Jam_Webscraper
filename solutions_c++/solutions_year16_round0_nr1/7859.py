#include<bits/stdc++.h>
using namespace std;
int a[11];
int main()
{ios_base::sync_with_stdio(false);
	long long int t,i,n,tp,to,x,y,p,q,co;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		for(int ii=0;ii<10;ii++)
			a[ii]=0;
		cout<<"Case "<<"#"<<i<<": ";
		if(n==0)
		{
			cout<<"INSOMNIA\n";
			
		}
		else
		{
			tp=1;
			co=0;
			while(1)
			{
				x=n*tp;
				tp++;
				y=x;
				while(y)
				{
					if(co==10)
					break;
					p=y%10;
					if(a[p]==0)
					{
						co++;
						a[p]=1;
					}
					y=y/10;

				}
				if(co==10)
					break;
			}
			cout<<x<<"\n";
		}
	}

}