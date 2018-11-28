#include <iostream>
using namespace std;
typedef long long int ull;


ull rev(ull n)
{
	ull nn=0;
	while(n)
	{
		nn=nn*10 + n%10;
		n/=10;
	}
	return nn;
}
int main() {
	// your code goes here
	ull t,i,cnt,k,tt,n;
	cin>>t;
	
	for(tt=1;tt<=t;tt++)
	{
		cin>>n;
		cnt=1;
		ull prev=1;
		for(;prev<=n;cnt++)
		{
			
			if(prev==n)break;
			ull temp=rev(prev);
			if(temp>prev && temp<=n)
			{
				prev=temp;
			}
			else
			prev++;
		}
		printf("Case #%lld: %lld\n",tt,cnt);
		}
	return 0;	
	}
	
