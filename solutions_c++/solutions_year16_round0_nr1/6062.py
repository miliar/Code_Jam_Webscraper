//
//  Created by VectorCai on 16/04/06.
//  Copyright © 2016年 VectorCai. All rights reserved.
//
#if 1
#ifdef __GNUC__
#include <bits/stdc++.h>
#endif
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <utility>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#include <climits>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <sstream>
#include <functional>
#include <tuple>
#include <unordered_map>
using namespace std;

#define mpr make_pair
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <double, double> pdd;
typedef vector <int> vi;
typedef vector <ll> vll;
typedef vector <double> vd;
typedef vector <string> vs;
typedef map <string, int> mpsi;
typedef map <double, int> mpdi;
typedef map <int, int> mpii;

int N, M;
#define um 0xFFFFFFFF



int main(){
	freopen("A-small-attempt2.in", "r", stdin);
	
	freopen("A-small-attempt2.out", "w", stdout);
	int t = 0, c = 0;
	ll n = 0;
	scanf("%d", &t);
	while (c<t)
	{
		c++;
		scanf("%d", &n);
		if (n == 0){
			printf("Case #%d: INSOMNIA\n", c);
			continue;
		}
		int i = 1;
		set<int> digits;
		while (1){
			ll s = (i++)*n;
			while (s)
			{
				digits.insert(s % 10);
				s /= 10;
			}
			if (digits.size() == 10){
				printf("Case #%d: %lld\n", c,(i-1)*n);
				break;
			}
		}
	}
	return 0;
}
#endif