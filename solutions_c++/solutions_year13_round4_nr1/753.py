#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#define loop(a,b,c) for (int a = b; a < c; a++)

using namespace std;

int main() {
  int tc;
  cin >> tc;
  loop (a,0,tc) {
    long long n,m;
    cin >> n >> m;
    vector<vector<long long> > ppl;
    map<long long,int> bkpts;
    vector<long long> pts;
    set<long long> ptsset;
    loop (i,0,m) {
      long long s,e,p; cin >> s >> e >> p;
      vector<long long> x; x.push_back(s); x.push_back(e); x.push_back(p);
      ppl.push_back(x);
      ptsset.insert(s); ptsset.insert(e);
    }
    for (set<long long>::iterator it = ptsset.begin(); it != ptsset.end(); it++) {
      bkpts[*it] = pts.size();
      pts.push_back(*it);
    }
    int p = pts.size();
    long long dp[p];
    loop (i,0,p) dp[i] = 0;
    loop (i,0,ppl.size()) {
      loop (j,bkpts[ppl[i][0]],bkpts[ppl[i][1]]) dp[j] += ppl[i][2];
    }
    //loop (i,0,m) cout << ppl[i][0] << " " << ppl[i][1] << " " << ppl[i][2] << "\n";
    //loop (i,0,pts.size()) cout << pts[i] << " ";
    //cout << "\n";
    long long tot = 0;
    int head = 0;
    while (1) {
      //loop (i,0,p) cout << dp[i] << " ";
      //cout << ": " << tot << "\n";
      while (dp[head] == 0 && head < p) head++;
      if (head == p) break;
      long long minv = dp[head];
      int tail = head+1;
      while (dp[tail] > 0) {
        minv = (minv < dp[tail]) ? minv : dp[tail];
        tail++;
      }
      tot = (tot + (((pts[tail]-pts[head])*(pts[tail]-pts[head])) % 2000004026) * minv) % 2000004026;
      loop (i,head,tail) dp[i] -= minv;
    }
    long long oldtot = 0;
    loop (i,0,m) {
      oldtot = (oldtot + (((ppl[i][1] - ppl[i][0]) * (ppl[i][1] - ppl[i][0])) % 2000004026) * ppl[i][2]) % 2000004026;
    }
    cout << "Case #" << (a+1) << ": " << ((tot-oldtot)/2+1000002013)%1000002013 << "\n";
    //cout << "@@@@@@@@@============a==============@@@@@@@@@@@@@@22\n";
  }
}
