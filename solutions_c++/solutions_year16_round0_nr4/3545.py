#include<stdio.h>
#include<string.h>
#include<math.h>
main()
{
	//freopen("D-small-attempt0.in","r",stdin);
	//freopen("output_file.out","w",stdout);
	long long int t,ca=0,k,c,s,a,k1;
	scanf("%lld",&t);
	while(t--)
	{
		ca++;
		a=1;
		scanf("%lld",&k);
		scanf("%lld",&c);
		scanf("%lld",&s);
		k1=pow(k,c-1);
		printf("Case #%lld:",ca);
		while(k--)
		{
			printf(" %lld",a);
			a=a+k1;
		}
		printf("\n");
	}
	return 0;
}
