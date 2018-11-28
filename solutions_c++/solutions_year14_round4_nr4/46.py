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

const int CHARS = 'Z' - 'A' + 1;
int get(char c) { return c - 'A'; }

struct Node {
	int next[CHARS];
	Node() {
		memset(next, -1, sizeof(next));
	}
};

int m, n;
vector<string> words;

vector<Node> nodes;
vector<int> roots;

int ans;
int bestCnt;

vector<int> goesTo;
void SolveRec(int u) {
	if (u == m) {
		nodes.clear();
		roots.clear();

		for (int i = 0; i<n; i++) {
			roots.push_back(nodes.size());
			nodes.push_back(Node());
		}

		vector<int> pop(n, 0);
		for (int i = 0; i<m; i++) {
			int curr = roots[goesTo[i]];
			pop[goesTo[i]]++;
			const auto& str = words[i];
			for (int j = 0; j < str.size(); j++) {
				int c = get(str[j]);
				if (nodes[curr].next[c] < 0) {
					nodes[curr].next[c] = nodes.size();
					nodes.push_back(Node());
				}
				curr = nodes[curr].next[c];
			}
		}

		if (count(pop.begin(), pop.end(), 0))
			return;

//		Eo(nodes.size());
		if (ans < int(nodes.size())) {
			ans = nodes.size();
			bestCnt = 0;
		}
		if (ans == nodes.size())
			bestCnt++;

		return;
	}

	for (int i = 0; i<n; i++) {
		goesTo.push_back(i);
		SolveRec(u+1);
		goesTo.pop_back();
	}
}

char buff[1<<20];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d", &m, &n);
		words.clear();
		for (int i = 0; i<m; i++) {
			scanf("%s", buff);
			words.push_back(buff);
		}

		ans = bestCnt = -1;
		goesTo.clear();
		SolveRec(0);
		Eo(ans);

		printf("Case #%d: %d %d\n", tt, ans, bestCnt);
		fflush(stdout);
	}
	return 0;
}
                