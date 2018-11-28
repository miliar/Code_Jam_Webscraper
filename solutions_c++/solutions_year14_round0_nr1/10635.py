#include<iostream>
#include<cstdio>
#include<string.h> 
using namespace std;

int T,a,b,flag[20],x;

int main() {
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++) {
        scanf("%d",&a);
        memset(flag,0,sizeof(flag));
        for (int i=1;i<=4;i++) 
            for (int j=1;j<=4;j++) {
                scanf("%d",&x);
                if (i==a) flag[x]++;
            }
        scanf("%d",&b);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++) {
                scanf("%d",&x);
                if (i==b) flag[x]++;
            }
        int ans=-1;
        for (int i=1;i<=16;i++)
            if (flag[i]==2){
               if (ans==-1) ans=i;
               else ans=17;
            }
        printf("Case #%d: ",cas);
        if (ans==-1) printf("Volunteer cheated!\n");
        else if (ans==17) printf("Bad magician!\n");
        else printf("%d\n",ans);
    }
    return 0;
} 
