#include<iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <vector>
#include <cstdio>
#include <string>
#include <stack>
using namespace std;
int main()
{
	int ti;
	double c,f,x,num,t,v1,v2,t1,t2,v;
	freopen("d:\\test.txt","w",stdout);
	scanf("%d",&ti);
	int count=1;
	while(ti--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: ",count++);
		/*if(x<=c)
		{
			printf("%.7lf\n",x/2);
			continue;
		}
		num=c;v=2;t=c/2;
		x-=c;
		while((x-num)/v>(x+c-num)/(v+f))
		{
			x-=c;
			v+=f;
			t+=c/v;
		}
		t+=(x-num)/v;*/
		v=2;
		t=x/2;
		int i;
		t1=0;
		for(i=0;i<=x/c;i++)
		{
			t=min(t,t1+x/v);
			t1+=c/v;
			v+=f;
		}
		printf("%.7lf\n",t);
	}
	return 0;
}
