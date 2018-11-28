#include<bits/stdc++.h>
using namespace std;
void add(int a[10],long n)
{
	while(n>0)
	{
		a[n%10]=1;
		n/=10;
	}
}
int check(int a[10])
{
	for(int i=0;i<10;i++)
	if(a[i]==0)
	return 0;
	return 1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++)
	{
	    long n;
	    scanf("%ld",&n);
    	int a[10]={0,0,0,0,0,0,0,0,0,0};
    	long i;
    	if(n==0)
    	    printf("Case #%d: INSOMNIA",T);
        else
    	for(i=1;1;i++)
    	{
    		long te=i*n;
    		add(a , te );
    		if(check(a)==1)
    		{
    			printf("Case #%d: %d",T,i*n);
    			break;
			}
		}
		printf("\n");
   }
	return 0;
}
