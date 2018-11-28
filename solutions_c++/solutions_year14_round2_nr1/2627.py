#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <iostream>
#include <functional>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <cmath>
#include <limits>

using namespace std;
typedef long long ll;

typedef vector<pair<char, int> > PairVec;

int solve(int N, const vector<string>& lines)
{
	vector<PairVec> pvs;
	for (const auto& line : lines) {
		PairVec tmp;
		for (int i = 0; i < (int)line.size(); i++) {
			if (tmp.empty() || tmp.back().first != line[i]) {
				tmp.push_back(make_pair(line[i], 1));
			} else {
				tmp.back().second++;
			}
		}
		if (!pvs.empty()) {
			if (pvs[0].size() != tmp.size())
				return -1;
			for (size_t i = 0; i < tmp.size(); i++) {
				if (pvs[0][i].first != tmp[i].first)
					return -1;
			}
		}
		pvs.push_back(tmp);
	}

	int ans = 0;
	int M = pvs[0].size();
	for (int j = 0; j < M; j++) {
		double acc = 0;
		for (int i = 0; i < N; i++) {
			acc += pvs[i][j].second;
		}
		int avg = (int)floor((acc / (double)N) + 0.5);
		for (int i = 0; i < N; i++) {
			ans += abs(avg - pvs[i][j].second);
		}
	}
	return ans;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		vector<string> lines(N);
		for (int i = 0; i < N; i++) {
			cin >> lines[i];
		}

		cout << "Case #" << t << ": ";
		int ans = solve(N, lines);
		if (ans < 0)
			cout << "Fegla Won";
		else
			cout << ans;
		cout << endl;
	}
	return 0;
}
