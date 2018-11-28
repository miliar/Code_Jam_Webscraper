//
//  A.cpp
//  CODE
//
//  Created by Vikas Yadav on 29/10/14.
//  Copyright (c) 2014 Vikas Yadav. All rights reserved.
//

#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iterator>
#include <memory.h>
#include <cassert>

using namespace std;

typedef long long LL;

#define pb push_back
#define mp make_pair
#define gc getchar_unlocked
#define F first
#define S second
#define endl '\n'

#define PI 3.14159265

long long myPower(long long a, long long p){
	if(p==0)    return 1;
	if(p==1)    return a;
	long long temp = myPower(a,p/2);
	temp*=temp;
	temp*=myPower(a,p%2);
	return temp;
}

int main(){
	int tt = 1,ttt = 0;
	freopen("dlarge.in", "r", stdin);
	freopen("dlargeout.out", "w", stdout);
	//double st = clock();
	scanf("%d", &tt);
	while(tt--){
		long long x=0,y=0,z=0;
		long long k,c,s,ans =0;
		scanf("%lld%lld%lld", &k, &c, &s);
		printf("Case #%d: ", ++ttt);
		ans = ceil(double(k)/c);
		if(s<ans){
			printf("IMPOSSIBLE\n");
			continue;
		}
		vector < long long > answer;
		for(long long a=0;a<ans;a++){
			x = 1;
			for(long long b=1;b<=c;b++){
				x += (min(b-1+a*c,k-1))*(myPower(k,c-b));
			}
			answer.pb(x);
		}
		for(int a=0;a<answer.size();a++){
			printf("%lld ", answer[a]);
		}
		printf("\n");
	}
	//cout<<(clock()-st)/CLOCKS_PER_SEC<<endl;
	return 0;
}