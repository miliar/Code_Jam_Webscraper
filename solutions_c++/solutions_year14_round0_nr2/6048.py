// zoj.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include<string>
#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<math.h>;
using namespace std;
long long mod=1000000007;
long long ans=0;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for (int cs=1;cs<=t;cs++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double v=2;
		double ans=0;
		while (x>=(c+c/f*v))
		{
			ans+=c/v;
			//x-=c;
			v+=f;
		}
		ans+=x/v;
		printf("Case #%d: %.7lf\n",cs,ans);
	}
	return 0;
}