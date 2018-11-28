#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int TC, n, p[10000], pr[1001], ans, fwl[10001], fwr[10001];
bool cmp(int a, int b){
    return p[a] < p[b];
}
int smin(int a, int b){
    if(a == -1) return b;
    if(b == -1) return a;
    return min(a, b);
}
int main(){
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        scanf("%d", &n);
        for(int i = 0; i < n; ++i) scanf("%d", &p[i]);
        for(int i = 0; i < n; ++i) pr[i] = i;
        sort(pr, pr+n, cmp);
        ans = 0;
        for(int i = 0; i < n; ++i){
            int a = 0, b = 0;
            for(int j = 0; j < pr[i]; ++j) if(p[j] > p[pr[i]]) ++a;
            for(int j = n-1; j > pr[i]; --j) if(p[j] > p[pr[i]]) ++b;
            ans += min(a, b);
        }
        printf("Case #%d: %d\n", tc, ans);
    }
    //system("pause");
}
