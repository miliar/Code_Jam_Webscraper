#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	ll tt,t,n,s,str;char arr[101];
	scanf("%lld",&tt);
	t=0;
	while(t!=tt)
	{
		ll count=0;
		t++;
		
		scanf("%s",arr);
		
		if(arr[0]=='-')
		{
		count++;
		ll i=0;
		while(arr[i]=='-')
		arr[i++]='+';
	    }
	    
	    for(ll i=0;i<strlen(arr)-1;i++)
	    {
	    	if(arr[i]=='+' && arr[i+1]=='-')
	    {
	    	count+=2;
	    //	printf("found a pair\n");
	    }
		}
		
	printf("Case #%lld: %lld\n",t,count);
	}
	return 0;
}