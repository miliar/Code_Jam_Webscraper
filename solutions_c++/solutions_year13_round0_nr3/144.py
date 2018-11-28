/*
 * B.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Mostafa Saad
 */

#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<numeric>
#include<utility>
#include <functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define rep(i, v)		for(int i=0;i<sz(v);++i)
#define lp(i, n)		for(int i=0;i<(int)(n);++i)
#define lpi(i, j, n)	for(int i=(j);i<(int)(n);++i)
#define lpd(i, j, n)	for(int i=(j);i>=(int)(n);--i)

typedef long long ll;
const ll OO = 1e8;

const double EPS = (1e-7);
int dcmp(double x, double y) {
	return fabs(x - y) <= EPS ? 0 : x < y ? -1 : 1;
}

#define pb					push_back
#define MP					make_pair
#define P(x)				cout<<#x<<" = { "<<x<<" }\n"
typedef long double ld;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;

ll A, B, B2;
ll ans;

string arr[11] = { "", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" };

ll toNum(string &str) {
	ll num;
	istringstream iss(str);
	iss >> num;
	return num;
}
template<class T> string toStr(T par) {
	ostringstream oss;
	oss << par;
	return oss.str();
}

int mxLen;

bool isPal(ll n) {
	string s1 = toStr(n);
	string s2 = s1;
	reverse(all(s1));

	return s1 == s2;
}

vector<ll> sols;

void go(string cur) {
	ll n = cur == "" ? 0 : toNum(cur);

	if (sz(cur) > mxLen || n > B2)
		return;

	ll n2 = n * n;
	if (cur[0] != '0' && A <= n2 && n2 <= B && isPal(n2)) {
		ans++;
		sols.push_back(n2);
	}

	lpi(i, 1, 11) {
		string temp = arr[i];
		temp += cur;
		temp += arr[i];
		go(temp);
	}
}

int main() {

	freopen("C-large-1.in", "rt", stdin);
	freopen("C-large-1.out.txt", "wt", stdout);

	A = 1, B = 100000000000000LL;

	B2 = (ll) (sqrt((long double) B) + EPS);

	mxLen = toStr(B2).size();

	ans = 0;
	lp(i, 11)
		go(arr[i]);

	int cases;
	cin >> cases;
	lp(cc, cases) {
		cin >> A >> B;

		ans = 0;
		rep(i, sols)
			if (A <= sols[i] && sols[i] <= B)
				ans++;

		cout << "Case #" << cc + 1 << ": " << ans << "\n";
		//sort( all(sols) );
		//rep(i, sols)	cout<<sols[i]<<"\n";
	}

	return 0;
}
