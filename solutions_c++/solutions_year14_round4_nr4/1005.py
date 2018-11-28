#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>

#define REP(i, N) for (int i = 0; i < (int)N; i++)
using namespace std;
typedef long long LL;

int size;

struct Trie {
  Trie* next[26];
  bool isLast;
  Trie(): isLast(false) {
    for (int i = 0; i < 26; i++) {
      next[i] = nullptr;
    }
  }
  void addWord(const string& s) {
    addWord(s, 0);
  }
  void addWord(const string& s, const int pos) {
    if ((int)s.size() == pos) {
      isLast = true;
      return;
    }
    int index = s[pos] - 'a';
    if (next[index] != nullptr) {
      next[index]->addWord(s, pos+1);
    } else {
      next[index] = new Trie();
      size++;
      next[index]->addWord(s, pos+1);
    }
  }
  bool findWord(const string& s, const int wrongChars) const{
    return findWord(s, wrongChars, 0);
  }
  bool findWord(const string& s, const int wrongChars, const int pos) const{
    bool r;
    if ((int)s.size() == pos && isLast) {
      return isLast;
    }
    if (pos < (int)s.size()) {
      int index = s[pos] - 'a';
      if (next[index] != nullptr) {
        r = next[index]->findWord(s, wrongChars, pos+1);
        if (r) return r;
      }
    }

    if (wrongChars > 0) {
      // change word, match "adc" to "abc"

      // avoid recalling same parameter
      int index = -1;
      if (pos < (int)s.size()) {
        index = s[pos] - 'a';
      }
      for (int i = 0; i < 26; i++) {
        if (i != index && next[i] != nullptr) {
          r = next[i]->findWord(s, wrongChars - 1, pos+1);
          if (r) return r;
        }
      }

      // delete word, match "abcd" to "abc"
      r = findWord(s, wrongChars - 1, pos+1);
      if (r) return r;

      // insert word, match "ac" to "abc"
      for (int i = 0; i < 26; i++) {
        if (next[i] != nullptr) {
          r = next[i]->findWord(s, wrongChars - 1, pos);
          if (r) return r;
        }
      }
    }
    return false;
  }
  ~Trie() {
    for (int i = 0; i < 26; i++) if (next[i] != nullptr) {
        delete next[i];
    }
  }
};

string lower(const string& s) {
  string res;
  REP(i, s.size()) res += tolower(s[i]);
  return res;
}

void solve_small(int caseCnt) {
  int worst = 0;
  int cnt = 0;
  size = 0;
  int M, N;
  cin >> M >> N;
  vector<string> v;
  REP(i, M) {
    string s;
    cin >> s;
    v.push_back(lower(s));
  }
  int loop = 1;
  REP(i, M) loop *= N;
  REP(i, loop) {
    int s[N] = {};
    REP(n, N) {
      int l = i;
      Trie* t = new Trie();
      size = 0;
      REP(m, M) {
        if (l % N == n) {
          t->addWord(v[m]);
        }
        l /= N;
      }
      s[n] = size + 1;
      delete t;
    }
    int sum = 0;
    bool ok = true;
    REP(i, N) if (s[i] == 1) ok = false;
    if (!ok) continue;
    REP(i, N) sum += s[i];
    if (worst == sum) {
      cnt++;
    } else if (worst < sum){
      cnt = 1;
      worst = sum;
    }
  }

  //cout << t->size << endl;
  printf("Case #%d: %d %d\n", caseCnt, worst, cnt);
}


int main(){
	int TestCase;
  cin >> TestCase;
	for(int caseCnt=1; caseCnt <= TestCase; caseCnt++){
		solve_small(caseCnt);
		//solve(caseCnt);
	}
	return 0;
}
