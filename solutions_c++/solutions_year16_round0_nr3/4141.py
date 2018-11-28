//============================================================================
// Name        : ayman.cpp
// Author      : Ayman Mostafa
// Email       : ayman93live@hotmail.com
// Version     : v5.0
//============================================================================

#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>

using namespace std;

#define all(x) x.begin(),x.end()
#define allr(x) x.rbegin(),x.rend()
#define clr(v,d) memset(v,d,sizeof(v));

const double PI = 2 * acos(0.0);
int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0 };
void fastInOut();

long long power(long long x, long long y) {
	long long z = 1;
	for (long long i = 0; i < y; i++)
		z *= x;
	return z;
}
int comp_double(double a, double b) {
	if (fabs(a - b) <= 1e-10)
		return 0;
	return a < b ? -1 : 1;
}
vector<string> v;
void sol(string s) {
	if (s.size() == 16) {
		if (s[0] == '1' && s[15] == '1')
			v.push_back(s);
		return;
	}
	sol(s + '0');
	sol(s + '1');
}
unsigned long long con(string s, int base) {
	unsigned long long res = 0;
	for (int i = 0, k = s.size() - 1; i < s.size(); i++, k--) {
		if (s[k] == '0')
			continue;
		res += (power(base, i));
	}
	return res;
}
bool *arr = new bool[1000100];
void prim(int n) {
	n++;
	for (int i = 0; i < n; i++)
		arr[i] = true;
	for (int i = 2; i * i < n; i++)
		if (arr[i])
			for (int k = i * i; k < n; k += i)
				arr[k] = false;
}
unsigned long long div(unsigned long long x) {
	for (int i = 2; i * i <= x; i++)
		if (x % i == 0)
			return i;
	return 0;
}
//----------------------------------------------------------------------------------
//----------------------------------------------------------------------------------

//##########################################################################################
//###################################MAIN FUNCTION##########################################
//##########################################################################################
int main() {
#ifndef ONLINE_JUDGE
	//freopen("B-large.in", "rt", stdin);
	freopen("C-small-attempt1.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
#endif
	fastInOut();
//----------------------------------------------------------------------------------
//----------------------------------------------------------------------------------
	int n;
	cin >> n >> n >> n;
	sol("");
	prim(1000000);
	vector<string> t, res;
	for (int i = 0; i < v.size(); i++)
		if (!arr[con(v[i], 2)])
			t.push_back(v[i]);
	cout << "Case #1:\n";
	for (int i = 0; i < t.size(); i++) {
		//cout << t[i] << " ";
		for (int k = 2; k <= 10; k++)
			//cout << div(con(t[i], k)) << " ";
			if (div(con(t[i], k)) == 0)
				goto hell;
		//cout << div(con(t[i], 10)) << endl;
		res.push_back(t[i]);
		if (res.size() >= 50)
			break;
		hell: ;
	}
	for (int i = 0; i < res.size(); i++) {
		cout << res[i] << " ";
		for (int k = 2; k < 10; k++)
			cout << div(con(res[i], k)) << " ";
		cout << div(con(res[i], 10)) << endl;
	}

}
void fastInOut() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL), cout.tie(NULL);
}
