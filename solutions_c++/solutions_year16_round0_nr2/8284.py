#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<cmath>
#include<vector>
using namespace std;
#define PB push_back
#define PPB pop_back
#define MP make_pair
#define LL long long
#define fs first
#define sc second
#define pii pair<int,int>
#define pll pair<LL,LL>
#define ppii pair<int, pii>
#define BIG 2000000000

const int N = 105;
int tc,pjg,cnt;
char st,cur,s[N];

int main() {
  scanf("%d",&tc);
  for (int z=1;z<=tc;++z) {
    scanf("%s",s);
    pjg = strlen(s);
    st = cur = s[0];
    cnt = 1;
    for (int i=1;i<pjg;++i) {
      if (s[i] != cur) {
        ++cnt;
        cur = s[i];
      }
    }
    
    printf("Case #%d: ",z);
    if (st == '+') {
      printf("%d\n",(cnt%2)?--cnt:cnt);
    } else {
      printf("%d\n",(cnt%2)?cnt:--cnt);
    }
  }
	return 0;
}
