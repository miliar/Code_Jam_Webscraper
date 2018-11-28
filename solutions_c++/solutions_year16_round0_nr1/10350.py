#include<bits/stdc++.h>
using namespace std ;

#define ll long long

ll a[11] ;

bool check(){
	for(int i=0;i<=9;i++)
		if(a[i] == 0)
			return false ;
	return true ;
}

int main()
{
	int t,i ;
	scanf("%d",&t);
	for(i = 1 ; i<=t ; i++)
	{
		ll n , x=2;
		for(int g=0 ; g<=9 ;g++)
			a[g] = 0 ;
		scanf("%lld",&n);
		ll c  = n ;
		if(n == 0){
			printf("Case #%d: INSOMNIA\n",i );
		}
		else
		{
			while(1)
			{
				ll y = c ;
				while(y)
				{	
					ll k = y%10 ;
					if(a[k] == 0)
						a[k]++ ;  
					y = y/10 ;
				}
				if(check() == true)
				{
					printf("Case #%d: %lld\n",i,c );
					break ;
				}
				c = n*x ;
				x++ ;
			}
			}
		}
		return 0 ;
	}
