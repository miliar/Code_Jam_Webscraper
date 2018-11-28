#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <utility>
#include <iomanip>
 
using namespace std;
 
long double dp[100010];
 
bool check(long double C, long double F, long double X, long double mid) {
    long double Max = -1;
	for(int i = 0; i <= 100000; i++) {
        Max = max(Max, 1LL * max((long double)0, (mid - dp[i])) * (1LL * F * i + 2));
    }
    return Max >= X;
}
 
long double solve(long double C, long double F, long double X) {
	long double l =  0, r = 1e5 + 1, mid = 0;
	while(r - l > 0.0000000001) {
		mid = (l + r) / 2;
		if(check(C, F, X, mid))
			r = mid;
		else
			l = mid;
	}
    return r;
}
 
int main() {
	ifstream cin("B-large.in");
	ofstream cout("output.txt");
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		long double A, B, C;
		cin >> A >> B >> C;
		long double count = 2;
		dp[1] = A / count;
		for(int i = 2; i <= 100000; i++) {
			count += B;
			dp[i] = dp[i - 1] + A / count;
		}
		cout << "Case #" << t + 1 << ": " << fixed << setprecision(12) << solve(A, B, C) << endl;
	}
	return 0;
}