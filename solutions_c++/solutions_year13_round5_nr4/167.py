#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
typedef long long ll;
typedef double du;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)
const int MAXN = 20;

char s[MAXN+1];
du f[MAXN+1][1<<MAXN];
int n;

int shuffle(int k){
    return (k>>1)|((k&1)<<(n-1));
}

int minimize(int k){
    int ret = k;
    int i = k;
    do{
        i = shuffle(i);
        ret = min(ret, i);
    }while(i != k);
    return ret;
}

du get(int k){
    k = minimize(k);
    if(f[n][k] >= -1e-10)
        return f[n][k];
    //cout<<k<<endl;
    int i, j;
    du ret = 0.;
    for(i = 0; i < n; i++, k = shuffle(k)){
        j = 0;
        while(1<<j&k)
            j++;
        ret += get(k|1<<j)+(n-j);
    }
    return f[n][k] = ret/n;
}

int main()
{
    #ifdef __FIO
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D.txt", "w", stdout);
    #endif
    int T, i0;
    cout<<fixed<<setprecision(14);
    for(int i = 0; i <= MAXN; i++)
        for(int j = 0; j < (1<<MAXN); j++)
            f[i][j] = -1;
    for(int i = 0; i <= MAXN; i++)
        f[i][(1<<i)-1] = 0;
    scanf("%d", &T);
    for(i0 = 1; i0 <= T; i0++){
        printf("Case #%d: ", i0);
        int i, j, k;
        scanf("%s", s);
        n = strlen(s);
        k = 0;
        for(i = 0; i < n; i++)
            if(s[i] == 'X')
                k |= 1<<i;
        cout<<get(k)<<endl;
    }
    return 0;
}
