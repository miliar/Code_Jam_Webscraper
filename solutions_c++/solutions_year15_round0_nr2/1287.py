// test.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"

#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<math.h>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int cst;
	int p[1100];
	cin>>cst;
	for (int cs=1;cs<=cst;cs++)
	{
		cout<<"Case #"<<cs<<": ";
		int ans=1101;
		int d;
		cin>>d;
		for (int i=0;i<d;i++)
			scanf("%d",&p[i]);
		for (int eat=1;eat<=1000;eat++)
		{
			int cur=0;
			for (int i=0;i<d;i++)
			{
				if (p[i]>eat) cur+=(int)(1.0*p[i]/eat+0.999-1);
			}
			cur+=eat;
			if (ans>cur) 
				ans=cur;
		}
		cout<<ans<<endl;
	}
	return 0;
}