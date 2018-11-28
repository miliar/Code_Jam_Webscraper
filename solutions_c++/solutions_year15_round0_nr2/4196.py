#include<cstdio>
#include<algorithm>
using namespace std;
const int MAX = 1000 + 10;
int rec[MAX];
int main(){
    freopen("b.in" ,"r", stdin);
    freopen("b.out", "w", stdout);
    int TN;
    scanf("%d", &TN);
    for(int casen = 1 ; casen <= TN ; casen++){
        int n;
        scanf("%d", &n);
        for(int i = 0 ; i < n ; i++){
            scanf("%d", &rec[i]);
        }
        sort(rec, rec+n);
        int ans = rec[n-1];
        for(int i = 1 ; i <= ans ; i++){
            int sum = i;
            for(int j = n-1 ; j >= 0 ; j--){
                if(rec[j] <= i) break;
                sum += (rec[j]-1) / i;
            }
            ans = min(ans, sum);
        }
        printf("Case #%d: %d\n", casen, ans);
    }
    return 0;
}
