#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <iomanip>
#include <bitset>
#include <string>
#include <cstring>
#include <sstream>
using namespace std;

const double epsilon  = 1e-9;
typedef long long ll;
typedef long double ld;
map<string, int> wordMap;
int index;
int doWordMapping(const string& str)
{
	map<string, int>::iterator itr;
	itr = wordMap.find(str);
	if (itr == wordMap.end()) {
		wordMap[str] = index;
		return index++;
	} else {
		return itr->second;
	}
}
int mask[1 << 13];
int tempMask[1 << 13];
int main() {
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for (int testCounter = 1; testCounter <= numTests; testCounter++) {
		printf("Case #%d: ", testCounter);
		wordMap.clear();
		index = 0;
		int n;
		cin >> n;
		vector<vector<int> > sentences(n);
		string str;
		getline(cin, str);
		int number;
		for (int i = 0; i < n; i++) {
			getline(cin, str);
			istringstream ss(str);

			while (ss >> str) {
				number = doWordMapping(str);
				sentences[i].push_back(number);
			}
		}

		set<int> english;
		set<int> french;
		memset(mask, 0, sizeof(mask));
		for (int i = 0; i < sentences[0].size(); i++) {
			mask[sentences[0][i]] |= 1;
		}
		for (int i = 0; i < sentences[1].size(); i++) {
			mask[sentences[1][i]] |= 2;
		}
		int minm = 1 << 20;
		for (int i = 0; i < (1 << n); i++) {
			memcpy(tempMask, mask, sizeof(mask));
			for (int j = 0; j < n; j++) {
				for (int k = 0; k < sentences[j].size(); k++)
				{
					if (i & (1 << j))
						tempMask[sentences[j][k]] |= 1;
					else
						tempMask[sentences[j][k]] |= 2;

				}
				
			}
			int common = 0;
			for (int i = 0; i <= index; i++) {
				if (tempMask[i] == 3)
					common++;
			}
			minm = min(minm, common);
		}

		cout << minm << endl;
	}
	return 0;
}
