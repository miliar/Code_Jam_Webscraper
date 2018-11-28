#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int N, ret, mxid;
vector<char> vch;
vector<int> vx;

void doit(int i, int b) {
  for (int j = mxid+1; j+1 < 15; j++) {
    if ((b&(1<<j)) && !(b&(1<<(j+1)))) return;
  }
  if (i == N) {
    int cur = 0;
    for (int j = 0; j < 15; j++) cur += !!(b&(1<<j));
    ret = min(ret, cur);
  } else if (vch[i] == 'E' && vx[i] != 0) {
    int j = vx[i]-1;
    if (b&(1<<j)) return;
    doit(i+1, b+(1<<j));
  } else if (vch[i] == 'L' && vx[i] != 0) {
    int j = vx[i]-1;
    if (!(b&(1<<j))) return;
    doit(i+1, b-(1<<j));
  } else if (vch[i] == 'E') {
    for (int j = 0; j < 15; j++)
      if (!(b&(1<<j))) doit(i+1, b+(1<<j));
  } else if (vch[i] == 'L') {
    for (int j = 0; j < 15; j++)
      if (b&(1<<j)) doit(i+1, b-(1<<j));
  }
}

main() {
  int T, prob=1;
  for (cin >> T; T--;) {
    cin >> N;
    vch.resize(N);
    vx.resize(N);
    for (int i = 0; i < N; i++) cin >> vch[i] >> vx[i];
    vector<int> id(2001);
    mxid = 0;
    for (int i = 0, n = 1; i < N; i++) {
      if (vx[i] && id[vx[i]] == 0) id[vx[i]] = n++;
      mxid = max(mxid, id[vx[i]]);
    }
    for (int i = 0; i < N; i++) vx[i] = id[vx[i]];
    ret = 1000;
    for (int b = 0; b < (1<<15); b++) {
      doit(0, b);
    }
    if (ret == 1000) goto fail;

    cout << "Case #" << prob++ << ": " << ret << endl;
    continue;
fail:
    cout << "Case #" << prob++ << ": CRIME TIME" << endl;
  }
}
