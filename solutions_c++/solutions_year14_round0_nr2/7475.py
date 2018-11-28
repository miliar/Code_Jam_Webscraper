#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <string.h>
#include <fstream>
#include <math.h>
#include <sstream>
#include <cctype>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cstdio>
#include <stdio.h>
#include <numeric>
#include <climits>
#include <stack>
#include <utility>

using namespace std;

#define sz(v) (int)v.size()
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define ss   stringstream
#define ll long long
#define pb push_back
#define mem(a,b) memset(a,b,sizeof(a))
#define F first
#define S second
#define cnt(x , n) count(x.begin(),x.end(),n)
#define mx(x) *max_element(x.begin(),x.end())
#define mn(x) *min_element(x.begin(),x.end())
#define ull unsigned long long
#define ac(x) accumulate(all(x),0)
#define iter(it,v) for(it=v.begin();it!=v.end();it++)
#define MP make_pair
#define next next_permutation

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.in","w",stdout);
	double n, c, f, x, con, t, m, T;
	cin >> n;
	for (int h = 1; h <= n; h++) {
		cin >> c >> f >> x;
		con = 2.0, t = 0.0, T = x / 2;
		while (true) {
			t += c / con;
			con += f;
			m = x / con;
			t += m;
			if (t > T)
				break;
			T = t;
			t -= m;
		}
		cout << "Case #" << h << ": ";
		cout.precision(7);
		cout.setf(ios::fixed);
		cout << T << endl;
	}
	return 0;
}
