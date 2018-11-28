#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <cstring>
#include <string>
using namespace std;

typedef pair<int,int> pairii;
typedef long long llong;

//#define TESTING
#define pb push_back
#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

int n,j;
string s;
llong buf[11]={0,0,3,2,3,2,7,2,3,2,3};

bool check(llong b) {
  llong x=0,base=1;
  FORZ(i,n) {
    x=(x+base*(llong)(s[n-1-i]-'0'))%buf[b];
    base=(b*base)%buf[b];
  }
  return x%buf[b]==0;
}

void solve() {
  cin>>n>>j;
  s="1";
  FORZ(i,n-2) s.pb('0');
  s.pb('1');
  int cnt=0;
  while (cnt<j) {
    bool good=true;
    FOR(i,2,11) if (!check(i)) {
      good=false;
      break;
    }
    if (good) {
      cnt++;
      cout<<s<<" ";
      FOR(i,2,11) {
        cout<<buf[i]<<" ";
#ifdef TESTING
        llong x=0,base=1;
        FORZ(k,n) {
          x+=base*(llong)(s[n-1-k]-'0');
          base*=(llong)i;
        }
        if (x%buf[i]==0) cout<<"good ";
        else  cout<<"xxxx ";
#endif
      }
      cout<<"\n";
    }
    int i=n-2;
    while (true) {
      s[i]++;
      if (s[i]=='2') {
        s[i]='0';
        i--;
        continue;
      }
      break;
    }
  }
}

int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d:\n", i);
    solve();
  }
  
  return 0;
}
