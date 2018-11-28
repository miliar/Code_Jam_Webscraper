/*
 * codejam2014b.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: ahmedfarag
 */

#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iterator>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <bitset>
#include <cstring>
#include <climits>
#include <deque>
#include <utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#include <valarray>

//#include<bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

#define ALL(x) (x).begin(),(x).end()
#define RALL(x) (x).rbegin(),(x).rend()
#define SZ(x) (int)(x).size()
#define MEMSET(x,val) memset((x),(val),sizeof(x))

#define OO 1e9
#define EPS 1e-9
const double PI = acos(-1);

#define MX 101
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };



int main()
{
	#ifndef ONLINE_JUDGE
    freopen("B-large.in", "r", stdin);
    freopen("bout.out", "w", stdout);
	#endif
    int t, count = 1;
    double c, f, x, farms_cost, cur, res;
    cin >> t;
    while(t--){
    	farms_cost = 0;
    	cur = 2;
    	res = OO;
    	cin >> c >> f >> x;
    	for (int farms = 0; farms <= x + 1; ++farms) {
    		res = min(farms_cost + x / cur, res);
    		farms_cost += c/cur;
    		cur += f;
		}
    	printf("Case #%d: %.7lf\n", count ++,  res);
    }

    return 0;
}

