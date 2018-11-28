#include<cstdio>
#include<iostream>
#include<cstring> 
#include<vector>
#include<algorithm>
#include<queue>
#include<cmath>
#include<cstdlib>
#define MAXN 100010
#define PI 3.14159265359
#define LEN 0.00001
#define base 100000
#define e 2.71828182846
#define YU 1000000007
#define INF 2147483647
//#define N 50005
using namespace std;
double a[1010],b[1010];
int main()
{
	int t,case_num=0,n,ans1,ans2,k;
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d",&n);
		for (int i = 0; i < n; i++)
		{
			scanf("%lf",&a[i]);
		}
		for (int i = 0; i < n; i++)
		{
			scanf("%lf",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		ans1=0;
		ans2=0;
		k=0;
		for (int i = 0; i < n; i++)
		{
			if(a[i]>b[k]){ans1++;k++;}
		}
		k=0;
		for (int i = 0; i < n; i++)
		{
			if(b[i]>a[k]){ans2++;k++;}
		}
		ans2= n-ans2;
		printf("Case #%d: %d %d\n",++case_num,ans1,ans2);
	}
	return 0;
}