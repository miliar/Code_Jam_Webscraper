#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 1010;

int T, cas = 0;
int n, a[N], Highest, Ans;

int solve(int H){
    int Sum = 0;
    for(int i = 1; i <= n; i++)
        if (a[i] > H) Sum += a[i]/H + (a[i]%H > 0) - 1;
    return Sum + H;
}

int main(){
    //freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n); Highest = 1;
        for(int i = 1; i<= n; i++)
            scanf("%d", &a[i]), Highest = max(Highest, a[i]);
        Ans = Highest;
        for(int H = 1; H <= Highest; H++)
            Ans = min(Ans, solve(H));
        printf("Case #%d: %d\n", ++cas, Ans);
    }
    return 0;
}
