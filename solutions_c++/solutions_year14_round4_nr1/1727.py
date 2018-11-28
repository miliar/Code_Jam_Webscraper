#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef vector<long long> vll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define mset(arr,val)  memset(arr,val,sizeof(arr))
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define forr(var,from,to) for(int var=(from);var<=(to);var++) 
#define found(s,e)  ((s).find(e)!=(s).end())
#define remove_(c,val) (c).erase(remove((c).begin(),(c).end(),(val)),(c).end())
#define lastc(str) (*((str).end()-1))

// #include "cout.h"

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
    int N, X; cin >> N >> X;
    vector<int> s(N);
    rep(n,N) cin >> s[n];
    sort(all(s)); reverse(all(s));

    //cout << N << " " << X << s << endl;
    priority_queue<int> pq;

    int cnt = 0;
    rep(i,N){
      int si = s[i];
      //printf("%d) %d\n", i, si);
      if (!pq.empty()) {
        int t = pq.top();
        //printf("top = %d; ", t);
        if (si <= t) {
          pq.pop();
          //printf("pop\n");
        } else {
          // waste
          pq.push(X - si);
          //printf("push %d - %d\n", X, si);
          ++cnt;
        }
      } else {
        pq.push(X - si);
        //printf("push %d - %d\n", X, si);
        ++cnt;
      }
    }

 answer:
    cout << "Case #" << (1+_t) << ": " << cnt << endl;
  }
}
