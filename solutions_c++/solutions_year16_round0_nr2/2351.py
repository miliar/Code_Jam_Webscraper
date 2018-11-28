#include<algorithm>
#include<cstdio>
#include<cmath>
#include<iostream>
#include<string.h>
#include<queue>
using namespace std;
const int N=110;
char s[N]; int A[N];
int main()
{
#ifdef gh546
freopen("b.in","r",stdin);
freopen("b.out","w",stdout);
#endif // gh546
    int TAT; scanf("%d",&TAT);
    for(int cas=1;cas<=TAT;cas++){
        scanf("%s",s+1);
        int n=strlen(s+1);
        for(int i=1;i<=n;i++) A[i]=s[i]=='+'?1:0;
        int bns=1;
//        for(int i=1;i<=n;i++){
//           // printf("%d",A[i]);
//            if(i>=2&&A[i]!=A[i-1]) bns++;
//        }
//        //printf("\n");
//        if(A[n]==1) bns--;
        int R=n,L=1,ans=0;
        for(int i=1;i<=10;i++){
            while(A[R]&&R>0) R--;
            if(R==0) break;
            L=1;
            if(A[L]){
                ans++; while(A[L]&&L<=n){A[L]=0; L++;}
            }
         //   printf("L=%d R=%d\n",L,R);
            reverse(A+1,A+R+1);
            for(int i=1;i<=R;i++) A[i]=1-A[i];
//            for(int i=1;i<=n;i++){
//                printf("%d",A[i]);
//            }
//            printf("\n");
            ans++;
        }
        //if(ans!=bns)
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
