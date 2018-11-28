#include <bits/stdc++.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

#define dd(x)  cerr << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define SORT(c) sort((c).begin(),(c).endd())
#define PB push_back

using namespace std;

int main() {
  int problem_num;

  cin >> problem_num;

  FOR(pn,0,problem_num) {
    int x, r, c;
    cin >> x >> r >> c;
    int gote_win = false;
    if (r > c) {int tmp = r; r = c; c = tmp;}
    int area = r*c;

    if (x == 1) {
      gote_win = true;

    } else if (x == 2) {
      if (area%2==0) gote_win = true;
      else           gote_win = false;

    } else if (x == 3) {
      if (r==1) {
        gote_win = false;
      } else if (r==2) {
        if (area%6==0) gote_win = true;
        else           gote_win = false;
      } else if (r==3) {
        gote_win = true;
      } else if (r==4) {
        gote_win = false;
      }

    } else if (x == 4) {
      if (r==1) {
        gote_win = false;
      } else if (r==2) {
        gote_win = false;
      } else if (r==3) {
        if (c<=3) gote_win = false;
        else      gote_win = true;
      } else if (r==4) {
        gote_win = true;
      }
    }

    if (gote_win) printf("Case #%d: GABRIEL\n", pn+1);
    else          printf("Case #%d: RICHARD\n", pn+1);

  }

  return 0;
}
