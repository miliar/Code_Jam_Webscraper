#include <cstdio>
#include <iostream>
#include <cstring>
#include <set>
#include <vector>

using namespace std;

const int MaxN = 20;
const int MaxLet = 15;
const int Mod = 1000000007;

vector <int> trie[MaxN];
int N, M, maks, kol, tot, koji[MaxN];
string s[MaxN];
set <string> S;

void add (int t) {
  S.clear();
  S.insert("");
  for (int i = 0; i < trie[t].size(); ++i)
    for (int len = 1; len <= s[trie[t][i]].size(); ++len)
      S.insert(s[trie[t][i]].substr(0, len));

  tot += S.size();
}

void rec (int i) {
  if (i == N) {
    tot = 0;

    bool ok = true;
    for (int k = 0; k < M; ++k)
      if (trie[k].size() == 0)
	ok = false;

    if (!ok)
      return;

    for (int j = 0; j < M; ++j)
      add(j);
    
    if (tot > maks) {
      maks = tot;
      kol = 1;
    }
    else if (tot == maks)
      ++kol;
    return;
  }

  for (int j = 0; j < M; ++j) {
    trie[j].push_back(i);
    rec(i + 1);
    trie[j].pop_back();
  }
}

void solve (int tc) {
  maks = kol = 0;
  scanf("%d %d",&N,&M);
  for (int i = 0; i < N; ++i) {
    char in[MaxLet];
    scanf("%s",in);
    s[i] = in;
  }

  rec(0);

  printf("Case #%d: %d %d\n",tc,maks,kol);
}

int main (void) {
  int t;
  scanf("%d",&t);
  for (int c = 1; c <= t; ++c)
    solve(c);
  return 0;
}
