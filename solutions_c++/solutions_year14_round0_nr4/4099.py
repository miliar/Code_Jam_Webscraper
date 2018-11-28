#include <set>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int war(set<int> p1, set<int> p2) {
  int cnt = 0;
  while(p1.size() > 0) {
    if(*p1.rbegin() > *p2.rbegin()) {
      p2.erase(*p2.begin());
      p1.erase(*p1.rbegin());
      cnt++;
    } else {
      p2.erase(p2.lower_bound(*p1.begin()));
      p1.erase(*p1.begin());      
    }
  }
  return cnt;
}

int deceit(set<int> p1, set<int> p2) {
  int cnt = 0;
  while(p1.size() > 0) {
    if(*p1.begin() > *p2.begin()) {
      p1.erase(*p1.begin());
      p2.erase(*p2.begin());
      cnt++;
    } else {
      p1.erase(*p1.begin());
      p2.erase(*p2.rbegin());
    }
  }

  return cnt;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    printf("Case #%d:", t);
    
    int N;
    cin >> N;
    
    set<int> p[2];
    for(int j = 0; j < 2; j++) {
      for(int i = 0; i < N; i++) {
        string n;
        cin >> n;
        n = n.substr(2);
        p[j].insert(atoi(n.c_str()));
      }
    }
   
    // printf("[");
    // for(int x : p[0])
    //   printf("%d ", x);
    // printf("]\n");

    // printf("[");
    // for(int x : p[1])
    //   printf("%d ", x);
    // printf("]\n");

    printf(" %d %d\n", deceit(p[0], p[1]), war(p[0], p[1]));
  }

  return 0;
}
