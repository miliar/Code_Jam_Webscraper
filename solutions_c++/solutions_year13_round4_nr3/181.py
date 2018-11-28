#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <stack>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define for1(i, n) for (int i = 1; i <= (int)(n); i++)
#define forv(i, v) forn(i, v.size())

typedef pair<int, int> pii;
typedef long long ll;

#define lf(v) (v << 1)
#define rg(v) ((v << 1) + 1)

#define NMAX 2005
int n;
bool g[NMAX][NMAX];
int din[NMAX];
bool used[NMAX];
int a[NMAX], b[NMAX], x[NMAX];
int da[NMAX], db[NMAX];

void calc_d()
{    
    forn(i, n)
    {
        da[i] = 1;
        forn(j, i) if (x[j] < x[i] && x[j] != -1) da[i] = max(da[i], da[j] + 1);
    }
    for (int i = n - 1; i >= 0; i--)
    {
        db[i] = 1;
        for (int j = i + 1; j < n; j++) if (x[j] < x[i] && x[j] != -1) db[i] = max(db[i], db[j] + 1);
    }
}

int t1[NMAX * 4], t2[NMAX * 4];
int tsize;

void update(int* t, int i, int val)
{
    i += tsize;
    t[i] = val;
    i >>= 1;
    while (i)
    {
        t[i] = max(t[lf(i)], t[rg(i)]);
        i >>= 1;
    }    
}

int rmq(int* t, int l, int r)
{
    int ret = 0;
    l += tsize;
    r += tsize;
    while (l <= r)
    {
        if (l & 1)
        {
            ret = max(ret, t[l]);
            l++;
        }
        if (!(r & 1))
        {
            ret = max(ret, t[r]);
            r--;
        }
        r >>= 1;
        l >>= 1;
    }
    return ret;      
}

void calc_d2()
{    
    tsize = 1;
    while (tsize < n) tsize *= 2;
    forn(i, 2 * tsize) t1[i] = t2[i] = 0;

    //cerr << "X:\n";
    //forn(i, n) cerr << x[i] << " ";
    //cerr << endl;

    forn(i, n)
    {
        if (x[i] == -1) continue;
        da[i] = 1 + rmq(t1, 0, x[i] - 1);
        update(t1, x[i], da[i]);
        //da[i] = 1;
        //forn(j, i) if (x[j] < x[i] && x[j] != -1) da[i] = max(da[i], da[j] + 1);
    }

    for (int i = n - 1; i >= 0; i--)
    {
        if (x[i] == -1) continue;
        db[i] = 1 + rmq(t2, 0, x[i] - 1);
        update(t2, x[i], db[i]);
        //db[i] = 1;
        //for (int j = i + 1; j < n; j++) if (x[j] < x[i] && x[j] != -1) db[i] = max(db[i], db[j] + 1);
    }

    //forn(i, n) cerr << da[i] << " ";
    //cerr << endl;

    //forn(i, n) cerr << db[i] << " ";
    //cerr << endl;
}



bool check()
{
    calc_d2();
    forn(i, n) if (a[i] != da[i]) return false;
    forn(i, n) if (b[i] != db[i]) return false;
    return true;
}

bool rec(int k)
{
    if (k == n) return true;
    vector<int> pos;
        calc_d2();
        forn(i, n)
        {
            if (x[i] != -1) continue;

            int ca = 1, cb = 1;
            forn(j, i) if (x[j] != -1) ca = max(ca, da[j] + 1);
            for (int j = i + 1; j < n; j++) if (x[j] != -1) cb = max(cb, db[j] + 1);

            while (i < n && x[i] == -1)
            {
                if (ca > a[i] || cb > b[i]) return false;
                if (ca == a[i] && cb == b[i])
                {
                    pos.pb(i);
                }
                i++;
            }

            i--;
        }

    forv(i, pos)
    {
        x[pos[i]] = k;
        if (rec(k + 1)) return true;
        x[pos[i]] = -1;
    }
        
    return false;    
}

void find_perm()
{
    forn(i, n) x[i] = -1;
    forn(i, n)
    {
        if (a[i] == 1 && b[i] == 1)
        {
            x[i] = 0;
        }
    }

    assert(rec(1));

    /*
    for (int k = 1; k < n; k++)
    {
        calc_d();
        bool ok = false;
        forn(i, n)
        {
            if (x[i] != -1) continue;

            int ca = 1, cb = 1;
            forn(j, i) if (x[j] != -1) ca = max(ca, da[j] + 1);
            for (int j = i + 1; j < n; j++) if (x[j] != -1) cb = max(cb, db[j] + 1);

            if (ca == a[i] && cb == b[i])
            {
                ok = true;
                x[i] = k;
                break;    
            }
        }  
        if (!ok)
        {
            forn(i, n) cerr << a[i] << " ";
            cerr << endl;
            forn(i, n) cerr << b[i] << " ";
            cerr << endl;
            forn(i, n) cerr << x[i] << " ";
            cerr << endl;
            assert(false);
        }
    }
    */
}

void solve(int tc)
{
    cerr << tc << endl;
    printf("Case #%d:", tc);
    cin >> n;
    forn(i, n) cin >> a[i];
    forn(i, n) cin >> b[i];
    find_perm();  
    assert(check());
    forn(i, n) cout << " " << x[i] + 1;
    cout << endl;
}

void test(int n)
{    
    ::n = n;
    int p[NMAX];
    forn(i, n) x[i] = i;
    random_shuffle(x, x + n);
    forn(i, n) p[i] = x[i];
    //forn(i, n) cerr << p[i] << " ";
    //cerr << endl;
    calc_d();
    forn(i, n) a[i] = da[i];
    forn(i, n) b[i] = db[i];
    find_perm();
    if (!check())
    {
        forn(i, n) cerr << p[i] << " ";
        cerr << endl;            
        forn(i, n) cerr << a[i] << " ";
        cerr << endl;            
        forn(i, n) cerr << b[i] << " ";
        cerr << endl;
        assert(false);     
    }    
}
                   
int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tc;
    cin >> tc;
    
    /*
    forn(it, tc)
    {
        cerr << it << endl;
        test(2000);
        cerr << clock() << endl;
    }
    */
    
    
    forn(it, tc) solve(it + 1);
    return 0;
}
