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

long long n;
bool vis[11];

void postmartem(long long no){
	while(no>0){
		vis[no%10] = true;
		no/=10;
	}
}

int main(){
	int tt = 1,ttt = 0;
	freopen("alarge.in", "r", stdin);
	freopen("alargeout.out", "w", stdout);
	//double st = clock();
	scanf("%d", &tt);
	while(tt--){
		long long x = 0,y,z;
		vector < int > ans;
		scanf("%lld", &n);
		printf("Case #%d: ", ++ttt);
		bool flag = true;
		for(int a=0;a<10;a++)		vis[a] = false;
		for(long long a=1;a<=1000;a++){
			postmartem(a*n);
			flag = true;
			x = a*n;
			for(int b=0;b<10;b++){
				flag &= vis[b];
			}
			if(flag)		break;
		}
		if(flag)		printf("%lld\n", x);
		else			printf("INSOMNIA\n");
	}
	//cout<<(clock()-st)/CLOCKS_PER_SEC<<endl;
	return 0;
}