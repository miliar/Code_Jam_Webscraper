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
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for (int cs=1;cs<=t;cs++)
	{
		int a,b;
		int a1[20],a2[20];
		cin>>a;
		for (int i=1;i<=16;i++)
			cin>>a1[i];
		cin>>b;
		for (int i=1;i<=16;i++)
			cin>>a2[i];
		int sum=0;
		int ans=0;
		for (int i=4*a-3;i<=4*a;i++)
			for (int j=4*b-3;j<=4*b;j++)
				if (a1[i]==a2[j])
				{
					sum++;
					ans=a1[i];
				}	
		printf("Case #%d: ",cs);
		if (sum==1) cout<<ans<<endl;
		if (sum>1) cout<<"Bad magician!"<<endl;
		if (sum==0) cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}