#include <bits/stdc++.h>
using namespace std;
#define in(n) scanf("%lld",&n)
int main() { 
	// your code goes here
	long long t,k,c,s,T,a,ans,te;
	
	in(t);
	T=t;
	
	while(t--)
	{
		in(k);
		in(c);
		in(s);
		
		
		printf("Case #%lld: ",T-t);
			
		a=k/c;
		if(k%c!=0)
		a++;
		
		if(s<a)
		printf("IMPOSSIBLE");
		
		else
		{
			for(long long i=0;i<a;i++)
			{
				ans=0;
				
				for(long long j=1;j<=c;j++)
				{
					te=i*c+j;
					if(te>k)
					te=k;
					
					te--;
					
					ans=ans*k+te;
					
				}
				ans++;
				printf("%lld ",ans);
			}
		}
		
		printf("\n");
	}
	return 0;
}