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

#define pb push_back
#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))

int MMAX[10]={0,10,100,1000,10000};

string sa,sb;
int n;

bool valid(string& s1, string& s2) {
  FORZ(i,n) {
    if (sa[i]!='?'&&s1[i]!=sa[i]) return false;
    if (sb[i]!='?'&&s2[i]!=sb[i]) return false;
  }
  return true;
}

void solve() {
  cin>>sa>>sb;
  n=(int)sa.length();
  int gap=99999;
  int ca,cb;
  string ta(n,'0'),tb(n,'0');
  FORZ(i,MMAX[n]) {
    int tmpi=i;
    FORZ(k,n) {
      ta[n-k-1]=tmpi%10+'0';
      tmpi/=10;
    }
    FORZ(j,MMAX[n]) {
      int tmpj=j;
      FORZ(k,n) {
        tb[n-k-1]=tmpj%10+'0';
        tmpj/=10;
      }
      if (valid(ta,tb)) {
        if (gap>abs(i-j)) {
          gap=abs(i-j);
          ca=i;
          cb=j;
        } else if (gap==abs(i-j)) {
          if (ca>i) {
            ca=i;cb=j;
          } else if (ca==i && cb>j) {
            ca=i;cb=j;
          }
        }
      }
    }
  }
  string ra(n,'0'),rb(n,'0');
  FORZ(k,n) {
    ra[n-k-1]=ca%10+'0';
    ca/=10;
    rb[n-k-1]=cb%10+'0';
    cb/=10;
  }
  cout<<ra<<" "<<rb<<"\n";
}

int main() {
#ifdef DEBUG
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d: ", i);
    solve();
  }
  
  return 0;
}
