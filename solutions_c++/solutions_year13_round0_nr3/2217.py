#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

long long int palindroms[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
int main()
{
	long long int a,b;
	int t;
	freopen("cin.txt","r",stdin);
	freopen("cout.txt","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		long long int c=0;
		scanf("%lld %lld",&a,&b);
		
		for(int j=0;j<sizeof(palindroms)/sizeof(palindroms[0]);j++)
		{
			if(palindroms[j]>b)
				break;
			if(palindroms[j]>=a && palindroms[j]<=b)
				c++;
		}
		printf("Case #%d: %lld",i,c);
		printf("\n");
	}
	return 0;
}