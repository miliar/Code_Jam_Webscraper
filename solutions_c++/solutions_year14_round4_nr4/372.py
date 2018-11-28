#include<bits/stdc++.h>
using namespace std;

#define CLR(a,x) memset(a,x,sizeof(a))
#define PB push_back
#define INF 1000000000
#define MOD 1000000007
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define LL long long
#define VI vector < int >
#define PII pair < int , int >

int t, m, n;
string str[16];
int ans[1<<20], assign[1<<20];

int cost(int mask) {
  set < string > S;
  for(int i=0;i<m;i++) {
    if((mask>>i)&1) {
      for(int j=0;j<=(int)str[i].size();j++) {
        S.insert(str[i].substr(0, j));
      }
    }
  }
  return (int)S.size();
}

int main() {
  scanf("%d",&t);
  while(t--) {
    scanf("%d%d",&m,&n);
    for(int i=0;i<m;i++)
      cin>>str[i];
    for(int i=0;i<(1<<m);i++) {
      ans[i] = cost(i);
    }
    int maxi = 0, fre = 1;
    for(int mask=0;mask<(1<<(2*m));mask++) {
      for(int i=0;i<n;i++) {
        assign[i] = 0;
      }
      int flag = 0;
      for(int i=0;i<m;i++) {
        int put = (mask>>(2*i))&3;
        if(put >= n) {
          flag = 1;
          break;
        }
        assign[put] |= (1<<i);
      }
      if(flag == 1) continue;
      int cur = 0;
      for(int i=0;i<n;i++) {
        if(assign[i] == 0) {
          cur = 0;
          break;
        }
        cur += ans[assign[i]];
      }
      if(cur == maxi) {
        fre++;
      } else if(cur > maxi) {
        maxi = cur;
        fre = 1;
      }
    }
    int static kase = 1;
    printf("Case #%d: %d %d\n",kase++, maxi, fre);
  }
  return 0;
}
