#include <bits/stdc++.h>
using namespace std;
#define REP(i,n) for(int i=0;i<int(n);++i)
#define out(x) cout<<#x"="<<x<<endl
char buf[112345];
map<string, int> dic[3];
int g[(1<<18)+15];
int main(){
    int T;
    scanf("%d",&T);
    REP(tt,T){
        int cnt = 0;
        REP(i,3)dic[i].clear();
        int n;
        scanf("%d ",&n);
        REP(i,n){
            gets(buf);
            char *p=strtok(buf, " ");
            for(; p; p=strtok(NULL, " "))
                dic[min(i,2)][p]|=1<<i;
        }
        for(auto s: dic[1]){
            cnt+=(dic[0].find(s.first)!=dic[0].end());
        }
        int ma = 1<<(n-2);
        memset(g, 0, ma*4+10);
        for(auto s: dic[2]){
            bool f0 = 0, f1 = 0;
            f0 = dic[0].find(s.first)!=dic[0].end();
            f1 = dic[1].find(s.first)!=dic[1].end();
            int msk = s.second >> 2;
            if (f0 && f1) cnt--;
            else {
                REP(st,ma){
                    g[st] += (!f1 && (st&msk)==msk) + (!f0 && (st&msk)==0);
                }
            }
        }
        int ans = dic[2].size();
        REP(st,ma){
            ans=min(ans, int(dic[2].size()-g[st]));
        }
        printf("Case #%d: %d\n", tt+1, cnt+ans);
    }
}
