#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <iomanip>
#include <bitset>
#include <string>
#include <sstream>
using namespace std;

const double epsilon  = 1e-9;
typedef long long ll;
typedef long double ld;

int main() {
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for (int testCounter = 1; testCounter <= numTests; testCounter++) {
		printf("Case #%d: ", testCounter);
		int n;
		double t, v;
		cin >> n >> v >> t;
		double debit, temp;
		double positiveDebit = 0;
		double negativeDebit = 0;
		double positiveAmount = 0;
		double negativeAmount = 0;
		double factor, totalDebit;
		double neutralDebit = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> debit >> temp;
			if (fabs(t - temp) < epsilon) {
				neutralDebit += debit;
			} else if (temp < t) {
				positiveDebit += debit;
				positiveAmount += (t - temp) * debit;
			} else {
				negativeDebit += debit;
				negativeAmount += (temp - t) * debit;
			}
			
		}
		if (fabs(negativeAmount) < epsilon || fabs(positiveAmount) < epsilon) {
			if (neutralDebit > epsilon) {
				printf("%.9lf\n", v / neutralDebit);
				continue;
			} else {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
		}
		if (positiveAmount > negativeAmount) {
			factor = negativeAmount / positiveAmount;
			totalDebit = negativeDebit + factor * positiveDebit + neutralDebit;
			printf("%.9lf\n", v / totalDebit);
		} else {
			factor = positiveAmount / negativeAmount;
			totalDebit = factor * negativeDebit + positiveDebit + neutralDebit;
			printf("%.9lf\n", v / totalDebit);
		}
		
	}
	return 0;
}
