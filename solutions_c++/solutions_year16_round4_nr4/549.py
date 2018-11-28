#include <bits/stdc++.h>
#ifdef BUG
    #include "../top-coder/debug.hpp"
#else
    #define DEBUG(var)
#endif
#define CASE(i) "Case #" << (i) + 1 << ": "

using namespace std;
template<class T1, class T2> inline istream &
operator>>(istream & fin, pair<T1, T2> & pr)
{ fin >> pr.first >> pr.second; return fin; }
template<class T0, class T1, class T2> inline istream &
operator>>(istream & fin, tuple<T0, T1, T2> & t)
{ fin >> get<0>(t) >> get<1>(t) >> get<2>(t); return fin; }
template<class T> inline istream &
operator>>(istream & fin, vector<T> & a) {
for(auto & u: a) fin >> u; return fin; }
template<class T, size_t n> inline istream &
operator>>(istream & fin, array<T, n> & a) {
for(auto & u: a) fin >> u; return fin; }
/* ------------------------------ */

inline bool
isvalid(const size_t idx,
        const vector<size_t> & ord,
        const vector<vector<bool>> & a,
        vector<bool> & tag)
{
    const auto n = a.size();
    if(idx == n) return true;
    bool fail = true;

    for(size_t i = 0; i < n; ++ i)
        if(a[ord[idx]][i] && !tag[i])
        {
            tag[i] = true;
            if(!isvalid(idx + 1, ord, a, tag))
            {
                return false;
            }

            tag[i] = false;
            fail = false;
        }

    return !fail;
}

inline bool
isvalid(const vector<vector<bool>> & a)
{
    const auto n = a.size();

    vector<size_t> ord(n);
    iota(begin(ord), end(ord), 0);

    do
    {
        vector<bool> tag(n, false);
        if(!isvalid(0, ord, a, tag)) return false;

    } while(next_permutation(begin(ord), end(ord)));

    return true;
}

size_t
xsolve(const size_t idx,
       const size_t mask,
       vector<vector<bool>> & a,
       vector<vector<size_t>> & cache)
{
    const auto n = a.size();

    if(idx == n)
    {
        return isvalid(a) ? 0 : 200;
    }

    if(cache[idx][mask] != (size_t) -1)
        return cache[idx][mask];

    size_t out = 200; // xsolve(idx + 1, mask, a, cache);

    const size_t size = 1 << n;
    for(size_t i = 0; i < size; ++ i)
    {
        bool fail = false;
        size_t inc = 0;

        vector<size_t> xs;

        for(size_t s = 0, w = i; 0 < w && !fail; ++ s, w >>= 1)
        {
            if(w & 1)
            {
                if(a[idx][s])
                {
                    fail = true;
                    break;
                }

                a[idx][s] = true;
                xs.push_back(s);
                ++ inc;
            }
        }

        if(!fail)
        {
            out = min(out, inc + xsolve(idx + 1, mask | (i << (idx * n)), a, cache));
        }

        for(const auto x: xs)
            a[idx][x] = false;

        // for(size_t s = 0, w = i; 0 < w && !fail; ++ s, w >>= 1)
        //     if(w & 1) a[idx][s] = false;
    }

    return cache[idx][mask] = out;
}


inline size_t
freeform_factory()
{
    size_t n;
    cin >> n;
    vector<vector<bool>> a(n, vector<bool>(n));
    {
        vector<string> str(n);
        cin >> str;

        for(size_t i = 0; i < n; ++ i)
            for(size_t j = 0; j < n; ++ j)
                a[i][j] = str[i][j] == '1';
    }

    const size_t size = 1 << (n * n);
    vector<vector<size_t>> cache(n, vector<size_t>(size, (size_t) -1));

    return xsolve(0, 0, a, cache);
}

int main(const int, char **)
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    size_t ncase;
    cin >> ncase;

    for(size_t idx = 0; idx < ncase; ++idx, cout << '\n')
    {
        cout << CASE(idx) << freeform_factory();
    }

    return EXIT_SUCCESS;
}
