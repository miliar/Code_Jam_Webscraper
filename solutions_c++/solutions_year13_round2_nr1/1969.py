#include<cstdio>
#include<algorithm>
#define LL long long
#define N 105
using namespace std;
LL T, a, n;
LL sumaa[N], sumct[N]; 
int main(){
    freopen("GCJ_1B_Alarge.in","r",stdin);
    freopen("GCJ_1B_Alarge.out","w",stdout);
    scanf("%I64d",&T);
    for (LL i = 0; i < T; i++){
        scanf("%I64d%I64d",&a,&n);
        LL s[N], ans =n;
        for (LL j = 0; j < n; j++)
            scanf("%I64d",&s[j]);
     if (a > 1){
        sort(s,s+n);
        for (LL j = 0; j < n; j++){
            LL ct, aa;
            if (j == 0){
               ct = sumct[0] = 0;
               aa = sumaa[0] = a;
            }
            else {
                 ct = sumct[j-1];
                 aa = sumaa[j-1];
            }
            if (aa > s[j]) aa+= s[j];
            else {
                 aa += (aa-1); ct++;
                 while (aa<=s[j]){
                       aa+=(aa-1);
                       ct++;
                 }
                 aa += s[j];
            }
            ct += (n-j-1);
            ans = min(ans,ct);
            
            sumct[j] = ct-(n-j-1);
            sumaa[j] = aa;
        }
     }
     else ans = n;
        printf("Case #%I64d: %I64d\n", i+1, ans);
        
    }
    scanf("\n");
    return 0;
}
