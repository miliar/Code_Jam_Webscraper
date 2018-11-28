#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int main () {
  int T; cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    int d; cin >> d;

    vector<int> pans;

    for(int i = 0; i < d; i++) {
      int tmp; cin >> tmp;
      pans.push_back(tmp);
    }

    int ans = 100000000;

    for (int di=0; di<100; di++) {
      priority_queue<int> que;
      for (int i = 0; i < pans.size(); i++) {
	que.push(pans[i]);
      }

      int total = 0;
      int count = 0;
      while(!que.empty() && count < di) {
	int v = que.top();
	if (v <= 3) {
	  break;
	}
	que.pop(); count++;
	total++;
	//	if (v % 2 == 1 && (que.empty() || (v / 2 + 2 > que.top()))) {
	if (v == 9 && (que.empty() || (que.top() <= 3 || que.top() == 6))) {
	  int a = v / 2 + 2;
	  int b = v - a;
	  que.push(a); que.push(b);
	} else {
	  int a = v / 2;
	  int b = v - a;
	  que.push(a); que.push(b);
	}
      }
      if (!que.empty()) {
	total += que.top();
      }
      ans = min(ans, total);
    }
    cout << "Case #" << tc << ": " << ans << endl;
  }
  return 0;
}
