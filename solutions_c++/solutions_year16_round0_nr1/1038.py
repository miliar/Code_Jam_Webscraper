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

inline uint64_t
counting_sheep()
{
    const uint64_t inf = numeric_limits<uint64_t>::max() >> 1;

    uint64_t n;
    cin >> n;
    if(n == 0) return (uint64_t) -1;

    vector<bool> tag(10, false);
    uint64_t acc = 0;

    for(size_t i = 0; i < 100000 && acc < inf; ++i)
    {
        acc += n;

        for(auto w = acc; 0 < w; w /= 10)
            tag[w % 10] = true;

        if(find(begin(tag), end(tag), false) == end(tag)) return acc;
    }

    return (uint64_t) -1;
}

int main(const int argc, char * argv [])
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    size_t ncase;
    cin >> ncase;

    for(size_t i = 0; i < ncase; ++i, cout << '\n') {
        cout << CASE(i);
        const auto out = counting_sheep();

        if(out == (uint64_t) -1)
            cout << "INSOMNIA";
        else
            cout << out;
    }

    return EXIT_SUCCESS;
}
