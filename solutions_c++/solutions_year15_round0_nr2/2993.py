#include <bits/stdc++.h>
#define MAX_N 460
#define HASH 30007
#define MAX_T 1000010
using namespace std;
typedef long long LL;
int A[1100];
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T,N,cas=1;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&N);
        for(int i=0;i<N;i++){
            scanf("%d",&A[i]);
        }

        sort(A,A+N);
        int l=1,r=A[N-1];
        int ans=r;
        while(l<=r){
      //      printf("[%d,%d]\n",l,r);
            int mid=(l+r)/2;
            bool flag=false;
            for(int i=1;i<=mid;i++){
                int res=i;

                for(int j=N-1;j>=0&&A[j]>i;j--){
                    res+=(A[j]+i-1)/i-1;
                  //  if(mid==4)printf("%d:%d\n",i,A[j]);
                }
                if(res<=mid){
                  //  if(mid==4)printf("ans:%d\n",i);
                    flag=true;
                    break;
                }
            }
            if(flag){
                ans=mid;
                r=mid-1;
            }
            else l=mid+1;
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
}
