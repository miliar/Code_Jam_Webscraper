//============================================================================
// Name        : a1.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C, Ansi-style
//============================================================================

#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<iostream>
#define N 100050
#define LL __int64
using namespace std;
int a[22][22],b[22][22];
int bo[22];
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int tt,i,j,k,ri=0,n,m;
	double c,f,x;
	scanf("%d",&tt);
	while(tt--)
	{
		ri++;
		double ans,p=2;
		double cal=0;
		scanf("%lf%lf%lf",&c,&f,&x);
		ans=x/p;
		for(i=1;i<=10000;i++)
		{
			cal+=c/p;
			p+=f;
			double sum;
			sum=cal+x/p;
			if(sum<ans)
				ans=sum;
		}
		printf("Case #%d: %.7lf\n",ri,ans);
	}
}
