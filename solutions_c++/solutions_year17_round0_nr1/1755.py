#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#define fi first
#define se second
using namespace std;
typedef long long LL;
const int MOD = 1e9+7;
const int maxn = 1e3+10;

int a[maxn];
int f[maxn];
int n;
int computeM(int k){
  memset(f,0,sizeof(f));
  int sum = 0;
  int ans =0;
  for(int i=0 ; i+k<=n ; ++i){
    if((sum+a[i])&1){
      f[i] = 1;ans++;
    }
    sum+=f[i];
    if(i-k+1>=0)sum-=f[i-k+1];
  }
  for(int i = n-k+1 ; i<n ; ++i)
  {
    if((sum+a[i])&1)return -1;
    if(i-k+1>=0)sum-=f[i-k+1];
  }
  return ans;
}
char s[maxn];

int main() {
    int T;
    cin>>T;
    int k;
    int kase =0;
    while(T--){
        scanf("%s%d",s,&k);
        n = strlen(s);
        for(int i=0 ; i<n ; ++i)
            a[i]=(s[i]=='-');
        int step = computeM(k);
        printf("Case #%d: ",++kase );
        if(step == -1){
            printf("IMPOSSIBLE\n");
        }else std::cout << step << '\n';
    }

  return 0;
}
