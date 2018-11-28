/*************************************************************************
    > File Name: 4.cpp
    > Author: mengshangqi
    > Mail: mengshangqi@gmail.com 
    > Created Time: 2014年04月12日 星期六 19时30分34秒
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<set>
#include<map>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<bitset>
#include<sstream>
#include<queue>
#include<stack>
#include<cmath>
using namespace std;
const int N=1005;
double a[N],b[N];
int main()
{
#ifndef ONLINE_JUDGE
    freopen("4.in","r",stdin);
	freopen("4.out","w",stdout);
#endif
	int t;
	int n;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		set<double>sa,sb;
		int res1=0,res2=0;
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>a[i],sa.insert(a[i]);

		for(int i=0;i<n;i++)
			cin>>b[i],sb.insert(b[i]);

		set<double>:: iterator it,tt;
		
		for(it=sa.begin();it!=sa.end();it++)
		{
			double num=*it;
			tt=sb.lower_bound(num);
			if(tt!=sb.end())
				sb.erase((*tt));
			else {
				tt=sb.begin();
				res1++;
				sb.erase((*tt));
			}
		}
		sa.clear();
		sb.clear();
		for(int i=0;i<n;i++)
		{
			sa.insert(a[i]);
			sb.insert(b[i]);
		}
		for(it=sa.begin();it!=sa.end();it++)
		{
			double num=*it;
			if(num>(*sb.begin()))
			{
				res2++;
				tt=sb.begin();
				sb.erase((*tt));
			}else {
				tt=--sb.end();
				sb.erase((*tt));
			}
		}
		printf("Case #%d: %d %d\n",c,res2,res1);
	}
    return 0;
}
