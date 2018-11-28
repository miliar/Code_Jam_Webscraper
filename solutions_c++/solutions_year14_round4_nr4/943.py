#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iostream>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

long long Cur;

// 알파벳은 대문자 26자만 입력된다고 가정
// N : 문자열 수, M : 문자열 길이
const int ALPHABETS = 26;
int toNumber(char ch) { return ch - 'A'; }
struct TrieNode {
	TrieNode* children[ALPHABETS];
	bool terminal;
	TrieNode() : terminal(false) { memset(children, 0, sizeof (children)); }
	~TrieNode() { for (int i = 0; i < ALPHABETS; i++) if (children[i]) delete children[i]; }
	void insert(const char* key)
	{
		if (*key == 0) terminal = true;
		else {
			int next = toNumber(*key);
			if (children[next] == NULL) {
				children[next] = new TrieNode();
				Cur++;
			}
			children[next]->insert(key + 1);
		}
	}
	TrieNode* find(const char* key)
	{
		if (*key == 0) return this;
		int next = toNumber(*key);
		if (children[next] == NULL) return NULL;
		return children[next]->find(key + 1);
	}
};

int N, M, K;
int P[11];
long long Ans, Ans2;
bool Chk[11];

char S[11][111];

void Recur(int Idx)
{
	if (Idx == N) {
		int F = 0;
		memset(Chk, false, sizeof (Chk));
		for (int i = 0; i < N; i++) {
			if (!Chk[P[i]]) {
				Chk[P[i]] = true;
				F++;
			}
		}
		if (F != K) {
			return;
		}
		TrieNode T[4];
		Cur = 0;
		for (int i = 0; i < N; i++) {
			T[P[i]].insert(S[i]);
			
		}
		if (Ans == Cur) {
				Ans2++;
			} else if (Ans < Cur) {
				Ans = Cur;
				Ans2 = 1;
			}
		return;
	}
	for (int i = 0; i < K; i++) {
		P[Idx] = i;
		Recur(Idx + 1);
	}
}

int main(void)
{
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC;
	scanf("%d", &TC);
	for (int tt = 1; tt <= TC; tt++) {
		
		scanf("%d%d", &N, &K);
		memset(S, 0, sizeof (S));
		for (int i = 0; i < N; i++) scanf("%s", S[i]);
		Ans = 0;
		Ans2 = 0;
		Recur(0);
		
		printf("Case #%d: %lld %lld\n", tt, Ans + K, Ans2);
	}

	return 0;
}
