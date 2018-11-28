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
//----------------------------------------------------------------------------------
//----------------------------------------------------------------------------------

//##########################################################################################
//###################################MAIN FUNCTION##########################################
//##########################################################################################
int main() {
#ifndef ONLINE_JUDGE
	//freopen("input.txt", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
#endif
	fastInOut();
//----------------------------------------------------------------------------------
//----------------------------------------------------------------------------------
	int t, n;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> n;
		int arr[10] = { 0 };
		bool res = false;
		unsigned long long resn;
		for (int k = 1; k <= 10000; k++) {
			unsigned long long tn = n * k;
			while (tn) {
				arr[tn % 10]++;
				tn /= 10;
			}
			int temp = 0;
			for (int m = 0; m < 10; m++)
				if (arr[m])
					temp++;
			if (temp == 10) {
				res = true;
				resn = k * n;
				break;
			}
		}
		cout << "Case #" << i << ": ";
		if (res)
			cout << resn;
		else
			cout << "INSOMNIA";
		cout << endl;
	}
}
void fastInOut() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL), cout.tie(NULL);
}
