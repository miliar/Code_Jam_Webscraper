#define _CRT_SECURE_NO_WARNINGS
#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <iostream> 
#include <sstream> 
#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <fstream> 
#include <numeric> 
#include <iomanip> 
#include <bitset> 
#include <list> 
#include <stdexcept> 
#include <functional> 
#include <utility> 
#include <ctime> 
using namespace std;

template<class T> inline void checkmin(T &a, T b){ if (b < a) a = b; }//NOTES:checkmin( 
template<class T> inline void checkmax(T &a, T b){ if (b > a) a = b; }//NOTES:checkmax( 
#define SIZE(x) ((int)(x).size()) 
#define for0(i,n) for(int i=0;i<(n);i++) 
#define for1(i,n) for(int i=1;i<=(n);i++) 
#define for0r(i,n) for(int i=(n)-1;i>=0;i--) 
#define for1r(i,n) for(int i=(n);i>=1;i--) 
typedef long long ll;
typedef pair<int, int> pii;
#define FRsmall(x,y) do{freopen(#x"-small-attempt"#y".in","r",stdin);freopen(#x"-small-attempt"#y".out","w",stdout);}while(0)
#define FRlarge(x) do{freopen(#x"-large.in","r",stdin);freopen(#x"-large.out","w",stdout);}while(0)

int N;
int d[1000000];

bool check(ll mi)
{
    int i = 0;
    for0(j, 3)
    {
        for (ll s = 0; i < N && s + d[i] <= mi; i++)s += d[i];
    }
    return i == N;
}

void solve()
{
    int p, q, r, s;
    scanf("%d %d %d %d %d", &N, &p, &q, &r, &s);
    ll sum = 0;
    q %= r;
    for0(i, N)
    {
        d[i] = q + s;
        q = (p + q) % r;
        sum += d[i];
    }
    ll hi = sum;
    ll lo = 0;
    while (hi > lo)
    {
        ll mi = (hi + lo) / 2;
        if (check(mi))
            hi = mi;
        else
            lo = mi + 1;
    }
    printf("%.15f\n", (double)(sum - hi) / sum);
}

int main()
{
    //freopen("in.txt", "r", stdin);
    //FRsmall(A, 0);
    FRlarge(A);
    int T, TC = 0;
    scanf("%d", &T);
    while (++TC <= T)
    {
        printf("Case #%d: ", TC);
        solve();
    }
    return 0;
}
