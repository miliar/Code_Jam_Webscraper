#include <iostream>
#include <string>
#include <list>
#include <sstream>
#include <map>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

#define FOR(i, n) for (int i = 0; i < n ; ++ i)

map<string, int> words;


int n;
int nphrases[20];
int phrases[20][1000];

int language[2][4000];
int common;

void process(int p, int lang) {
  FOR(i, nphrases[p]) {
    int w = phrases[p][i];
    language[lang][w]++;
    if (language[lang][w] == 1 && language[1-lang][w] > 0) {
      ++common;
    }
  }
}

void unprocess(int p, int lang) {
  FOR(i, nphrases[p]) {
    int w = phrases[p][i];
    language[lang][w]--;
    if (language[lang][w] == 0 && language[1-lang][w] > 0) {
      --common;
    }
  }
}

int recurse(int p) {
  if (p == n) {
    //printf("best %d\n", common);
    return common;
  }

  int b = 1000000;
  process(p, 0);
  b = min(b, recurse(p+1));
  unprocess(p, 0);
  process(p, 1);
  b = min(b, recurse(p+1));
  unprocess(p, 1);
  return b;
}

void solve(int testcase) {
  cin >> n;

  words.clear();
  memset(nphrases, 0, sizeof(nphrases));
  memset(language, 0, sizeof(language));
  common = 0;

  string x;
  getline(cin, x);
  FOR(i, n) {
    getline(cin, x);
    //cout << "phrase: "<< x << endl;
    istringstream iss(x);
    while (iss >> x) {
      if (words[x] == 0) { words[x] = words.size(); }
      phrases[i][nphrases[i]++] = words[x];
    }

    //FOR(j, nphrases[i]) cout << phrases[i][j] << " "; cout << endl;
  }

  process(0, 0);
  process(1, 1);
  int best = recurse(2);

  printf("Case #%d: %d\n", testcase, best);
}

int main() {
  int T;
  cin >> T;
  FOR(i, T) solve(i+1);
  return 0;
}
