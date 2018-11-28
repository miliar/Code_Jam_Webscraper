#include <iostream>
#include <vector>
#include <map>
using namespace std;

#define delete_one(x) count[x]--;if(count[x] == 0) count.erase(x);
int main() {
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; tc++) {
    int P;
    map<int,int> count;
    cout << "Case #" << tc << ":";
    cin >> P;
    vector<int> X(P), Y(P);
    for(int i = 0; i < P; i++) {
      cin >> X[i];
    }
    for(int i = 0; i < P; i++) {
      cin >> Y[i];
      count[X[i]] = Y[i];
    }
    delete_one(0);
    vector<int> S;
    while(count.size() > 0) {
      S.push_back(count.begin()->first);
      int mp = 1 << (S.size() - 1);
      for(int i = 0; i < mp; i++) {
        long long p = 0;
        for(int j = 0; j < S.size() - 1; j++) {
          if(i >> j & 1) p += S[j];
        }
        delete_one(p + S.back());
      }
    }
    for(int i = 0; i < S.size(); i++) {
      cout <<  " " << S[i];
    }
    cout << endl;

  }
}
