#include <cstdio>
const int N = 1111;
int a[N];
int main(){
    freopen("inbig.txt","r",stdin);
    freopen("2.txt","w",stdout);
    int t;
    int nCase = 0;
    for (scanf("%d",&t);t;t--){
        int n;
        scanf("%d",&n);
        for (int i=0;i<n;i++) scanf("%d",&a[i]);
        int ans = 1000;
        for (int j=1;j<=1000;j++){
            int sum = 0;
            for (int i=0;i<n;i++) sum += (a[i]-1)/j;
            if (sum+j<ans) ans = sum + j;
        }
        printf("Case #%d: %d\n",++nCase,ans);
    }
    return 0;
}
