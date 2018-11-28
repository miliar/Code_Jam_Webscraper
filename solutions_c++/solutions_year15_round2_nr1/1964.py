#include<stdio.h>
int l1;
long long int a[1000010];
long long int length(long long int x)
{
		long long int y=0;
		while(x)
		{
        	 y++;
        	 x/=10;
   		 }
    return y;
}
long long int reverse(long long int x)
{
	long long int rev=0,r;
	l1=0;
	while(x){
         r=x%10;
         rev=rev*10+r;
         x/=10;l1++;
    }
    return rev;
}
main()
{
	freopen( "A-small-attempt0.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	long long int n,i,temp,T,t;
	a[1]=1;
	for(i=2;i<=1000000;i++)
	{
		temp=reverse(i);
		if(temp<i&&a[temp]<a[i-1]&&l1==length(temp))
		{
			a[i]=a[temp]+1;
		}
		else
		a[i]=a[i-1]+1;
	}
	scanf("%lld",&T);
	t=1;
	while(t<=T)
	{
		scanf("%lld",&n);
		printf("Case #%lld: %lld\n",t,a[n]);
		t++;
	}
	return 0;
}		
