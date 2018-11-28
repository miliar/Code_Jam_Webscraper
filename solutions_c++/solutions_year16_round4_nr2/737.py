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

inline double
calc(unsigned mask, const size_t k, const vector<double> & a)
{
    vector<size_t> idx;
    for(size_t i = 0; mask > 0; mask >>= 1, ++ i)
        if(mask & 1) idx.push_back(i);

    if(k != idx.size()) return 0;

    vector<double> out(k + 1, 0);
    out[0] = 1.0;

    for(const auto i: idx)
    {
        for(size_t s = k; 0 < s; --s)
            out[s] = a[i] * out[s - 1] + (1.0 - a[i]) * out[s];

        out[0] = (1.0 - a[i]) * out[0];
    }

    return out[k / 2];
}

double
xsolve(const size_t idx,
       const size_t mask,
       const size_t n,
       const size_t k,
       const vector<double> & a,
       vector<vector<double>> & cache)
{
    if(idx == n) return calc(mask, k, a);
    if(cache[idx][mask] != -1) return cache[idx][mask];

    auto out =     xsolve(idx + 1, mask,              n, k, a, cache);
    out = max(out, xsolve(idx + 1, mask | (1 << idx), n, k, a, cache));

    return cache[idx][mask] = out;
}


inline double
red_tape_committee()
{
    size_t n, k;
    cin >> n >> k;

    vector<double> a(n);
    cin >> a;

    const size_t size = 1 << n;
    vector<vector<double>> cache(n, vector<double>(size, -1));

    return xsolve(0, 0, n, k, a, cache);
}

int main(const int, char **)
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    size_t ncase;
    cin >> ncase;

    for(size_t idx = 0; idx < ncase; ++idx, cout << '\n')
    {
        cout << CASE(idx) << setprecision(17) << red_tape_committee();
    }

    return EXIT_SUCCESS;
}
