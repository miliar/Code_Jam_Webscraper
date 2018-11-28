#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#ifdef HOME
	#define E(c) cerr<<#c
	#define Eo(x) cerr<<#x<<" = "<<(x)<<endl
	#define Ef(...) fprintf(stderr, __VA_ARGS__)
#else
	#define E(c) ((void)0)
	#define Eo(x) ((void)0)
	#define Ef(...) ((void)0)
#endif

const int SIZE = 256;
const int WORDS = 4<<10;

int n, w;
bool tagged[2][WORDS];
vector<int> arr[SIZE];

map<string, int> wordMap;
int GetIndex(string s) {
	if (wordMap.count(s))
		return wordMap[s];
	int t = wordMap.size();
	wordMap[s] = t;
	return t;
}

bool temp[2][WORDS];

char buff[1<<20];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	gets(buff);
	sscanf(buff, "%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		wordMap.clear();
		memset(tagged, 0, sizeof(tagged));

		gets(buff);
		sscanf(buff, "%d", &n);
		for (int i = 0; i<n; i++) {
			arr[i].clear();
			gets(buff);
			for (char *curr = strtok(buff, " "); curr; curr = strtok(0, " ")) {
				int id = GetIndex(string(curr));
				if (i < 2) tagged[i][id] = true;
				else arr[i-2].push_back(id);
			}
		}
		n -= 2;
		w = wordMap.size();

		int ans = 1000000000;
		for (int m = 0; m < 1<<n; m++) {
			memcpy(temp, tagged, sizeof(temp));
			for (int t = 0; t < n; t++) {
				int st = (m >> t) & 1;
				for (int i = 0; i < arr[t].size(); i++)
					temp[st][arr[t][i]] = true;
			}
			int tres = 0;
			for (int t = 0; t < w; t++)
				tres += temp[0][t] && temp[1][t];
			ans = min(ans, tres);
		}
		
		printf("Case #%d: %d\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
