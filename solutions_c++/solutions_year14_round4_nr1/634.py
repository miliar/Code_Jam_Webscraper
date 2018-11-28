#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int TC, n, p[100000], x, ans;
int main(){
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        scanf("%d %d", &n, &x);
        for(int i = 0; i < n; ++i) scanf("%d", &p[i]);
        sort(p, p+n, greater<int>());
        ans = 0;
        //for(int i = 0; i < n; ++i) printf("%d\n", p[i]);
        for(int i = 0, j = n-1; i < n && i <= j; ++i){
            ++ans;
            if(i == j) break;
            //printf("dd %d\n", p[i] + p[j]);
            if(p[i] + p[j] <= x) --j;
        }
        printf("Case #%d: %d\n", tc, ans);
    }
}
