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

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t = 0, c = 0;
	string s;
	cin >> t;
	while (c<t)
	{
		c++;
		cin >> s;
		string::iterator end = unique(s.begin(), s.end());
		s = s.substr(0,end-s.begin());
		int res = s.size();
		if (s[s.size() - 1] == '+')res--;
		cout << "Case #"<<c<<": "<< res << endl;
	}
	return 0;
}
#endif