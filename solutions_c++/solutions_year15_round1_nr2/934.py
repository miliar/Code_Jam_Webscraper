// File Name: b.sample.cpp
// Author: darkdream
// Created Time: 2015年04月18日 星期六 09时05分30秒

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
LL a[1005];
LL b , n ; 
LL count(LL t){
	LL sum = 0 ; 
	for(int i = 1;i <= b;i ++)
	{
	  sum += (t/a[i]) + 1 ;    
	}
	return sum;
}
LL fen(LL l , LL  r){
    LL m = (l + r)/2;
	while(l<= r){
		//printf("***\n");
         m = (l + r)/2;		 	
	     LL t = count(m);
		 if(t >= n){
			r = m - 1; 
		 }else l = m + 1; 
	}
	return l ; 
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("output","w",stdout);
	LL T;
	scanf("%lld",&T);
	for(int ca = 1; ca <= T ;ca ++){
		scanf("%lld %lld",&b,&n);
		for(LL i = 1;i <= b;i ++)
			scanf("%lld",&a[i]);
		printf("Case #%d:",ca);
	    if(n <= b  )
		{
			printf(" %lld\n",n);
			continue;
		}
		LL t = fen(1,1e15);
		LL num = count(t-1);
		for(int i = 1;i <= b;i ++){
		    if(t % a[i] == 0){
				num ++;
			}
			if(num == n)
			{
				printf(" %d\n",i);
				break;
			}
		}
		
	}

return 0;
}
