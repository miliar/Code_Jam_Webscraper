#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <queue>
#define FI first
#define SE second
using namespace std;
const double EPS = 1e-8;
const int MAXN = 100005;
int main()
{
    freopen("/home/qitaishui/practice/retired/in.txt","r",stdin);
    freopen("/home/qitaishui/practice/retired/out.txt","w",stdout);
    int cas;
    int tmp,n,m,a[4],b[4],ans,cnt;
    scanf("%d",&cas);
    for (int ca = 1; ca <= cas; ++ca) {
        scanf("%d",&n);
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d",&tmp);
                if (i+1 == n) a[j] = tmp;
            }
        }
        scanf("%d",&n);
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d",&tmp);
                if (i+1 == n) b[j] = tmp;
            }
        }
        cnt = 0;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (a[i] == b[j]) {
                    ++cnt;
                    ans = a[i];
                }
            }
        }
        printf("Case #%d: ",ca);
        if (cnt == 1) printf("%d\n",ans);
        else if (cnt == 0)
            printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    return 0;
}
