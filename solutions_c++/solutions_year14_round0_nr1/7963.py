#include <iostream>
#include <iomanip>
#include <array>
#include <string>
#include <algorithm>
using namespace std;

int main(){
  int T; cin >> T;
  for(int t=1;t<=T;++t) {
    int row1,row2;
    array<array<int,4>,4> prev,post;
    cin >> row1;
    for(auto &i: prev) for(auto &j: i) cin >> j;
    cin >> row2;
    for(auto &i: post) for(auto &j: i) cin >> j;
    sort(prev[row1-1].begin(),prev[row1-1].end());
    sort(post[row2-1].begin(),post[row2-1].end());
    vector<int> intersect(4);
    vector<int>::iterator it;
    it = set_intersection(prev[row1-1].begin(),prev[row1-1].end(),
                          post[row2-1].begin(),post[row2-1].end(),
                          intersect.begin());
    intersect.resize(it - intersect.begin());
    //for(auto i: intersect) cout << i << endl;
    cout << "Case #" << t << ": ";
    if(intersect.size()>1) {
      cout << "Bad magician!";
    } else if(intersect.empty()) {
      cout << "Volunteer cheated!";
    } else {
      cout << intersect[0];
    }
    cout << endl;
  }
  return 0;
}
