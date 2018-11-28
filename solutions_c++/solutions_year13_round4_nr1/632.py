#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

template<class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cerr << "Case #" << caseNumber << endl;
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

struct TPath {
	int Origin;
	int End;
	long long Count;
};

/*
bool operator < (const TPath& a, const TPath& b) {
	return (a.Origin == b.Origin && a.End < b.End) || (a.Origin < b.Origin);
} */

const long long mod = 1000002013;

template <class AnswerType>
AnswerType SolveTestCase() {

	long long n;
	int m;
	cin >> n >> m;
	vector<TPath> path(m);
	vector<pair<int, int> > points(2 * m);
	long long maxSum = 0;
	for (int i = 0; i < m; i++) {
		cin >> path[i].Origin >> path[i].End >> path[i].Count;
		points[2 * i] = make_pair(path[i].Origin, -i - 1);
		points[2 * i + 1] = make_pair(path[i].End, i + 1);
		long long d = path[i].End - path[i].Origin;
		maxSum = (maxSum + (((n * (n - 1) / 2 - (n - d) * (n - d - 1)/ 2) % mod) * path[i].Count) % mod) % mod;
	}
	sort(points.begin(), points.end());
	map<int, long long> used;
	long long minSum = 0;
	for (int i = 0; i < 2 * m; i++) {
		if (points[i].second < 0) {
			used[points[i].first] += path[- points[i].second - 1].Count;
		} else {
			map<int, long long>::reverse_iterator ri = used.rbegin();
			long long left = path[points[i].second - 1].Count;
			while (left > 0) {
				long long count = min(left, ri->second);
				long long d = points[i].first - ri->first;
				minSum = (minSum + (((n * (n - 1) / 2 - (n - d) * (n - d - 1)/ 2) % mod) * count) % mod) % mod;
				ri->second -= count;
				left -= count;
				ri++;
			}
		}
	}
	return (maxSum - minSum + mod) % mod;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase<int>() );

	return 0;
}