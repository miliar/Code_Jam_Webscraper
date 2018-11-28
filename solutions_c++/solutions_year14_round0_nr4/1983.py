/**
 * @author neko01
 */
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstring>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
typedef long long LL;
#define INF 0x7fffffff
const double eqs=1e-8;
double a[1005];
double b[1005];
int main()
{
	int t,cnt=0;
	//freopen("D-large.in" , "r" , stdin);
    //freopen("D-large.out" , "w" , stdout);
	scanf("%d",&t);
	while(t--)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(int j=0;j<n;j++)
			scanf("%lf",&b[j]);
		sort(a,a+n);
		sort(b,b+n);
		int ans1=0,ans2=0;
		for(int i=0,j=0;i<n&&j<n;)
		{
			if(b[j]>a[i])
			{
				ans2++;
				j++,i++;
			}
			else
				j++;
		}
		for(int i=0,j=0;i<n&&j<n;)
		{
			if(a[i]>b[j])
			{
				ans1++;
				j++,i++;
			}
			else
				i++;
		}
		ans2=n-ans2;
		printf("Case #%d: %d %d\n",++cnt,ans1,ans2);
	}
	return 0;
}