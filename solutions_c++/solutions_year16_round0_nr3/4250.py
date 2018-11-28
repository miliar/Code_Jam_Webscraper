#include <iostream>
#include <set>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

const int inf = 1e9;

vector<long long> primes;

bool solve(vector<int> &v, vector<int> &ans) {

	for (int b = 2; b <= 10; b++) {
		long long num = 0;
		int m = v.size();
		for (int i = 0; i < v.size(); i++) {
			num += pow(b, m - i - 1) * v[i];
		}

		bool flag = false;
		for (int i = 0; i < primes.size() && primes[i] * primes[i] <= num;
				i++) {
			if (num % primes[i] == 0) {
				flag = true;
				ans.push_back(primes[i]);
				break;
			}
		}

		if (!flag)
			return false;
	}
	return true;
}

void output(int caseNum, long long res) {

	if (res == -1) {
		cout << "Case " << "#" << caseNum << ": " << "INSOMNIA" << endl;
	} else
		cout << "Case " << "#" << caseNum << ": " << res << endl;
}

void output(vector<int> &v, vector<int> &ans, int t) {

	for (int x : v)
		cout << x;
	cout << ' ';
	for (int x : ans)
		cout << x << ' ';
	cout << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	vector<int> v;

	for (int i = 2; i <= 1e7; i++) {
		if (i == 2)
			primes.push_back(i);
		if (i % 2 == 0)
			continue;
		int d = 3;
		bool flag = false;
		while (d * d < i) {
			if (i % d == 0) {
				flag = true;
				break;
			}
			d += 2;
		}
		if (!flag)
			primes.push_back(i);
	}

	v.resize(16, 0);
	v[0] = 1;
	v[v.size() - 1] = 1;

	vector<int> ans;
	int cnt = 0;
	cout << "Case " << "#" << 1 << ": \n";
	for (int i = 0; i <= v.size() - 2; i++) {
		for (int j = 1; j <= i; j++)
			v[v.size() - 1 - j] = 1;
		do {
			ans.clear();
			if (solve(v, ans)) {


				cnt++;
				output(v, ans, cnt);
				if (cnt == 50) return 0;
			}
		} while (next_permutation(++v.begin(), --v.end()));

	}

}
