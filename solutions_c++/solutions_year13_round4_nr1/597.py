#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

typedef long long ll;

class P{
public:
  int beg;
  int end;
  int num;

};

bool operator<(const P &a, const P& b){
  if(a.beg == b.beg)
    return a.end < b.end;
  return a.beg < b.beg;
}

int N, M;
P p[1000];

const ll MOD = 1000002013;

ll f(int d){
  return (N+3)*N/2 - (d+3)*d/2;
}

int main(void){
  int T;
  cin >> T;
  for(int k = 0; k < T; ++k){
    cin >> N >> M;
    for(int i = 0; i < M; ++i)
      cin >> p[i].beg >> p[i].end >> p[i].num;

    sort(p, p+M);

    set<int> ts;

    ll total = 0;
    for(int i = 0; i < M; ++i){
      total += f(p[i].end - p[i].beg) * p[i].num;
      total %= MOD;
      ts.insert(p[i].beg);
      ts.insert(p[i].end);
    }

    ll ss = 0;
    vector<P> s;
    for(set<int>::iterator iter = ts.begin(); iter != ts.end(); ++iter){
      int t = *iter;
      for(int i = 0; i < M; ++i){
        if(p[i].beg == t)
          s.push_back(p[i]);
      }
      for(int i = 0; i < M; ++i){
        if(p[i].end == t){
          while(p[i].num > 0){
            if(s.back().num >= p[i].num){
              ss += p[i].num * f(p[i].end - s.back().beg);
              s.back().num -= p[i].num;
              p[i].num = 0;

              if(s.back().num == 0)
                s.pop_back();
            }
            else{
              p[i].num -= s.back().num;
              ss += s.back().num * f(p[i].end - s.back().beg);
              s.pop_back();
            }

            ss %= MOD;
          }
        }
      }
    }

    // cout << total << " "  << ss << endl;

    cout << "Case #" << k+1 << ": " << total - ss << endl;
  }

  return 0;
}
