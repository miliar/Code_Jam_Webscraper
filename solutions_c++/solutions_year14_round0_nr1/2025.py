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

int r1, a[5][5], r2, b[5][5];

void input(){
    scanf("%d", &r1);
    FOR (i, 1, 4)
        FOR (j, 1, 4) scanf("%d", &a[i][j]);
    scanf("%d", &r2);
    FOR (i, 1, 4)
        FOR (j, 1, 4) scanf("%d", &b[i][j]);
}

void process(){
    int ans = 0;
    int x;
    FOR (i, 1, 4)
        FOR (j, 1, 4)
            if (a[r1][i] == b[r2][j]){
                ans++;
                x = a[r1][i];
            }
    if (ans == 0) printf("Volunteer cheated!");
    else if (ans == 1) printf("%d", x);
    else printf("Bad magician!");
    printf("\n");
}

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int test;
    cin>>test;
    FOR (i, 1, test){
        printf("Case #%d: ", i);
        input();
        process();
    }
    return 0;
}

