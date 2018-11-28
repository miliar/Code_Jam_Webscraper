// File Name: b.cpp
// Author: darkdream
// Created Time: 2015年04月11日 星期六 23时16分58秒

#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<ctime>
#define LL long long

using namespace std;
int t; 
int n; 
int a[1005];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("output","w",stdout);
    scanf("%d",&t);
	for(int CA = 1; CA <= t; CA ++)
	{
		scanf("%d",&n);
		int MX = 0 ; 
		for(int i= 1;i <=n;i ++){
			scanf("%d",&a[i]);
			MX = max(MX,a[i]);
		}
		int ans = 1e9;
		
		for(int i = 1;i <= MX ;i ++){
			int sum = i ; 
			for(int j = 1;j <= n;j ++)
			{
			    if(a[j] > i)
				{
				  if(a[j] % i == 0 )
				  {
				    sum += a[j]/i - 1; 
				  }else sum += a[j]/i ; 
				}
			}
			ans = min(sum,ans);
		}
		printf("Case #%d: %d\n",CA,ans);
	}
return 0;
}
