#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <deque>
using namespace std;

int go(double *a, double *b, int sz){
  int c = 0, d = 0;
  for( ; d < sz; d++){
    while(c < sz && b[c] < a[d]) c++;
    if(c == sz) break;
    c++;
  }
  return sz - d;
}

int main(){
  freopen("in.txt", "r", stdin);
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++){
    int N;
    double a[1000], b[1000];
    cin >> N;
    for(int i = 0; i < N; i++) cin >> a[i];
    for(int i = 0; i < N; i++) cin >> b[i];
    sort(a, a + N);
    sort(b, b + N);
    int res = go(a, b, N), v = 0;
    deque<double> d, e;
    for(int i = 0; i < N; i++) d.push_back(a[i]);
    for(int i = 0; i < N; i++) e.push_back(b[i]);
    while(d.size()){
      if(d.front() < e.front()){
        d.pop_front();
        e.pop_back();
      } else {
        v++;
        d.pop_front();
        e.pop_front();
      }
    }
    cout << "Case #" << t << ": " << v << " " << res << '\n';
  }
}
