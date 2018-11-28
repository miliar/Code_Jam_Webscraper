#include <algorithm>
#include <thread>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define DEBUG(x) cerr << '>' << #x << ':' << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0; i<(a);++i)
inline bool EQ(double a, double b) {return fabs(a-b) < 1e-9;}

const int INF = 1<<29;
typedef long long ll;

map<string, int> wordMap;
int words = 0;

vector<vector<int>> sentences;

vector<int> loadSentence() {
  vector<int> sentence;
  while (true) {
    char buf[200];
    char c;
    scanf("%s%c", buf, &c);
    int word;
    auto it = wordMap.find(buf);
    if (it != wordMap.end()) {
      word = it->second;
    } else {
      word = words++;
      wordMap[buf] = word;
    }
    sentence.push_back(word);
    if (c != ' ') break;
  }
  return sentence;
}

int solve(int N, vector<vector<int>> sentences) {
  int best = INF;
  REP(m,1<<(N-2)) {
    if (m%1024==0) cerr << m << '/' << (1<<(N-2)) << '\n';
    vector<int> english = sentences[0], french = sentences[1];
    REP(i,N-2) {
      bool isFrench = m & (1<<i);
      vector<int>& target = isFrench ? french : english;
      for (int w : sentences[i+2]) target.push_back(w);
    }
    sort(english.begin(), english.end());
    sort(french.begin(), french.end());
    vector<int> intersection;
    set_intersection(english.begin(), english.end(), french.begin(), french.end(), back_inserter(intersection));
    best = min(best, (int)intersection.size());
  }
  return best;
}

int main() {
  int T;
  scanf("%d", &T);
  vector<thread> threads;
  int output[50];
  REP(t,T) {
    words = 0;
    wordMap.clear();
    sentences.clear();
    int N;
    scanf("%d ", &N);
    REP(i,N) {
      sentences.push_back(loadSentence());
    }
    vector<vector<int>> sentences_ = sentences;
    threads.emplace_back([&output, t, N, sentences_]{output[t] = solve(N, sentences_);});
  }
  REP(t,T) {
    threads[t].join();
    printf("Case #%d: %d\n", t+1, output[t]);
  }
  return 0;
}
