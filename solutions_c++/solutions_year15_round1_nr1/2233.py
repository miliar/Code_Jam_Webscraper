#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int Case = 1;Case <= T;Case++) {
    int n;
    vector<int> v;
    //input
    cin >> n;
    while(n--) {
      int a;
      cin >> a;
      v.push_back(a);
    }

    int a1,a2;
    //solve
    int last = -1;
    a1 = 0;
    //a1
    for (size_t i = 0;i < v.size();i++) {
      if (v[i] < last) {
        a1 += last - v[i];
      }
      last = v[i];
    }

    //a2
    float min_rate = 0;
    for (size_t i = 0;i < v.size()-1;i++) {
      for (size_t j = i+1;j < v.size();j++) {
        double rate = (v[j]-v[i])/double(j-i);
        if (rate < min_rate) min_rate = rate;
      }
    }
    //printf("rate = %f\n",min_rate);
    //calc eaten
    a2 = 0;
    last = v[0];
    for (size_t i = 1;i < v.size();i++) {
      a2 += std::min(float(last),-min_rate);
      last = v[i];
    }
    printf("Case #%d: %d %d\n",Case,a1,a2);
  }
}
