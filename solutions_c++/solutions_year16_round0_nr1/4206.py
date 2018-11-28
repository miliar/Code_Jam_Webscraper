#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <cassert>

using namespace std;

#define MAXN (1000000+1)

vector<int> results(MAXN, -1);

void addDigits(int kk, set<int> &digs) {
     while (kk) {
        digs.insert(kk%10);
        kk /= 10;
     }
}

void preprocess() {
     int nn, kk;
     for (nn=1; nn<MAXN; ++nn) {
          kk=0;
          set<int> digs;
          while (true) {
              kk+=nn;
              addDigits(kk, digs);
              if (digs.size() == 10) break;
          }
          results[nn] = kk;
     }
}

void solve() {
   int N;
   cin >> N;
   assert(N < MAXN);
   if (N == 0) {
       cout << "INSOMNIA";
       return;
   }
   cout << results[N];
}

int main() {
    preprocess();
    int T;
    cin >> T;
    int tt;
    for (tt=1; tt<=T; ++tt) {
   	cout << "Case #" << tt << ": ";
	solve();
   	cout << endl;
    }
    return 0;
}

