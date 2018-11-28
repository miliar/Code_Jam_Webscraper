#include<bits/stdc++.h>
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
using namespace std;
int main()
{
	f_in("small4.in");
    f_out("small4out.txt");
	long long t,k,c,s,j=0,i;
	cin>>t;
	while(t--)
	{
		j++;
		cin>>k>>c>>s;
		cout<<"Case #"<<j<<": ";
		if(k==1)
		{
			if(s>=1)
			{
				cout<<"1"<<endl;
			}
			else
			{
				cout<<"IMPOSSIBLE"<<endl;
			}
		}
		else
		{
			if(c==1)
			{
				if(s<k)
				{
					cout<<"IMPOSSIBLE"<<endl;
				}
				else
				{
					for(i=1;i<=k;i++)
					{
						cout<<i<<" ";
					}
					cout<<endl;
				}
			}
			else
			{
				if(s<k-1)
				{
					cout<<"IMPOSSIBLE"<<endl;
				}
				else
				{
					for(i=2;i<=k;i++)
					{
						cout<<i<<" ";
					}
					cout<<endl;
				}
			}
		}
	}
	return 0;
}
