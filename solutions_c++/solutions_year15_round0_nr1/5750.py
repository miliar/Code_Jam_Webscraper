#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<cmath>
#include<map>
#include<set>
#include<iostream>
#include<utility>
#define MOD 1000000009
#define LL long long int
#define gc getchar
#define pc putchar
#define pb push_back
#define mp make_pair
#define all(c) c.begin(),c.end()
#define rall(c) c.rbegin(),c.rend()
#define tr(container, it) \
for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define present(container, element) (container.find(element) != container.end())
using namespace std;
int compare(const void *a,const void *b)
{
	return (*(int *)a-*(int *)b);


}
inline LL myscanf()
{
LL n=0;
int ch=gc();
while( ch < '0' || ch > '9' )
{
ch=gc();
}
while( ch >= '0' && ch <= '9' )
{
n = (n<<3)+(n<<1) + ch-'0';
ch=gc();
}
return n;
}
inline void myprintf(LL n)
{
	LL a[20];
	LL i=19,j,k;
	for(;;)
	{
		k=n%10;
		n=(n-k)/10;
		a[i--]=k;
		if(n==0)
		break;
	}
	for(j=i+1;j<=19;j++)
	pc(a[j]+'0');

	pc('\n');
}
int main()
{
int t,k,l,ans,prev_sum,i;
t=myscanf();
for(k=1;k<=t;k++)
{
	l=myscanf();
	char a[l+1];
	scanf("%s",a);
	getchar();
//	printf("%s\n",a);
	ans=0;
	prev_sum=0;
	for(i=0;i<=l;i++)
	{
		if(a[i]!='0')
		{
			//printf("akshay\n");
			int temp=a[i]-48;
			if(i<=prev_sum)
			{
				prev_sum+=temp;
			}
			else
			{
				//myprintf(prev_sum);
				//myprintf(i);
				ans+=i-prev_sum;
				//myprintf(ans);
				prev_sum+=i-prev_sum+temp;
				//myprintf(prev_sum);
			}
		}
		
	}
	printf("Case #%d: %d\n",k,ans);
}

return 0;
}

