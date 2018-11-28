#include<bits/stdc++.h>
using namespace std;

int main() {
  freopen("g.in","r",stdin);
  freopen("g.out","w",stdout);
  int tt;
  scanf("%d",&tt);
  int cases=1;
  while(tt--) {
    int n;
    scanf("%d",&n);
    string s;
    cin>>s;
    int res=s[0]-'0';
    int cnt=0;
    for(int i=1;i<=n;i++) {
      if(res>i) {
        res+=s[i]-'0';
      } else {
        cnt+=(i-res);
        res+=s[i]-'0'+(i-res);
      }
    }
    printf("Case #%d: %d\012",cases++,cnt);
  }
  return 0;
}
