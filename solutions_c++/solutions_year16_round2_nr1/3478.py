#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define mk make_pair
#define pii pair<int,int>

int cnt[255];
int sol[10];

string num[] = {"ZERO", "ONE", "TWO", 
"THREE", "FOUR", "FIVE", "SIX",
 "SEVEN", "EIGHT", "NINE"};

bool done = false;

void solve(int dx) {
  if (dx == 10) {
    bool ok = true;
    for (int i = 0; i < 255; ++i)
      ok = ok && cnt[i] == 0;

    if (ok) done = 1;
    return;
  }

  vector<int> cntw(255);
  for (int i = 0; i < num[dx].size(); ++i)
    cntw[num[dx][i]]++;

  int i = 0;
  if (dx == 0) i = cnt['Z'];
  if (dx == 2) i = cnt['W'];
  if (dx == 4) i = cnt['R'];
  if (dx == 6) i = cnt['X'];
  if (dx == 8) i = cnt['G'];
  if (dx == 9) i = cnt['I'];

 // cout << dx << " " << i <<  endl;

  for (; i < 2000; ++i) {
    bool ok = 1;
    for (int k = 0; k < 255; ++k)
      ok = ok && cntw[k]*i <= cnt[k];

    if (!ok) break;

    for (int k = 0; k < 255; ++k)
      cnt[k] -= cntw[k]*i;

    sol[dx] = i;
    solve(dx + 1);
    if (done) return;

    for (int k = 0; k < 255; ++k)
      cnt[k] += cntw[k]*i;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  int tests;
  cin >> tests;
  for (int t = 1; t <= tests; ++t) {
    memset(cnt, 0, sizeof(cnt));
    memset(sol, 0, sizeof(sol));
    done = false;

    string w;
    cin >> w;

    for (int i = 0; i < w.size(); ++i)
      cnt[w[i]]++;

    solve(0);

    cout << "Case #" << t << ": ";
    for (int i = 0; i < 10; ++i) {
      for (int k = 0; k < sol[i]; ++k)
        cout << i;
    }cout << endl;
  }

 
}