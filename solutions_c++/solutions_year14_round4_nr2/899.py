#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int t, n, a[1000], b[1000];
int ans;
void dfs(int x, int l, int r, int cur){
    //printf("dfs: %d %d %d %d\n", x, l, r, cur);
    if(cur>=ans)    return;
    if(x==n){
        ans = min(ans, cur);
        return;
    }
    int id;
    for(int i=l; i<=r; i++){
        if(a[i]==b[x]){
            id=i;
            break;
        }
    }
    int res=0;
    for(int i=id; i>l; i--){
        swap(a[i], a[i-1]);
        res++;
    }
    dfs(x+1, l+1, r, cur+res);
    for(int i=l; i<id; i++){
        swap(a[i], a[i+1]);
    }
    res=0;
    for(int i=id; i<r; i++){
        swap(a[i], a[i+1]);
        res++;
    }
    dfs(x+1, l, r-1, cur+res);
    for(int i=r; i>id; i--){
        swap(a[i], a[i-1]);
    }
}
int main(){
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    scanf("%d", &t);
    for(int ct=1; ct<=t; ct++){
        scanf("%d", &n);
        for(int i=0; i<n; i++){
            scanf("%d", a+i);
            b[i]=a[i];
        }
        sort(b, b+n);
        ans = 0x7fffffff;
        dfs(0, 0, n-1, 0);
        printf("Case #%d: %d\n", ct, ans);
    }
    return 0;
}
