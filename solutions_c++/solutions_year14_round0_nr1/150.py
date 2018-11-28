#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <set>
using namespace std;
typedef long long LL;
int ca;
#define N 5005
int a[16];
void work()
{
    printf("Case #%d: " , ++ ca);
    set<int> H;
    int i , x , ans , cnt = 0;
    scanf("%d",&x) , -- x;
    for (i = 0 ; i < 16 ; ++ i)
        scanf("%d",&a[i]);
    for (i = x << 2 ; i < x + 1 << 2 ; ++ i)
        H.insert(a[i]);
    scanf("%d",&x) , -- x;
    for (i = 0 ; i < 16 ; ++ i)
        scanf("%d",&a[i]);
    for (i = x << 2 ; i < x + 1 << 2 ; ++ i) {
        if (H.count(a[i])) {
            ans = a[i];
            ++ cnt;
        }
    }
    if (cnt == 1) {
        printf("%d\n" , ans);
    } else if (!cnt) {
        puts("Volunteer cheated!");
    } else {
        puts("Bad magician!");
    }
}

int main (){
    freopen("1.txt" , "r" , stdin);
    freopen("2.txt" , "w" , stdout);

    int T;
    scanf("%d",&T);
    while (T --) {
        work();
    }
    return 0;
}
