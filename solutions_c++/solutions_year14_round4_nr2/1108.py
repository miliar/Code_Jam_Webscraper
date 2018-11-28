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

int Check(vector<int> p, const vector<int>& a, int maxPos) {
    int ans = 0;
    for (int i = 0; p[i] != maxPos; i++) {
        if (a[p[i]] > a[p[i + 1]]) {
            return 1000;
        }
    }
    for (int i = p.size() - 1; p[i] != maxPos; i--) {
        if (a[p[i]] > a[p[i - 1]]) {
            return 1000;
        }
    }
    for (int i = 0; i < p.size(); i++) {
        ans += abs(p[i] - i);
        for (int j = i + 1; j < p.size(); j++) {
            if (p[j] < p[i] && p[j] >= i) {
                p[j]++;
            }
            if (p[j] > p[i] && p[j] <= i) {
                p[j]--;
            }
        }
    }
    return ans;
}


int SolveSmall() {
    int n;
    cin >> n;
    vector<int> a(n);

    int maxPos = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] > a[maxPos]) {
            maxPos = i;
        }
    }
    vector<int> perm(n);
    for (int i = 0; i < n; i++) {
        perm[i] = i;
    }
    int ans = 1000;
    ans = min(ans, Check(perm, a, maxPos));
    while (next_permutation(perm.begin(), perm.end())) {
        ans = min(ans, Check(perm, a, maxPos));
    }
    return ans;
}

template <class AnswerType>
AnswerType SolveTestCase() {
    return SolveSmall();
    int n;
    cin >> n;
    vector< pair<int, int> > a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i].first;
        a[i].second = i;
    }
    sort(a.begin(), a.end());
    int maxPos = a.back().second;
    int ans = n * n;
    auto prev = a;

    for (int m = 0; m < n; m++) {
        int cur = 0;
        a = prev;
        vector< pair<int, int> > left;
        vector< pair<int, int> > right;
        for (int i = 0; i < n; i++) {
            if (i == maxPos) {
                continue;
            }
            if (a[i].second >= m && a[i].second < maxPos) {
                a[i].second++;
            }
            if (a[i].second <= m && a[i].second > maxPos) {
                a[i].second--;
            }

            if (a[i].second < m) {
                left.push_back(a[i]);
            } else {
                right.push_back(a[i]);
                right.back().second -= m + 1;
            }
        }
        sort(left.begin(), left.end());
        for (int i = 0; i < left.size(); i++) {
            cur += abs(left[i].second - i);
        }
        sort(right.rbegin(), right.rend());
        for (int i = 0; i < right.size(); i++) {
            cur += abs(right[i].second - i);
        }
        cur = cur /2 + abs(m - maxPos);
        ans = min(ans, cur);
    }

	return ans;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("B-small.in", "r", stdin);
	//freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase<int>() );

	return 0;
}