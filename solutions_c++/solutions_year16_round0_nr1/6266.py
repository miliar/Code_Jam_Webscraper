#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int A[10];
int ans[1000010];
int main(){
    freopen("Alarge.in","r",stdin);
    freopen("ALout.out","w",stdout);
    int T;
    ans[0] = -1;
    for(int i=1;i<=1000000;i++) {
        memset(A,0,sizeof(A));
        int sum = 0;
        ans[i] = -1;
        for(int j=1;j<=1000;j++) {
            int k = i*j;
            while(k > 0) {
                if(A[k%10] == 0){
                    sum++;
                    A[k%10]++;
                }k /= 10;
            }
            if(sum == 10) {
                ans[i] = j;
                break;
            }
        }
        //if(ans[i] == -1) printf("%d : %d\n",i, ans[i]);
    }
    scanf("%d",&T);
    for(int tt = 1;tt <= T;tt++) {
        int a;
        scanf("%d",&a);
        printf("Case #%d: ",tt);
        if(ans[a] == -1) printf("INSOMNIA\n");
        else printf("%d\n",ans[a] * a);
    }
    return 0;
}
