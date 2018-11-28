#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

int do_count(const vector<string>& ns)
{
  set<string> rs;

  for (auto i = ns.begin(); i != ns.end(); i++) {
    for (int j = 0; j <= i->size(); j++) {
      rs.insert(i->substr(0, j));
    }
  }

  return rs.size();
}

int main()
{
  int T;

  cin >> T;

  for (int cas = 1; cas <= T; cas++) {
    int M, N;
    vector<string> Ss;

    cin >> M >> N;
    for (int i = 0; i < M; i++) {
      string s;
      cin >> s;
      Ss.push_back(s);
    }

    int maxv = 0;
    int maxc = 0;
    for (int seed = 0; seed < (1 << 2*M); seed++) {
      int sp[8];

      for (int i = 0; i < 8; i++) {
        sp[i] = (seed >> (i * 2)) & 3;
        if (sp[i] >= N) goto next;
      }
      {
        int count = 0;
        for (int i = 0; i < N; i++) {
          vector<string> Ns;
          for (int j = 0; j < M; j++) {
            if (sp[j] == i) Ns.push_back(Ss[j]);
          }
          count += do_count(Ns);
        }
        if (count == maxv) maxc++;
        else if (count > maxv) {
          maxv = count;
          maxc = 1;
        }
      }
    next:;
    }

    cout << "Case #" << cas << ": " << maxv << " " << maxc << endl;
  }

  return 0;
}
