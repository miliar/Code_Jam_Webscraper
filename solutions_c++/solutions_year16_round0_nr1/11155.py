#include <bits/stdc++.h>
using namespace std;

vector<int> v(10);

bool check(long long int temp)
{
   while(temp)
   {
   	 v[temp%10]++;
   	 temp/=10;
   }
   for(long long int i=0;i<10;i++)
   {
   	 if(v[i]==0)
   	  return false;
   }
  return true; 
}

int main() {
	long long int t,i,n,k,temp;
	scanf("%lld",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%lld",&n);
		if(n==0)
		{
			printf("Case #%lld: INSOMNIA\n",k);
	    	continue;
	    }
		for(i=0;i<10;i++)
		 v[i]=0;
		for(i=1;i<10000;i++)
		{
			temp=n*i;
			if(check(temp))
			 break;
		}
		printf("Case #%lld: %lld\n",k,temp);
	}
	return 0;
}