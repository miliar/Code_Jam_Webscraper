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
int main()
{
	int t,case_num=0;
	double c,f,x,ans,temp,now;
	scanf("%d",&t);
	while (t--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		ans=x/2.0;
		now=2.0;
		temp=0;
		while (1)
		{
			temp+= (c/now);
			now+=f;
			if(temp+ (x/now) <ans)
			{
				ans= temp+(x/now);
			}
			else
			{
				break;
			}
		}
		printf("Case #%d: %.7lf\n",++case_num,ans);
	}
	return 0;
}