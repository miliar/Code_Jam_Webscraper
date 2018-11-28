#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <sstream>
using namespace std;

typedef unsigned long long ULL;

struct node
{
	int end;
	int next[26]; // a-z
};
struct word
{
	int lang; // 0, 1=E, 2=F, 3=EF
	string content;
};
#define MXNODE 40000
node trie[MXNODE];
int nodes = 1;

vector<word> W;

int insert(char * w)
{
	int p = 0;
	int i = 0;
	for (int i=0;w[i];++i) {
		int nx = w[i]-'a';
		int np = trie[p].next[nx];
		if (!np) {
			np = trie[p].next[nx] = nodes ++;
			memset(&trie[np], 0, sizeof(node));
		}
		p = np;
	}
	if (!trie[p].end) {
		trie[p].end = W.size();;
		W.push_back(word());
		W.back().content = w;
		W.back().lang = 0;
	}
	return trie[p].end;
}

int N;
vector<int> S[200];

void input()
{
	nodes = 1;
	memset(&trie[0], 0, sizeof(node));
	W.clear(); W.push_back(word()); // dummy

	string buf;
	cin >> N; getline(cin, buf); // end of line
	for (int i=0;i<N;++i) {
		S[i].clear();
		getline(cin, buf);
		istringstream iss (buf);
		char word[16];
		while (iss >> word) {
			S[i].push_back(insert(word));
		}
		/*
		for (int j=0;j<S[i].size();++j) {
			cout << S[i][j] << " ";
		} cout << endl;
		// */
	}
}

int try_it(int flag)
{
	vector<int> mark(W.size(), 0);
	for (int i=0;i<W.size();++i)
		mark[i] = W[i].lang;
	for (int i=0;i<N-2;++i) {
		int id = i+2;
		int f = 0;
		if (flag & (1<<i)) { // FR
			f = 2;
		} else { // EN
			f = 1;
		}
		for (int j=0;j<S[id].size();++j) {
			mark[S[id][j]] |= f;
		}
	}
	int cnt = 0;
	for (int i=1;i<W.size();++i) {
		if (mark[i] == 3) ++cnt;
	}
	return cnt;
}

int solve()
{
	for (int i=0;i<S[0].size();++i) {
		W[S[0][i]].lang |= 1;
	}
	for (int i=0;i<S[1].size();++i) {
		W[S[1][i]].lang |= 2;
	}
	/*
	for (int i=1;i<W.size();++i) {
		cout << i << ": (" << W[i].lang << ") [" << W[i].content << "]" << endl;
	}
	// */
	int ans = W.size();
	for (int f=0; f<(1<<(N-2)); ++f) {
		int c = try_it(f);
		if (c < ans) ans = c;
	}

	return ans;
}

int main()
{
	int T, nCase = 1;
	cin >> T;
	while (T--) {
		input();
		cout << "Case #" << nCase ++ << ": ";
		cout << solve();
		// solv();
		cout << endl;
	}

	return 0;
}

