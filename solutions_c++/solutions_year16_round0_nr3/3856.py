#include<stdio.h>
#include<string.h>
#include<math.h>
#include <stdlib.h>
using namespace std;
long long a[9];
char s[16];
long long base(char s[],int x)
{
	long long sum=0;
	int i=16;
	while(i--)
	{
		sum+=(long long)(s[i]-'0')*(long long)pow(x, 15-i);

	}
	return sum;
}
long long noprime(long long a)
{
	long long q=sqrt(a);
	for(long long i=2;i<=q;i++)
	{
		if(a%i==0)
		return i;
	}
	return 0;
}
int main()
{
	freopen("C-small-attempt3.in","r",stdin);
	freopen("C-small-attempt3.out","w",stdout);
	int T;
	scanf("%d",&T);
	int N,J;
	int j=1;
	while(T--)
	{
		scanf("%d%d",&N,&J);
		long long num=1;
		num=(num<<15)+1;
		printf("Case #1:\n");
		int count=0;
		while(1)
		{
			int flag=1;
			for(int i=2;i<=10;i++)
			{
				itoa(num,s,2);
				long long tem=base(s,i);
				a[i-2]=noprime(tem);
				if(a[i-2]==0)
				{
					flag=0;
					break;
				}
			}
				if(flag==1)
				{
					itoa(num,s,2);
					printf("%s",s);
					for(int i=0;i<9;i++)
					{
						printf(" %lld",a[i]);
					}
					printf("\n");
					count++;
				}
				if(count==J)
				break;
				num=num+2;
		}

	}
}
