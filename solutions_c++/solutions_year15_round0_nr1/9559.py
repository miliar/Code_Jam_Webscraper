#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;
int T, n;
char s[1024];
int main()
 {
     freopen("A-large.in","r",stdin);
     freopen("A.out","w",stdout);
     scanf("%d",&T);
     for(int t=1; t<=T; t++){
        scanf("%d %s",&n, s);
        int ans = 0, cnt = s[0]-'0';
        for(int i=1; i<=n; i++){
            int x = s[i]-'0';
            if(!x) continue;
            if(cnt<i) ans+=i-cnt, cnt=i;
            cnt+=x;
        }
        printf("Case #%d: %d\n",t,ans);
     }
     return 0;
 }
