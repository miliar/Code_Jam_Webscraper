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
template<class T> inline void checkmin(T &a, T b){ if (b<a) a = b; }//NOTES:checkmin( 
template<class T> inline void checkmax(T &a, T b){ if (b>a) a = b; }//NOTES:checkmax( 
#define SIZE(x) ((int)(x).size()) 
#define for0(i,n) for(int i=0;i<(n);i++) 
#define for1(i,n) for(int i=1;i<=(n);i++) 
#define for0r(i,n) for(int i=(n)-1;i>=0;i--) 
#define for1r(i,n) for(int i=(n);i>=1;i--) 
typedef long long ll;

void solve()
{
    int f;
    scanf("%d", &f);
    set<int> S;
    for1(i, 4)for0(j, 4)
    {
        int t;
        scanf("%d", &t);
        if (i == f)S.insert(t);
    }
    int s;
    scanf("%d", &s);
    set<int> S2;
    for1(i, 4)for0(j, 4)
    {
        int t;
        scanf("%d", &t);
        if (i == s)S2.insert(t);
    }
    int ans = 0;
    for (int a : S)
    {
        if (S2.count(a))
        {
            if (ans != 0)
            {
                puts("Bad magician!");
                return;
            }
            ans = a;
        }
    }
    if (ans != 0)printf("%d\n", ans);
    else puts("Volunteer cheated!");
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T, TC = 0;
    scanf("%d", &T);
    while (++TC <= T)
    {
        printf("Case #%d: ", TC);
        solve();
    }
    return 0;
}
