#include <stdio.h>
#include <iostream>
using namespace std;

#define MAXSIZE 1020
void solve()
{
    int s;
    char a[MAXSIZE];
    scanf("%d%s", &s, a);
    int ans = 0;
    int sum = a[0] - '0';
    for(int i=1; i<=s; ++i)
    {
        if(a[i] != '0' && sum < i){
            ans += i - sum;
            sum = i;
        }
        sum += a[i] - '0';
    }
    printf("%d\n", ans);
}
int main()
{
//    freopen("A-large.in", "r", stdin);
//    freopen("data.out", "w", stdout);
    int T;
    int num=0;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++num);
        solve();
    }
}
