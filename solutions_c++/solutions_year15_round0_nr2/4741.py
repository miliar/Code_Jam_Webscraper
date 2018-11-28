#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
using namespace std;

#define N 1100
int a[N];
int n;

inline int getmin(int x, int y) { return x<y?x:y; }

void conduct() {
    scanf("%d", &n);
    for (int i = 0; i<n; ++i) scanf("%d", &a[i]);
    int ans = 1000;
    for (int i = 1; i<=1000; ++i) {
        int tmp = i;
        for (int j = 0; j<n; ++j) tmp += (a[j]-1)/i;
        ans = getmin(ans, tmp);
    }
    printf("%d\n", ans);
}

int main() {
    int time;
    scanf("%d", &time);
    for (int i = 1; i<=time; ++i) {
        printf("Case #%d: ", i);
        conduct();
    }
    return 0;
}
