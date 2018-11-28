#include <cstdio>
#include <vector>
#include <string>
#include <map>
using namespace std;

// PREPROCESS INPUT WITH:
// sed '/[a-z]/s/$/ ./'

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    int N;
    scanf("%d", &N);
    fprintf(stderr, "(%d %d)\n", tc, N);
    vector<vector<int> > lines(N);

    map<string,int> wordmap;

    for (int i = 0; i < N; i++) {
      while (true) {
        char buf[600];
        scanf("%s", buf);
        if (buf[0] == '.') break;
        if (!wordmap.count(buf)) {
          int k = wordmap.size();
          wordmap[buf] = k;
        }
        lines[i].push_back(wordmap[buf]);
      }
    }

    long long best = -1;

    for (int s = 0; s < (1<<(N-2)); s++) {
      vector<char> words(wordmap.size(), 0);

      for (int i = 0; i < N; i++) {
        bool eng = (i == 0 ? true : i == 1 ? false : !!(s & (1<<(i-2))));
        for (int w : lines[i]) words[w] |= (eng ? 1 : 2);
      }

      long long r = 0;
      for (char p : words) if (p == 3) r++;

      if (s == 0 || r < best) best = r;
    }

    printf("Case #%d: %lld\n", tc, best);
  }
}
