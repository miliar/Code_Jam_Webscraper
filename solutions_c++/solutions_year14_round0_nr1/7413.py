/*
 * Author:  chlxyd
 * Created Time:  2014-4-12 21:03:11
 * File Name: A.cpp
 */
#include<iostream>
#include<sstream>
#include<fstream>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>
#include<ctime>
using namespace std;
const double eps(1e-8);
typedef long long lint;
#define clr(x) memset( x , 0 , sizeof(x) )
#define sz(v) ((int)(v).size())
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define repf(i, a, b) for (int i = (a); i <= (b); ++i)
#define repd(i, a, b) for (int i = (a); i >= (b); --i)
#define clrs( x , y ) memset( x , y , sizeof(x) )

int a[5][5], b[5][5];
int v[20], n;

int main(){
    freopen("A.out", "w", stdout);
    int T, ca = 1;
    scanf("%d", &T);
    while (T--) {
        clr(v);
        scanf("%d", &n);
        n--;
        rep (i, 4) {
            rep (j, 4) {
                int x;
                scanf("%d", &x);
                if (i == n) 
                    v[x] = 1; 
            }
        }
        int ans = 0, ans2 = 0;
        scanf("%d", &n);
        n--;
        rep (i, 4)
            rep (j, 4) {
                int x;
                scanf("%d", &x);
                if (i == n) {
                    if (v[x]) {
                        ans++;
                        ans2 = x;
                    }
                }
            }
        printf("Case #%d: ", ca++);
        if (ans == 0) printf("Volunteer cheated!\n");
        else if (ans == 1) printf("%d\n", ans2);
        else printf("Bad magician!\n");
    }
    return 0;
}

