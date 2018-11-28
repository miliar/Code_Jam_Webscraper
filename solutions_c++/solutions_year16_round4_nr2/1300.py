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

vector<double> choseNumbers(const vector<double>& numbers, int k) {
	vector<double> numbers2(numbers);
	sort(numbers2.begin(), numbers2.end());
	vector<double> toReturn;
	int n = numbers2.size();
	for (int i = 0; i < k; i++) {
		toReturn.push_back(numbers2[i]);
		toReturn.push_back(numbers2[n - i - 1]);
	}
	return toReturn;
}
double multiplier(const vector<double> & numbers, int degree) {
	int n = numbers.size();
	double toRet = 0.0;
	for (int i = 0; i < (1 << n); i++) {
		int cnt = 0;
		double tmp = 1.0;
		for (int j = 0; j < n; j++) {
			if (i & (1 << j)) {
				tmp *= numbers[j];
				cnt++;
			}

		}
		if (cnt == degree) {
			toRet += tmp;
		}
	}
	return toRet;
}

long long binom(long long n, long long k) {
	long long toRet = 1;
	for (int i = 0; i < k; i++) {
		toRet *= (n - i);
		toRet /= (i + 1);
	}
	return toRet;
}

double solve1(const vector<double>& numbers, int k){
	vector<double> numbers2 = choseNumbers(numbers, k);

	double toRet = 0.0;
	bool positive = true;
	for (int m = k; m <= 2 * k; m++) {
		double factor = multiplier(numbers2, m);
		factor *= binom(m, k);
		if (positive) toRet += factor;
		else toRet -= factor;
		positive = !positive;
	}
	return toRet;
}

double bruteForce(const vector<double> & numbers, int k) {
	int n = numbers.size();
	double maxm = 0;
	for (int i = 0; i < (1 << n); i++) {
		int cnt = 0;
		vector<double> chosen;

		for (int j = 0; j < n; j++) {
			if (i & (1 << j)) {
				cnt++;
				chosen.push_back(numbers[j]);
			}
		}
		if (cnt != 2 * k) continue;
		double res = 0.0;
		for (int j = 0; j < (1 << (2 * k)); j++) {
			cnt = 0;
			double prob = 1.0;
			
			for (int l = 0; l < (2 * k); l++) {
				if (j & (1 << l)) {
					cnt++;
					prob *= chosen[l];
				}  else {
					prob *= (1.0 - chosen[l]);
				}
			}
			if (cnt == k) {
				res += prob;
			}
		}
		maxm = max(maxm, res);
	}

	return maxm;
	

}
int main() {
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for (int testCounter = 1; testCounter <= numTests; testCounter++) {
		printf("Case #%d: ", testCounter);
		int n, k;
		cin >> n >> k;
		k/= 2;
		vector<double> numbers(n);
		for (int i = 0; i < n; i++) {
			cin >> numbers[i];
		}

		double toRet = solve1(numbers, k);
		double check = bruteForce(numbers, k);
		if (fabs(check - toRet) > 0.0000001) {
			cerr << testCounter << " " << check << " " << toRet << endl;
		}
		
		printf ("%.9lf\n", check);
	}
	return 0;
}
