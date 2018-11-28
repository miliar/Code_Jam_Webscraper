#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

typedef unsigned long long uint64;

struct data {
	int a, b, count;
};

template <class T>
void print(const T &v)
{
	cout << endl;
	for (auto &i : v)
		cout << i << " ";
	cout << endl;
}

const uint64 MOD = 1000002013ULL;

inline uint64 sumN(int n) {
	return (((uint64)n) * (n + 1) / 2) % MOD;
}
int n;
uint64 cost(int len) {
	return (sumN(n) - sumN(n - len)) % MOD;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int test_cases;
	cin >> test_cases;
	for (int test_num = 1; test_num <= test_cases; ++test_num) {
		cout << "Case #" << test_num << ": ";
		int m;
		cin >> n >> m;
		data tmp;
		vector<data> input;
		vector<int> stations;
		uint64 need = 0;
		uint64 real = 0;
		for (int i = 0; i < m; ++i) {
			cin >> tmp.a >> tmp.b >> tmp.count;
			tmp.a--;
			tmp.b--;
			stations.push_back(tmp.a);
			stations.push_back(tmp.b);
			input.push_back(tmp);
			need += cost(tmp.b - tmp.a) * tmp.count;
			need %= MOD;
		}
		// cout << "need : " << need << endl;
		sort(stations.begin(), stations.end());
		stations.resize(unique(stations.begin(), stations.end()) - stations.begin());
		vector<int> humans((int)stations.size() - 1, 0);
		for (int i = 0; i < (int)stations.size() - 1; ++i)
			for (auto &j : input)
				if (j.a <= stations[i] && stations[i + 1] <= j.b)
					humans[i] += j.count;

		// print(stations);
		// print(humans);

		while (1) {
			int start = 0;
			for (; start < (int)humans.size() && humans[start] == 0; ++start);
			if (start == (int)humans.size())
				break;
			int end;
			int m = humans[start];
			for (end = start + 1; end < (int)humans.size() && humans[end] != 0; ++end)
				m = min(m, humans[end]);
			// cout << "start, end : " << start << " " << end << endl; 
			for (int i = start; i < end; ++i)
				humans.at(i) -= m;
			real += (cost(stations.at(end) - stations.at(start)) * m) % MOD;
			real %= MOD;
			// print(humans);
			// cout << "min: " << m << "\nreal : " << cost(stations.at(end) - stations.at(start)) * m << endl;
		}

		uint64 ans = (MOD + need - real) % MOD;
		cout << ans << endl;
	}
	return 0;
}