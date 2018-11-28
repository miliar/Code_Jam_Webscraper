#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
int a[1024*100];
void solve(){
    int n, i, j, x, res=0;
    scanf("%d%d",&n, &x);
    for(i= 0;i<n;i++)
        scanf("%d",a+i);
    std::sort(a,a+n);
    for(j = n-1, i=0; j >=i; j--){
        if(a[j]+a[i] <= x)
            res++, i++;
        else
            res++;
    }
    printf("%d\n", res);
}
int main(void){
#ifdef _DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
