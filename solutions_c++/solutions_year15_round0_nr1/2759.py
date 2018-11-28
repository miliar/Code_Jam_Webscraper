#include<iostream>
#include<fstream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<numeric>
#include<deque>
using namespace std;
#define LL long long

char s[2000];

int main() {
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  
  int test, no=0;;
  scanf("%d", &test);
  while(test--){
    int n;
    scanf("%d %s", &n, s);
    int m = 0;
    int res = 0;
    for(int i=0;i<=n;++i) {
      int t = s[i] - '0';
      if(t && m < i) {
        res += i - m;
        m = i;
      }
      m += t;
    }
    cout << "Case #"<<++no<<": "<<res<<endl;
  }
}


