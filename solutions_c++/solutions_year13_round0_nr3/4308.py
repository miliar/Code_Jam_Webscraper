#include <cstdio>
#include<algorithm>
#include <queue>

#define FORN(i,a,b) for (int i = (a); i <= (b); i++)
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define S ({int x; scanf("%d%*c", &x); x;})
#define PN(x) ({printf("%d\n", x);})
#define PS(x) ({printf("%d ", x);})
#define NL ({printf("\n");})
#define printarr(i, x, y) ({for(int i=0;i<y;i++){ printf("%d ", x[i]);} printf("\n");})
#define inputarr(i, x, y) ({for(int i=0;i<y;i++){ scanf("%d", &x[i]);}})
#define MOD 1000000007
#define LL long long

using namespace std;
int main()
{
	int len=0, r, n=0;
	long long int x;
	int a[20];
	long long int arr[100000];
	for(int i=1; i<=10000010; i++)
	{
		len=0;
		int flag=0;
		r=i;
		while(r>0)
		{
			a[len++]=r%10;
			r/=10;
		}
		for(int j=0; j<len/2; j++)
			if(a[j]!=a[len-1-j])
				flag=1;
		if(!flag)
		{
			len=0;
			x=(long long int)i*(long long int)i;
			while(x>0)
			{
				a[len++]=x%10;
				x/=10;
			}
			for(int j=0; j<len/2; j++)
				if(a[j]!=a[len-1-j])
					flag=1;
			if(!flag)
			{
				arr[n++]=(long long int)i*(long long int)i;
			}
		}
	}

	int n5;
	n5=S;
	int casenum=0;
	while(n5--)
	{
		int num, num2;
		long long int j, k;
		casenum++;
		scanf("%lld%lld",&j, &k);
		for(int i=0; i<n; i++)
		{
			if(arr[i]>=j)
			{
				num=i;
				//printf("%lld\n", arr[i]);
				break;
			}
		}
		for(int i=0; i<n; i++)
		{
			if(arr[i]==k)
			{
				num2=i-num+1;
				//printf("%lld\n", arr[i]);
				break;
			}
			else if(arr[i]>k)
			{
				num2=i-num;
				break;
			}
		}
		printf("Case #%d: %d\n", casenum, num2);
	}

return 0;
}
