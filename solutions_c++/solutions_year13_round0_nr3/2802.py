#include <vector>
#include <iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string.h>
#include<queue>
#include <set>
#include<map>
#include<string>
#include<stdexcept>
#include<errno.h>

using namespace std;
template <class T> void show(T a, int n) { for (int i = 0; i < n; ++i) cout << a[i] << ' '; cout << endl; }
template <class T> void show(T a, int r, int l) { for (int i = 0; i < r; ++i) show(a[i], l); cout << endl; }
#define max(a, b) (a > b?a:b)
#define min(a, b) (a < b?a:b)

#define ms(a, v)    memset(a, v, sizeof(a))
#define pb push_back
#define mp make_pair
#define pii pair<int, int>

typedef long long LL;

const int N = 128 * 2;
const int M = 5000;
const int oo = 10000 * 10000 * 10;

long long n, m;

bool is_palin(long long a)
{
    vector<int> e;
    while(a)
    {
        e.push_back(a%10);
        a /= 10;
    }
    for (int i = 0, j = e.size() - 1;i < j;++i,--j)
        if (e[i] != e[j])
            return false;
    return true;
}

int main()
{
        freopen("in", "r", stdin);
        freopen("out1","w",stdout); 
    int i, j, cas = 0;
    cin >> cas;
    for (int cc = 0; cc < cas;++cc)
    {
        //printf("Case #%d: ", cc + 1);
        cout << "Case #" << cc + 1 << ": ";
        cin >> n >> m;
        long long ans = 0;

        for (long long i = 1; i * i <= m;++i)
        {
            if ( i * i >= n && is_palin(i) && is_palin(i*i))
                ++ans;
        }
        cout << ans << endl;

    }
    return 0;
}

