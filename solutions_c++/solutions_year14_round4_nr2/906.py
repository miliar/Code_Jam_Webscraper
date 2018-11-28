#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define all(o) (o).begin(), (o).end()
#define allr(o) (o).rbegin(), (o).rend()
const int INF = 2147483647;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> int size(T &x) { return x.size(); }

// assert or gtfo

int n;
vector<ii> arr;

struct fenwick_tree {
    int n; vi data;
    fenwick_tree(int _n) : n(_n), data(vi(n)) { }
    void update(int at, int by) {
        while (at < n) data[at] += by, at |= at + 1; }
    int query(int at) {
        int rez = 0;
        while (at >= 0) rez += data[at], at = (at & (at + 1)) - 1;
        return rez; }
    int rsq(int a, int b) { return query(b) - query(a - 1); }
};

int inversions(const vi &A, int l, int r, bool asc)
{
    fenwick_tree ft(n);

    int cnt = 0;
    for (int i = l; i <= r; i++)
    {
        if (asc)
            cnt += ft.rsq(A[i], n-1);
        else
            cnt += ft.query(A[i]);

        ft.update(A[i], 1);
    }

    return cnt;
}

int main()
{
    int ts;
    scanf("%d\n", &ts);

    for (int t = 0; t < ts; t++)
    {
        printf("Case #%d: ", t+1);

        scanf("%d\n", &n);

        arr = vector<ii>(n);
        vi orig(n);
        for (int i = 0; i < n; i++)
        {
            int x;
            scanf("%d", &x);
            arr[i] = ii(x, i);
        }

        sort(all(arr));

        for (int i = 0; i < n; i++)
            orig[arr[i].second] = i;

        int mn = INF;

        do
        {
            bool up = true;
            bool ok = true;

            for (int i = 1; i < n; i++)
            {
                if (arr[i-1].first < arr[i].first)
                {
                    if (!up)
                    {
                        ok = false;
                        break;
                    }
                }
                else
                {
                    if (up)
                    {
                        up = false;
                    }
                }
            }

            if (ok)
            {
                vii tmp(n);
                for (int i = 0; i < n; i++)
                {
                    tmp[i].first = arr[i].second;
                    // tmp[i].second = orig[i];
                    tmp[i].second = i;
                }

                sort(all(tmp));

                vi bla(n);
                for (int i = 0; i < n; i++)
                    bla[i] = tmp[i].second;

                int cur = 0;
                cur = inversions(bla, 0, n - 1, true);

                // for (int i = 0; i < n; i++)
                // {
                //     cur += abs(i - arr[i].second);
                // }

                mn = min(mn, cur);
            }

        } while (next_permutation(all(arr)));

        cout << mn << endl;
    }

    return 0;
}

