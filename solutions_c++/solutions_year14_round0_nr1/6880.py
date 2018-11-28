#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <iostream>
#include <set>
#include <queue>
#define zero(x) (((x)>0?(x):-(x))<eps)
#define mem(a,b) memset((a),(b),sizeof((a)))
#define lld long long
#define INF 0x3f3f3f3f
#define eps 1e-6
#define num_char 26
#define hash(x) ((x)-'a')
#define N 100009

using namespace std;

int num1[9][9], num2[9][9];
int n, m;

int MAIN() {
    scanf("%d", &n);
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            scanf("%d", &num1[i][j]);
        }
    }
    scanf("%d", &m);
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            scanf("%d", &num2[i][j]);
        }
    }
    n--;
    m--;
    int cnt = 0;
    int ans;
    for(int i = 0; i < 4; i++) {
        int ok = 0;
        for(int j = 0; j < 4; j++) {
            if(num2[m][j] == num1[n][i]) ok = 1;
        }
        cnt += ok;
        if(ok) ans = num1[n][i];
    }
    if(cnt == 1) {
        printf("%d\n", ans);
    } else if(cnt == 0) {
        printf("Volunteer cheated!\n");
    } else {
        printf("Bad magician!\n");
    }
    return 0;
}


int main() {
#ifdef LOCAL_TEST
    freopen("F:/ACMData.txt","r",stdin);
    freopen("F:/out.txt","w",stdout);
#endif
    int cases;
    scanf("%d", &cases);
    int cc = 1;
    while(cases--) {
        printf("Case #%d: ", cc++);
        MAIN();
    }
    return 0;
}

