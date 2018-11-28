#include <unordered_map>
#include <algorithm>
#include <vector>
#include <iostream>
#include <iomanip>
using namespace std;

typedef unordered_map<int, double> Pdf;

Pdf add(const Pdf &pdf, double pYes) {
	Pdf ans;
	for (const auto &item : pdf) {
		ans[item.first + 1] += item.second*pYes;
		ans[item.first - 1] += item.second * (1 - pYes);
	}
	return ans;
}

Pdf empty() {
	Pdf ans;
	ans[0] = 1;
	return ans;
}

double pTie(const Pdf &left, Pdf &right) {
	double sum = 0;
	for (const auto &item : left) {
		double pleft = item.second;
		double pright = right[-item.first];
		sum += pleft*pright;
	}
	return sum;
}

double solve(int k, vector<double> pYes) {
	std::sort(pYes.begin(), pYes.end());
	vector<Pdf> left(pYes.size()+1), right(pYes.size()+1);
	const int n = pYes.size();
	left[0] = empty();
	right[0] = empty();
	for (int i = 0; i < n; i++) {
		left[i + 1] = add(left[i], pYes[i]);
		right[i + 1] = add(right[i], pYes[n - i - 1]);
	}
	double best = 0;
	for (int i = 0; i <= k; i++) {
		const int j = k - i;
		const double p = pTie(left[i], right[j]);
		if (p > best)
			best = p;
	}
	return best;
}

int main() {
	//freopen(R"(C:\Users\andriuss\Documents\gcjpp\x64\Debug\B-small-attempt1.in)", "r", stdin);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int n, k;
		cin >> n >> k;
		vector<double> p(n);
		for (double &pi : p)
			cin >> pi;
		cout << "Case #" << i << ": " << setprecision(16) << solve(k, p) << endl;
	}
	return 0;
}
