#include <iostream>
using namespace std;


long long rec[1000001][3];
long long T, N;
bool rec2[1000001];

long long reverse(int n) {
  long long v = 0;
  while(n>0) {
    v = v*10;
    v += n%10;
    n = n/10;
  }
  return v;
}

void init() {
  for (int i=0; i<1000001; ++i) {
    rec2[i] = false;
  }
}

void path(int i) {
  while(i>0) {
    cout << "--- " << rec[i][1] << " " << rec[i][0] << endl;
    i = rec[i][2];
  }
}

int main() {

  cin >> T;
  for (int k=1; k<=T; ++k) {
    cin >> N;
    int i=0, j=1;
    init();
    rec[0][0] = N;
    rec[0][1] = 0;
    int count  = 0;
    while( i<j && rec[i][0] > 10) {
      long long rN = reverse(rec[i][0]);
      //cout << "---- " << i << "  " << rec[i][0] << "  " << rec[i][1] << endl;
      if (rec[i][0]%10 != 0 && rN > 10 && rN < rec[i][0] && !rec2[rN]) {
        rec[j][0] = rN;
        rec[j][2] = i;
        rec[j++][1] = rec[i][1] + 1;
        rec2[rN] = true;
      }
      if (!rec2[rec[i][0] - 1]) {
        rec[j][0] = rec[i][0] - 1;
        rec[j][2] = i;
        rec[j++][1] = rec[i][1] + 1;
        rec2[rec[i][0] - 1] = true;
      }
      ++i;
      count++;
    }
    //path(i);
    long long ans = rec[i][0] + rec[i][1];
    cout << "Case #" << k << ": " << ans << endl;
  }
  return 0;
}
