#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
std::pair<int, int> pa[1024*100];
int a[1024*100];
int getres(int*a, int n){
    if( n <= 2)
        return 0;
    int mini = 0, i;
    for(i = 0; i < n; i++)
        if(a[i] < a[mini])
            mini = i;
    i = mini;
    int res = i < n-i-1 ? i : n-i-1;
    while(i){
        std::swap(a[i], a[i-1]);
        i--;
    }

    return res+getres(a+1, n-1);
}
void solve(){
    int n, i;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d", a+i);
    }
    printf("%d\n", getres(a, n));
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
