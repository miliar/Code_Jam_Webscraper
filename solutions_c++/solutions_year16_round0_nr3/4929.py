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
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int t = 0, c = 0;
	int n, j;
	cin >> t;
	while (c<t)
	{
		c++;
		cin >> n>>j;
		cout << "Case #"<<c<<":"<< endl;
		ll s = (1 << (n - 1)) + 1;
		bitset<32> bs;
		for (int i = 0; i < j; s += 2){
			bs = s;
			vector<ll> vals;
			vector<ll> factors;
			
			for (int k = 2; k <= 10; k++){
				ll valbasek = 0;
				for (int h = 0; h < n; h++){
					valbasek += bs[h] * pow(k, h);
				}
				bool isbasek_prime = 1;
				for (ll m = 2; m < sqrt(valbasek); m++){
					if (valbasek % m == 0){
						vals.push_back(valbasek);
						factors.push_back(m);
						isbasek_prime = 0;
						break;
					}
				}
				if (isbasek_prime)break;
			}
			if (factors.size()==9){
				i++;
				string str = bs.to_string();
				str = str.substr(32-n, n);
				cout << str;
				for (auto v : factors){
					cout << " " << v;
				}
				cout << endl;
			}

		}
		
	}
	return 0;
}
#endif