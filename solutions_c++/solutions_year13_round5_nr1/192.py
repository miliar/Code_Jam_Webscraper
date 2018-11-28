#include <cmath>
#include <string>
#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <algorithm>
#include <stdint.h>
#include <iomanip>
using namespace std;

int t, n;
int64_t b;

vector<int64_t> played;

int max(int x, int y) { if (x > y) return x; return y;}
int min(int64_t x, int64_t y) {if (x < y) { return x;} return y;}

int64_t first_sum(int num) {
	int64_t ret = 0;
	for (int i = 0; i < num; i++) {
		ret += played[i];
	}
	return ret;
}

double find_ans(int num) {
	double profit = 0;
	for (int l = 0; l <= 37 - num; l++) {
		if (num + l == 37 || played[num + l - 1] < played[num + l]) {
			int64_t sum = first_sum(num + l);
			int64_t level = (b + sum - l) / ((int64_t) num + l);
			
			//cout << num << " " << l << " sum " << sum << " level " << level << endl;
			if (num + l < 37) {
				level = min(level, played[num + l] - 1);
				//if (l > 0) {
			//		level = min(level, played[num + l] - 2);
			//	}
			}
			//cout << num << " " << l << " sum " << sum << " level " << level << endl;
			if (level >= played[num + l - 1]) {
			if ((num * level - first_sum(num)) * 36.0 / (num + 0.0) - (num * level + l * (level + 1) - sum) > profit) {
				profit = (num * level - first_sum(num)) * 36.0 / (num + 0.0) - (num * level + l * (level + 1) - sum);
			}
				//break;
			}				
		}
	}
	return profit;
}

int main() {
	fstream in, out;
	in.open("A-small-attempt4.in", fstream::in);
	out.open("proba-small4.out", fstream::out);
	
	in >> t;
	out << setprecision(9);
    for (int i = 0; i < t; i++) {
		cout << "CASE " << i << endl;
		in >> b >> n;
		played.clear();
		int64_t temp;
		double xx;
		for (int j = 0; j < n; j++) {
			in >> temp;
			played.push_back(temp);
		}		
		for (int j = n; j < 37; j++) {
			played.push_back(0);
		}
		sort(played.begin(), played.end());
		
		double ans = 0.0;
		for (int j = max(1, 37 - n); j <= 36; j++) {
			double test_ans = find_ans(j);
			cout << j << " " << test_ans << endl;
			if (test_ans > ans) {
				ans = test_ans;
			}
		}

		out << "Case #" << i + 1 << ": " << ans << endl;
	}
 
	in.close();
	out.close();
	return 0;
}
