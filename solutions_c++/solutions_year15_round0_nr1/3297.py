// File Name: a.cpp
// Author: darkdream
// Created Time: 2015年04月11日 星期六 23时06分57秒

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
int n ;
int t ; 
int tmp; 
int main(){
   freopen("A-large.in","r",stdin);
   freopen("output","w",stdout);
   scanf("%d",&t);
   for(int CA = 1; CA <= t; CA ++)
   {
      scanf("%d",&n);
	  int sum = 0;
	  int ans = 0; 
	  for(int i= 0 ;i <= n;i ++)
	  {
	     scanf("%1d",&tmp);
		 if(sum < i )
		 {
		   ans += i - sum ;
		   sum = i ; 
		 }
		 sum += tmp ; 
	  }
	  printf("Case #%d: %d\n",CA,ans);
   }
return 0;
}
