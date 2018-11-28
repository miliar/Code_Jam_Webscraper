#include <iostream>
#include <iomanip>
#include <limits>

#define rep(i,m,n) for(int i = m; i < (int)n; i++)
#define REP(i,n) rep(i,0,n)

using namespace std;

double C, F, X;

void input() {
  cin >> C >> F >> X;
  return;
}

double solve() {
  double production = 2.0;
  double pre_ans = numeric_limits<double>::max();
  double now_ans = X/production;
  double base_time = 0.0;
  int factory = 0;
  while (now_ans < pre_ans) {
    base_time += C / (production + factory * F);
    factory += 1;
    pre_ans = now_ans;
    now_ans = base_time + X / (production + factory * F);
  }
  return pre_ans;
}

int main() {
  int T;
  cin >> T;
  REP(t, T) {
    input();
    cout << "Case #" << t+1 << ": "
	 << fixed << setprecision(11)
	 << solve() << endl;
  }
  return 0;
}
