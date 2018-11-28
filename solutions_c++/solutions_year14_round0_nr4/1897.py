#include<iostream>
#include<stdio.h>
#include<cstring>
#include<stdlib.h>
#include <queue>
#include<string>
#include <sstream>
#include<list>
#include<map>
#include<cmath>
#include<algorithm>
#include <unordered_map>
using namespace std;
#define INF 1e9
#define DIVIDE 10000

int main()
{
	int	flag = 0,answer,n,i=0,j,index = 0;
	freopen ("d:/Codejam/D-large.in","r",stdin);
    freopen ("d:/Codejam/D-large.out","w",stdout);
	int ans1,ans2,R,C,M;
	scanf("%d",&n);
	double b[1005],c[1005];
	bool b_ex[1005],c_ex[1005];
	while(n--)
	{
		cin>>R;
		for(i=0;i<R;i++)
			scanf("%lf",&b[i]);
			
		for(i=0;i<R;i++)
			scanf("%lf",&c[i]);
			
		sort(b,b+R);
		sort(c,c+R);
		memset(b_ex,true,sizeof(b_ex));
		int naomi_dwar = 0,ken_dwar=0;

		for(i=0 ; i<R ;)//ken
		{
			for(j=0 ; j<R ; j++)//naomi
			{
				if(b_ex[j])
				{
					if(b[j] > c[i])
					{
					b_ex[j] = false;
					naomi_dwar++;
					i++;
					break;
					}
				}
			}
			if(j == R)
				goto z;
		}
z: ken_dwar= R - naomi_dwar;

		int naomi_war = 0,ken_war = 0;
		memset(c_ex,true,sizeof(c_ex));
		for(j=0 ; j<R ; )//naomi
		{
			for(i=0 ; i<R ;i++)//ken
			{
				if(c_ex[i])
				{
					if(b[j] < c[i])
					{
					c_ex[i] = false;
					ken_war++;
					j++;
					break;
					}
				}
			}
			if(i == R)
				goto y;
		}
y: naomi_war = R - ken_war;
			printf("Case #%d: ",++index);
			printf("%d %d\n",naomi_dwar,naomi_war);
	}
	return 0;
}
