#include <bits/stdc++.h>
#define ll long long
using namespace std;
int prim[1234567]={0};
void gen()
{
	ll i,j;
	for(i=2;i*i<1234567;i++)
	{
		if(prim[i]==0)
		{
			for(j=2*i;j<1234567;j+=i)
				prim[j]=1;
		}
	}
}
int chk(ll n)
{
	ll i;
	for(i=2;i*i<=n;i++)
	{
		if((n%i)==0)
			return 1;
	
	}
	return 0;


}
int main ( void )
{

	int t;
	gen();
	cin>>t;
	while(t--)
	{

		ll n,k,i,c=0,l,j;
		cin>>n>>k;
		puts("Case #1:");
		ll num ,sum,arr[10],tmp;
		num = (1<<(n-1) |1);
	//	cout<<num;
		while(c<k)
		{
			tmp  = num;
			for(i=0;i<9;i++)
			{
				
				if(chk(tmp))
				{
					
				//	cout<<tmp<<" ";	
					for( j = 3 ; j < tmp ; j++)
					{
						if( (tmp%j)==0)
						{
							arr[i] = j;
							break;
						}
					}
				}
				else
					break;
				tmp = 0;
				l= 1;
				for(j=0;j<n;j++)
				{
					if(num&l)
						tmp += pow(i+3,j);
					l<<=1;	
				}

			}
			if(i==9)
			{
				c++;
				//cout<<num<<endl;
				l = 1<<(n-1);
				for(j=0;j<n;j++)
				{
					if(num&l)
						printf("1");
					else
						printf("0");
					l>>=1;	
				}
				for(i=0;i<9;i++)
				{
					printf(" %lli",arr[i]);
				}
				puts("");
			}
			num+=2;
		}
	}
	return 0;
}
