#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
#define F first
#define S second
using namespace std;
int T;
int main(void){
  cin >> T;
  for(int t = 1; t <= T; t++){
    int n;
    priority_queue<pair<int,pair<int,int> > > que;
    cin >> n;
    for(int i = 0; i < n; i++){
      int a;
      cin >> a;
      que.push( make_pair(a, make_pair(a,1) ) );
    }
    int best = que.top().F;
    int c = 0;

    while(que.top().F > 1){
      pair<int,pair<int,int> > p = que.top();
      que.pop();
      c++;
      p.S.S++;
      p.F = p.S.F/p.S.S + ((p.S.F%p.S.S)?1:0);
      que.push(p);
      best = min(best,que.top().F + c);
    }
    cout << "Case #" << t << ": " << best << endl;
  }
}
