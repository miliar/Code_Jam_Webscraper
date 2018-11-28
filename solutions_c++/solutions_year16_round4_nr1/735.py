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

string
build_soln(const size_t n, const char val)
{
    static map<pair<size_t, char>, string> cache;

    if(n == 0) return string(1, val);

    {
        const auto iter = cache.find({n, val});
        if(iter != end(cache))
            return iter->second;
    }

    string a, b;

    if(val == 'R')
    {
        a = build_soln(n - 1, 'R');
        b = build_soln(n - 1, 'S');
    }
    else if (val == 'S')
    {
        a = build_soln(n - 1, 'S');
        b = build_soln(n - 1, 'P');
    }
    else // val == 'P'
    {
        a = build_soln(n - 1, 'P');
        b = build_soln(n - 1, 'R');
    }

    return cache[make_pair(n, val)] = min(a + b, b + a);
}


inline string
rather_perplexing_showdown()
{
    size_t n, rock, paper, scissors;
    cin >> n >> rock >> paper >> scissors;

    string game("RSP");
    vector<string> out;

    for(const auto ch: game)
    {
        const auto str = build_soln(n, ch);
        map<char, size_t> cnt;
        for(const auto i: str)
            ++ cnt[i];

        if(cnt['R'] == rock && cnt['P'] == paper && cnt['S'] == scissors)
            out.push_back(str);
    }

    if(out.empty())
        return "IMPOSSIBLE";

    return * min_element(begin(out), end(out));
}

int main(const int, char **)
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    size_t ncase;
    cin >> ncase;

    for(size_t idx = 0; idx < ncase; ++idx, cout << '\n')
    {
        cout << CASE(idx) << rather_perplexing_showdown();
    }

    return EXIT_SUCCESS;
}
