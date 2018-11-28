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

void
fractiles()
{
    int64_t k, c, s;
    cin >> k >> c >> s;

    for(int64_t i = 1; i < k + 1; ++ i)
        cout << ' ' << i;
}

int main(const int argc, char * argv [])
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    size_t ncase;
    cin >> ncase;

    for(size_t i = 0; i < ncase; ++i, cout << '\n')
    {
        //cout << CASE(i);
        cout << "Case #" << (i) + 1 << ":";
        fractiles();
    }

    return EXIT_SUCCESS;
}
