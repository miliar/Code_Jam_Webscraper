#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
// 初期化！
int t, vol_ans1, vol_ans2;
int card1[4][4], card2[4][4]; // 1 to 16

void solve(int testnum) {
  vector<int> ans;
  ans.clear();
  rep(i,4) {
    rep(j,4) {
      //cout << card1[vol_ans1][i] << " " << card2[vol_ans2][j] << endl;
      if (card1[vol_ans1][i] == card2[vol_ans2][j]) {
	//cout << "same:" << card1[vol_ans1][i] << " " << card2[vol_ans2][j] << endl;
	ans.push_back(card1[vol_ans1][i]);
      }
    }
  }
  if (ans.size() == 0) {
    printf("Case #%d: Volunteer cheated!\n", testnum);
  }
  else if (ans.size() > 1) {
    printf("Case #%d: Bad magician!\n", testnum);
  }
  else {
    printf("Case #%d: %d\n", testnum, ans.at(0));
  }
}

int main() {
  cin >> t;
  rep(i,t) {
    cin >> vol_ans1;
    vol_ans1 = vol_ans1 - 1; // 0 origin
    rep(j,4) { // initialize the cards for first time.
      rep(k,4) {
	cin >> card1[j][k];
      }
    }
    cin >> vol_ans2;
    vol_ans2 = vol_ans2 - 1; // 0 origin
    rep(j,4) { // initialize the cards for second time.
      rep(k,4) {
	cin >> card2[j][k];
      }
    }
    solve(i+1); // 1 origin
  }


  return 0;
}
