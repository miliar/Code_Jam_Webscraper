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
	if (ans.size() == 0) {
		cout << "Case #" << caseNumber << ": " << "IMPOSSIBLE" << endl;
	} else {
		cout << "Case #" << caseNumber << ": " << ans[0] + 1;
		for (int i = 1; i < ans.size(); i++) {
			cout << " " << ans[i] + 1;
		}
		cout << endl;
	}
}

struct TState {
	map<int, int> Keys;
	vector<int> Seq;
	bool Visited;
	TState() {
		Visited = false;	
	}
};

struct TChest {
	int OpenKey;
	vector<int> Keys;
};

template <class AnswerType>
AnswerType SolveTestCase() {
	int keysCount;
	int chestsCount;
	cin >> keysCount >> chestsCount;

	int len = (1 << chestsCount);
	vector<TState> dp(len);
	dp[0].Visited = true;
	for (int i = 0; i < keysCount; i++) {
		int t;
		cin >> t;
		dp[0].Keys[t]++;
	}

	vector<TChest> chests(chestsCount);
	for (int i = 0; i < chestsCount; i++) {
		int k;
		cin >> chests[i].OpenKey >> k; 
		chests[i].Keys.resize(k);
		for (int j = 0; j < k; j++) {
			cin >> chests[i].Keys[j];
		}
	}

	for (int i = 0; i < len; i++) {
		if (!dp[i].Visited) {
			continue;
		}
		for (int j = 0; j < chestsCount; j++) {
			if (((1 << j) & i) == 0) {
				int next = i | (1 << j);
				map<int, int>::const_iterator it = dp[i].Keys.find(chests[j].OpenKey);
				if (it != dp[i].Keys.end() && it->second > 0) {
					if (!dp[next].Visited || dp[next].Seq > dp[i].Seq) {
						dp[next] = dp[i];
						dp[next].Seq.push_back(j);
						dp[next].Keys[chests[j].OpenKey]--;
						for (int h = 0; h < chests[j].Keys.size(); h++) {
							dp[next].Keys[chests[j].Keys[h]]++;
						}
					}
				}
			}
		}
	}
	if (!dp[len - 1].Visited) {
		return vector<int>();
	}
	return dp[len - 1].Seq;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("small.in", "r", stdin);
	//freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase< vector<int> >() );

	return 0;
}