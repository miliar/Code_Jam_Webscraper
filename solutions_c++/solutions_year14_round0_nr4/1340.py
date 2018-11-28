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
double a[1050],b[1050];
int main() {
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int tt,ri=0;
	int i,j,k,n,m;
	scanf("%d",&tt);
	while(tt--)
	{
		ri++;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(i=0;i<n;i++)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		int l,r,ans1=0,ans2=0;
		l=0;r=n-1;
		for(i=n-1;i>=0;i--)
		{
			if(b[r]>a[i])
			{
				r--;
			}
			else
			{
				ans2++;
				l++;
			}
		}
		l=0;r=n-1;
		for(i=0;i<n;i++)
		{
			if(a[i]>b[l])
			{
				l++;
				ans1++;
			}
			else
			{
				r--;
			}
		}
		printf("Case #%d: %d %d\n",ri,ans1,ans2);
	}
}
