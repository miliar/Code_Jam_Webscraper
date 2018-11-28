/*************************************************************************
    > File Name: 2.cpp
    > Author: mengshangqi
    > Mail: mengshangqi@gmail.com 
    > Created Time: 2014年04月12日 星期六 17时06分12秒
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
const double inf=99999999;
int main()
{
#ifndef ONLINE_JUDGE
    freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
#endif
	int t;
	cin>>t;
	for(int C=1;C<=t;C++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double v=2.0;
		double ans=x/v;
		double ti=c/v;
		for(int i=1;;i++)
		{
			double xx=x/(v+f);
			if(ti+xx<ans)
			{
				ans=ti+xx;
				v=v+f;
				ti+=c/v;
			}else break;
		}
		printf("Case #%d: %.7lf\n",C,ans);
	}
    return 0;
}
