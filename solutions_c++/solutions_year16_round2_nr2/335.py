/*
g++ -g -DBUG -D_GLIBCXX_DEBUG -std=c++11 -Wall -Wfatal-errors -o cjam{,.cpp}
g++ -O3 -std=c++11 -Wall -Wfatal-errors -o cjam{,.cpp}
ulimit -s 1268435456
*/
#include <bits/stdc++.h>
#ifdef BUG
    #include "debug.hpp"
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

inline uint64_t xdiff(const uint64_t a, const uint64_t b)
{
    return a < b ? b - a : a - b;
}

void brute(const size_t i,
           const vector<string> & str,
           const array<uint64_t, 2> & acc,
           array<uint64_t, 2> & out)
{
    if(i == str[0].size())
    {
        if(xdiff(acc[0], acc[1]) < xdiff(out[0], out[1]))
        {
            out[0] = acc[0];
            out[1] = acc[1];
        }
        else if(xdiff(acc[0], acc[1]) == xdiff(out[0], out[1]))
        {
            if(acc[0] < out[0] || (acc[0] == out[0] && acc[1] < out[1]))
            {
                out[0] = acc[0];
                out[1] = acc[1];
            }
        }
    }
    else if(str[0][i] != '?' && str[1][i] != '?')
    {
        const uint64_t t = str[0][i] - '0';
        const uint64_t s = str[1][i] - '0';
        brute(i + 1, str, {acc[0] * 10 + t, acc[1] * 10 + s}, out);
    }
    else if(str[0][i] == '?' && str[1][i] == '?')
    {
        for(uint64_t t = 0; t < 10; ++ t)
            for(uint64_t s = 0; s < 10; ++ s)
                brute(i + 1, str, {acc[0] * 10 + t, acc[1] * 10 + s}, out);
    }
    else if(str[0][i] == '?')
    {
        const uint64_t s = str[1][i] - '0';

        for(uint64_t t = 0; t < 10; ++ t)
            brute(i + 1, str, {acc[0] * 10 + t, acc[1] * 10 + s}, out);
    }
    else
    {
        const uint64_t t = str[0][i] - '0';
        for(uint64_t s = 0; s < 10; ++ s)
            brute(i + 1, str, {acc[0] * 10 + t, acc[1] * 10 + s}, out);
    }
}

template < typename value_type>
inline string val2str ( const value_type & x )
{
    ostringstream sout ( ios_base::out );
    sout << x;
    return sout.str();
}

inline vector<string>
close_match()
{
    vector<string> str(2), val(2);
    cin >> str;

    array<uint64_t, 2> out;
    out[0] = 0;
    out[1] = numeric_limits<uint64_t>::max();

    brute(0, str, {0, 0}, out);

    for(size_t i = 0; i < 2; ++ i)
    {
        val[i] = val2str(out[i]);
        while(val[i].size() < str[i].size())
            val[i] = '0' + val[i];
    }

    return val;
}

int main(const int argc, char * argv [])
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    size_t ncase;
    cin >> ncase;

    for(size_t i = 0; i < ncase; ++i, cout << '\n')
    {
        const auto out = close_match();
        cout << CASE(i) << out[0] << ' ' << out[1];
    }

    return EXIT_SUCCESS;
}
