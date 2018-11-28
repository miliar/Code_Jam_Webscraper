#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;


int gcd(int a,int b)
{
	if(a==0)
		return b;
	else if(b==0)
		return a;
	else
		return gcd(b%a,a);
}

int main()
{
	int t;
	scanf("%d",&t);
	int a,b;
	for(int i=1;i<=t;i++)
	{	
		scanf("%d/%d",&a,&b);
		int c = gcd(a,b);
		b=b/c;a=a/c;
		double ans;
		ans=log2(b);
		if(ans-(double)((int)ans)==0.0)
			printf("Case #%d: %d\n",i,((int)ans-(int)log2(a)));
		else
			printf("Case #%d: impossible\n",i);
			
		

	}


}
