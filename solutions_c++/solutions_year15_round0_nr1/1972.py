#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
  int t;
  cin >> t;
  for(int k = 0 ; k < t; ++k){
    int smax;
    cin >> smax;
    char ch;
    vector<int> ss;
    for(int i = 0; i <= smax; ++i){
      cin >> ch;
      for(int j = 0; j < ch - '0'; ++j)
        ss.push_back(i);
    }
    sort(ss.begin(), ss.end());
    int sum = 0;
    int cnt = 0;
    for(int i= 0; i < ss.size(); ++i){
      if(ss[i] <= sum) {
        ++sum;
      }
      else {
        cnt += ss[i] - sum;
        sum = ss[i] + 1;
      }
    }
    cout << "Case #" << k+1 << ": " << cnt << endl;
  }

  return 0;
}
