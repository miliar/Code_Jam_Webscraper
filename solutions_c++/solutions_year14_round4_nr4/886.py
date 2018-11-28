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
#include <unordered_set>

using namespace std;

template<class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cerr << "Case #" << caseNumber << endl;
	cout << "Case #" << caseNumber << ": " << ans.first << " " << ans.second << endl;
}

pair<int, int> ans; 

void Rec(int pos, int n, const vector<string>& s, vector<int>& split) {
    if (pos == s.size()) {
        int curSize = 0;
        for (int i = 0; i < n; i++) {
            bool used = false;
            unordered_set<string> pref;
            for (int j = 0; j < s.size(); j++) {
                if (split[j] == i) {
                    used = true;
                }
            }
            if (!used) {
                return;
            }
        }

        for (int i = 0; i < n; i++) {
            unordered_set<string> pref;
            for (int j = 0; j < s.size(); j++) {
                if (split[j] == i) {
                    for (int h = 0; h < s[j].length(); h++) {
                        pref.insert(s[j].substr(0, h + 1));
                    }
                }
            }
            curSize += 1 + pref.size();
        }
        if (curSize > ans.first) {
            ans.first = curSize;
            ans.second = 0;
        }
        if (curSize == ans.first) {
            ans.second++;
        }
        return;
    }
    for (int i = 0; i < n; i++) {
        split[pos] = i;
        Rec(pos + 1, n, s, split);
    }
}

template <class AnswerType>
AnswerType SolveTestCase() {
    int m, n;
    cin >> m >> n;
    vector<string> s(m);
    for (int i = 0; i < m; i++) {
        cin >> s[i];
    }
    ans = make_pair(0, 0);
    vector<int> split(m, 0);
    Rec(0, n, s, split);
    return ans;   
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("D-small.in", "r", stdin);
	//freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase< pair<int, int> >() );

	return 0;
}