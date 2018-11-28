#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <vector>
#include <cmath>
#include <climits>
#include <queue>
#include <cassert>
#include <iostream>
#include <sstream>
#include <utility>
#include <bitset>
#include <iomanip>
using namespace std;
#define PI 3.14159265358979323846264338327950288
vector<string> Tokenize(string s, string ch) {
	vector<string> ret;
	for (int p = 0, p2; p < s.size(); p = p2 + 1) {
		p2 = s.find_first_of(ch, p);
		if (p2 == -1)
			p2 = s.size();
		if (p2 - p > 0)
			ret.push_back(s.substr(p, p2 - p));
	}
	return ret;
}
int my_abs(int a) {
	int i = a >> 31;
	return ((a ^ i) - i);
}

vector<double> TokenizeInt(string s, string ch) {
	vector<double> ret;
	vector<string> p = Tokenize(s, ch);
//	for (auto x : p) {
//		cout << x << " ";
//	}
//	cout << endl;
	for (int i = 0; i < p.size(); i++)
		ret.push_back(atof(p[i].c_str()));
	return ret;
}

void process(vector<double> NaomiBlocks, vector<double> KenBlocks, int Case) {
	int N = NaomiBlocks.size();
	if (N == 1) {
		if (NaomiBlocks[0] < KenBlocks[0]) {
			printf("Case #%d: %d %d\n", Case, 0, 0);
		} else {
			printf("Case #%d: %d %d\n", Case, 1, 1);
		}
		return;
	}

	int ansWar = 0, ansDeceit = 0;
	sort(begin(NaomiBlocks), end(NaomiBlocks));
	sort(begin(KenBlocks), end(KenBlocks));
	for (int i = 0, j = 0; i < N, j < N;) {
		if (KenBlocks[j] > NaomiBlocks[i]) {
			i++;
			j++;
			continue;
		} else {
			j++;
			ansWar++;
		}
	}
//	auto it = upper_bound(begin(NaomiBlocks), end(NaomiBlocks),
//			*prev(end(KenBlocks), 2));
//	if (it != end(NaomiBlocks)) {
//		if (*it < *prev(end(KenBlocks), 1)) {
//			ansWar = distance(it, end(NaomiBlocks)) - 1;
//		} else {
//			ansWar = distance(it, end(NaomiBlocks));
//		}
//	} else {
//		ansWar = 0;
//	}
//ansDeceit
	auto ik = upper_bound(begin(KenBlocks), end(KenBlocks), NaomiBlocks.back());
	int toBeRemoved = distance(ik, end(KenBlocks));
	auto ij = upper_bound(begin(NaomiBlocks) + toBeRemoved, end(NaomiBlocks),
			*begin(KenBlocks));
	for (auto i = ij; i != end(NaomiBlocks); i++) {
		auto j = find_if(begin(KenBlocks), end(KenBlocks),
				bind2nd(less<float>(), *i));
		if (j != end(KenBlocks)) {
			ansDeceit++;
			NaomiBlocks.erase(i);
			i--;
			KenBlocks.erase(j);
			j--;
		}
	}
//	ansDeceit = distance(ij, end(NaomiBlocks));
//	int i = 0;
	printf("Case #%d: %d %d\n", Case, ansDeceit, ansWar);
}
int main() {
	vector<float> v1 = { 0.62, 0.22, 0.04, 0.83, 0.05, 0.60, 0.58, 0.08, 0.80,
			0.20 };
	vector<float> v2 = { 0.32, 0.90, 0.54, 0.21, 0.26, 0.29, 0.35, 0.23, 0.75,
			0.86 };
	sort(begin(v1), end(v1));
	sort(begin(v2), end(v2));

	for (auto x : v1) {
		cout << setw(5) << x << " ";
	}
	cout << endl;
	for (auto x : v2) {
		cout << setw(5) << x << " ";
	}
	cout << endl;
	reverse(begin(v2), end(v2));
	for (auto x : v2) {
		cout << setw(5) << x << " ";
	}
	cout << endl;

	int Case = 1;
	int T;
	char tmp[10000];
	int p[100];
	double res;
	vector<string> names;
	scanf("%d", &T);
	getchar();
	while (T--) {
		string s;
		getline(cin, s);
		getline(cin, s);
//		cout<<s<<endl;
		vector<double> NaomiBlocks = TokenizeInt(s, " ");
		getline(cin, s);
//		cout<<s<<endl;
		vector<double> KenBlocks = TokenizeInt(s, " ");
//		for (auto x : NaomiBlocks) {
//			cout << x << " ";
//		}
//		cout << endl;
//		for (auto x : KenBlocks) {
//			cout << x << " ";
//		}
//		cout << endl;
		process(NaomiBlocks, KenBlocks, Case++);
//		printf("Case #%d: %.7lf\n", Case++, res);
	}
	return 0;
}
