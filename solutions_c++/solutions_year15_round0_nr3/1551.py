#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 200005;
int ca;
int n , a[N];
LL m;
char s[N];

const int multi[5][5] = {
    {0 , 0 , 0 , 0 , 0},
    {0 , 1 , 2 , 3 , 4},
    {0 , 2 ,-1 , 4 ,-3},
    {0 , 3 ,-4 ,-1 , 2},
    {0 , 4 , 3 ,-2 ,-1}
};
int mul(int x , int y) {
    int z = 1;
    if (x < 0) x = -x , z = -z;
    if (y < 0) y = -y , z = -z;
    return multi[x][y] * z;
}

void work() {
    int i , j , k , x , y ;
    scanf("%d%lld%s",&n,&m,s);
    LL len = n * m;
    printf("Case #%d: " , ++ ca);
    x = 1;
    memset(a , 0 , sizeof(a));
    for (i = 0 ; i < n ; ++ i) {
        if (s[i] == 'i') j = 2;
        if (s[i] == 'j') j = 3;
        if (s[i] == 'k') j = 4;
        a[i] = j;
        x = mul(x , j);
    }
    LL p = m;
    y = 1;
    while (p) {
        if (p & 1)
            y = mul(y , x);
        x = mul(x , x) , p >>= 1;
    }
    if (y != -1) {
        puts("NO");
        return;
    }
    int L = -1  , R = -1;
    x = 1;
    for (i = 0 , j = 0; i < len && i < 50000 ; ++ i) {
        x = mul(x , a[j]);
        //cout << x << endl;
        if (x == 2) {
            L = i + 1;
            break;
        }
        j = (j + 1) % n;
    }
    x = 1;
    for (i = 0 , j = n - 1 ; i < len && i < 50000 ; ++ i) {
        x = mul(a[j] , x);
        if (x == 4) {
            R = i + 1;
            break;
        }
        j = (j + n - 1) % n;
    }
    //cout << L << ' ' << R << endl;
    if (~L && ~R && L + R < len)
        puts("YES");
    else
        puts("NO");
}

int main() {
    freopen("1.in" , "r" , stdin);
    freopen("1.out" , "w" , stdout);
    int T;
    scanf("%d" , &T);
    while (T --)
        work();
    return 0;
}
