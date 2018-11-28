#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define INF (1<<30)
#define F first
#define S second
#define mkp(a, b) make_pair(a, b)

typedef long long llong;
typedef long double ldouble;

#define FOR(I, A, B) for(int (I) = (A); (I) < (B); (I)++)
#define ROF(I, A, B) for(int (I) = (A); (I) >= (B); (I)--)
#define SQR(A) (A)*(A)

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

const char array_sep[] = " ";
const char array_end[] = "";

const char pair_sep[] = " ";
const char pair_end[] = "\n";

const char map_sep[] = "->";
const char map_end[] = "\n";

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};
const int ddx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int ddy[] = {0, 1, 1, 1, 0, -1, -1, -1};

template<typename A> ostream & operator<<(ostream & os, const vector<A> & x)
{
    for(int i = 0; i < x.size(); i++)
        os << x[i] << array_sep;
    os << array_end;
    return os;
}

template<typename A, typename B> ostream & operator<<(ostream & os, const pair<A, B> & x)
{
    os << x.first << pair_sep << x.second << pair_end;
    return os;
}

template<typename A> istream & operator>>(istream & is, vector<A> & x)
{
    for(int i = 0; i < x.size(); i++)
        is >> x[i];
    return is;
}

template<typename A, typename B> istream & operator>>(istream & is, pair<A, B> & x)
{
    is >> x.first >> x.second;
    return is;
}

template<typename _key, typename _val> ostream & operator<<(ostream & os, map<_key, _val> & mp)
{
    for(auto it : mp)   // not for C++98 or earlier
        os << it->F << map_sep << it->S << map_end;
    return os;
}

int sum[10];

void add(llong x)
{
    while(x != 0)
    {
        sum[x % 10]++;
        x /= 10;
    }
}

bool check()
{
    for(int i = 0; i < 10; i++)
        if(!sum[i])
            return false;
    return true;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
//    freopen("errlog.log", "w", stderr);
//   	ios_base::sync_with_stdio(0);

    register int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; test++)
    {
        int n;
        bool f = false;

        scanf("%d", &n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", test);
            continue;
        }

        memset(sum, 0, sizeof sum);

        for(long long i = 1; i <= 100000000; i++)
        {
            llong res = i*n;
//            cerr << i << endl;
            add(res);
            if(check())
            {
                printf("Case #%d: %I64d\n", test, res);
                f = true;
                break;
            }
        }
        if(!f)
            printf("Case #%d: INSOMNIA\n", test);
    }

    return 0;
}
