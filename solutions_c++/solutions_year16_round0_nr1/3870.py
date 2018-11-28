#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main(void)
{
	int t,k;
	cin>>k;
	for( t = 1 ; t <= k ; t++)
	{
		
		ll n,ans,flag=1,c=0,tmp,m,r;
		map<int,int> m1;
		map<ll,int> m2;
		
		cin>>n;
		if(n==0)
			flag=0;
		else
		{
			m=0;
			while(c<10)
			{
				m++;
				tmp = m*n;
				//cout<<tmp<<endl;
				while(tmp>0)
				{
					r = tmp%10;
					if( m1[ r] == 0 )	
					{
						c++;
						m1[r]++;
					}
					tmp/=10;
				}
		
			}
		//	cout<<c;
			ans = m*n;
		}


		printf("Case #%i: ",t);
		if(flag)
			printf("%lli\n",ans);
		else
			puts("INSOMNIA");

		
	}



	return 0;
}
