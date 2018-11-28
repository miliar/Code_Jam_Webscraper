#include<bits/stdc++.h>
using namespace std;
long long int power(long long int x, long long  int y)
{
    long long int temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}
int main()
{
	int t;
    long long int k,c,s;
	scanf("%d",&t);
	for(int m=1;m<=t;m++)
	{
		scanf("%lld%lld%lld",&k,&c,&s);
		if(c==1)
		{
			cout<<"Case #"<<m<<": ";
			for(long long int i=1;i<=k;i++)
			cout<<i<<" ";
			cout<<endl;
		}
		else
		{
			cout<<"Case #"<<m<<": ";
			long long int p=power(k,c-1);
		  for(long long int j=0;j<=k-1;j++)
		   	printf("%lld ",1+j*p);
		   cout<<endl;
	    }
		
	}
	return 0;
}
