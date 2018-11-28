/*
 *	Category: CodeJam
 *  Problem: B.CookieClickerAlpha.cpp
 *  Status: 
 * 	Date: Apr 12, 2014
 * 	Start: 2:18:34 AM	End: 		Duration: 
 * 	Author: Hossam Yousef
 */

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <cmath>
#include <deque>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <complex>
#include <sstream>
#include <utility>
#include <climits>
#include <cstring>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

#define OO (int)1e9
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define mems(s,v) memset(s,v,sizeof(s))

int main() {
	freopen("test.txt", "rt", stdin);
	freopen("o.txt", "wt", stdout);
	int t = 0, tc;
	double C, F, X, S;
	cin >> tc;
	while(tc--){
		S = 2.0;
		cout << "Case #" << ++t << ": ";
		cin >> C >> F >> X;
		double sum = 0.0, s = 2e9, e = -1.0;
		while(1){
			e = sum + X/S;
			sum += C/S;
			S += F + 1e-6;
			if(e >= s){
				printf("%.7lf\n",s+1e-7);
				break;
			}
			s = e;
		}
	}
	return 0;
}
