#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main() {
	int t,k;
	scanf("%d",&t);
	int ar[10];
	for(k=1;k<=t;k++)
	{
		ll n,i=1,j,f=0;
		scanf("%d",&n);
		for(i=0;i<10;i++)
	    ar[i]=0;
	    if(n==0)
	    printf("Case #%d: INSOMNIA\n",k);
	    else
	    { ll n1,cnt=0;
	    i=1;
		while(!f)
		{f=1;
		  n1=(ll)n*(ll)i;
		  cnt=n1;
		  while(n1!=0)
		  {
		  	int last=n1%10;
		  	n1/=10;
		  	ar[last]=1;
		  }
		    for(j=0;j<10;j++)
		  	{
		  		if(ar[j]!=1)
		  		f=0;
		  	}
		  i++;
		}
	   printf("Case #%d: %lld\n",k,cnt);
	  }
	}
	return 0;
}
