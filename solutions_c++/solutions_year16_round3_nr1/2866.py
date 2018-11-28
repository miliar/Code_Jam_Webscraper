#include<bits/stdc++.h>
using namespace std;

typedef __int64 ll;

int n,p[111];

int main() {
   // printf("%c\n",'A'-1);
    freopen("A-small-attempt1 (2).in","r",stdin);
    freopen("test.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++) {
        scanf("%d",&n);
        int tot=0,cnt=n;
        printf("Case #%d:",ca);
        for(int i=0;i<n;i++) scanf("%d",p+i),tot+=p[i];
        while(tot) {
            int t=-1,m=0;
            for(int i=0;i<n;i++) if(p[i]>m) {
                m=p[i];
                t=i;
            }
            printf(" %c",t+'A');
            tot--;
            p[t]--;
            if(tot==2) {
                printf(" ");
                continue;
            }
            t=-1,m=0;
            for(int i=0;i<n;i++) if(p[i]>m) {
                m=p[i];
                t=i;
            }
            printf("%c",t+'A');
            tot--,p[t]--;
        }
        puts("");
    }
    return 0;
}
