//my magic will tear you apart!
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdlib>
using namespace std;
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
typedef long long ll;
const int N = 10000;
int tc;
int n,r,p,s, a[3][N], cnt[3][3], b[3];
string str = "PSR";

void srt(string &q) {
  for(int i = 1;  i <= n; i++) {
    for(int j = 0; j < (1 << n); j += (1 << i)) {
      if(q.substr(j, (1 << (i-1))) > q.substr(j + (1 << (i-1)), (1 << (i-1)))) {
        
        for(int k = j; k < j + (1 << (i-1)); k++) {
          char tmp = q[k];
          q[k] = q[k+(1 << (i-1))];
          q[k+(1 << (i-1))] = tmp;
        }
        
      }
      
    }
  }
}
int main() {
  if(fopen("A.in","r")) freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  cin >> tc;
  for(int test = 1; test <= tc; test++) {
    printf("Case #%d: ", test);
    scanf("%d %d %d %d\n", &n, b+2, b , b + 1);
    bool done = 0;
    memset(a,0,sizeof(a));
    memset(cnt,0,sizeof(cnt));
    for(int i = 0; i < 3 && !done ; i++) {
      a[i][1] = i;
      for(int j = 1; j < (1 << n); j++) {
        if(a[i][j] == 0) {
          a[i][2*j] = 0;
          a[i][2*j + 1] = 2;
        } else if (a[i][j] == 1) {
          a[i][2*j] = 0;
          a[i][2*j + 1] = 1;
        } else {
          a[i][2*j] = 1;
          a[i][2*j + 1] = 2;
        }
      }
      for(int j = (1 << n); j < (1 << (n+1)); j++) {
        cnt[i][a[i][j]]++;
      }

      if(cnt[i][0] == b[0] && cnt[i][1] == b[1] && cnt[i][2] == b[2]) {
        string dum;
        for(int j = (1 << n); j < (1 << (n+1)); j++) {
          dum += str[a[i][j]];
        }
        srt(dum);
        cout << dum;
        cout << "\n";
        done = 1; 
      }

    }
    if(!done)
      cout << "IMPOSSIBLE\n";
  }
  return 0;
}