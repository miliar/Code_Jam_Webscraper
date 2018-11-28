#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>
using namespace std;

pair<double, double> flip(pair<double, double> x) {
	return make_pair(x.second, x.first);
}

pair<double, double> read_pair(istream &fi) {
	pair<double, double> ans;
	fi >> ans.first >> ans.second;
	ans.second *= ans.first;
	return ans;
}

void go(vector<pair<double, double>> v) {
	{
		double sum1 = 0, sum2 = 0;
		for (auto x : v) {
			sum1 += x.first;
			sum2 += x.second;
		}
		if (sum1>sum2)
			transform(v.begin(), v.end(), v.begin(), flip);
	}
	sort(v.begin(), v.end(), [](pair<double, double> x, pair<double, double> y) {
		return x.first*y.second>x.second*y.first;
	});

	double sum1 = 0, sum2 = 0;
	{
		for (auto x : v) {
			double r = (sum2 - sum1) / (x.first-x.second);
			if (x.first >= x.second*(1-100*numeric_limits<double>::epsilon())) {
				r = 1;
			}
			if (!(r<1))
				r = 1;
			if (!(r>0))
				r = 0;
			sum1 += r * x.first;
			sum2 += r * x.second;
		}
	}

	if (std::fabs(sum1-sum2) > 1000*numeric_limits<double>::epsilon()*sum2 || sum2==0 || sum1==0)
		cout << "IMPOSSIBLE";
	else
		cout << setprecision(16) << (1/sum1);
}

void run_test(istream &fi) {
	int n;
	fi >> n;
	pair<double, double> y = read_pair(fi);
	vector<pair<double, double>> v(n);

	for (int i=0; i<n; i++) {
		v[i] = read_pair(fi);

		v[i].first /= y.first;
		v[i].second /= y.second;
	}
	go(v);
}

#include <fstream>

int main() {
	int n;
	istream &fi = cin;
	fi >> n;
	for (int i=1; i<=n; i++) {
		cout << "Case #" << i << ": ";
		run_test(fi);
		cout << endl;
	}
}
