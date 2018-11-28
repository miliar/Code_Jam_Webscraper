#include<iostream>
using namespace std;
#define dbg 0
#define pdb if (dbg) cout <<

int main() {
  int t, sMax, caseNo = 1;
  char ss[1001];
  int qs[1001];
  int qt[1001];
  cin >> t;
  while (t--) {
    cout << "Case #" << caseNo++ << ": ";
    cin >> sMax;
    for (int i = 0; i <= sMax; i++) {
      cin >> ss[i];
      if (i == 0) {
        qs[i] = 0;
        qt[i] = ss[i]-48;
      }
      else {
        if (qt[i - 1] >= i) {
          qs[i] = qs[i - 1];
          qt[i] = qt[i - 1] + ss[i]-48;
        }
        else {
          qs[i] = qs[i - 1] + i - qt[i - 1];
          qt[i] = i + ss[i]-48;
        }
      }
      pdb "i=" << i << ", ss=" << ss[i] << ", qs=" << qs[i] << ", qt=" << qt[i] << endl;
    }
    cout << qs[sMax] << endl;
  }
}