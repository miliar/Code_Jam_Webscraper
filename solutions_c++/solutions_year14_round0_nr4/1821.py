#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <vector>

#define FOR(i,a,b) for(int i=a,_b=b;i<=_b;i++)
#define FO(i,a,b) for(int i=a,_b=b;i<_b;i++)
#define FORD(i,a,b) for(int i=a,_b=b;i>=_b;i--)
#define FOD(i,a,b) for(int i=a,_b=b;i>_b;i--)

#define LL long long
#define pi 2*acos(0.0)
using namespace std;

int n;
double a[1001], b[1001];
int c[1001];

void input(){
    scanf("%d", &n);
    FOR (i, 1, n) scanf("%lf", &a[i]);
    FOR (i, 1, n) scanf("%lf", &b[i]);
}

int find_ans1(){
    int ans = 0;
    int j = n;
    FORD (i, n, 1){
        while (j > 0 && a[i] <= b[j]) j--;
        if (j > 0){
            ans++;
            j--;
        }
    }
    return ans;
}

int find_ans2(){
    int ans = n;
    int j = 1;
    FOR (i, 1, n){
        while (j <= n && b[j] <= a[i]) j++;
        if (j <= n){
            ans--;
            j++;
        }
    }
    return ans;
}

void process(){
    sort(&a[1], &a[n+1]);
    sort(&b[1], &b[n+1]);
    printf("%d %d\n", find_ans1(), find_ans2());
}

int main(){
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int test;
    cin>>test;
    FOR (i, 1, test){
        printf("Case #%d: ", i);
        input();
        process();
    }
    return 0;
}

