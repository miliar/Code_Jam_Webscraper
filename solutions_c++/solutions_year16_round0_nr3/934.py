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
solve(const size_t i,
      const size_t k,
      string & acc,
      vector<string> & out)
{
    if(out.size() == k) return;
    if(acc.size() < i + 4)
    {
        if(find(begin(out), end(out), acc) == end(out))
            out.push_back(acc);

        return;
    }

    solve(i + 1, k, acc, out);
    acc[i] = acc[i + 1] = '1';

    solve(i + 2, k, acc, out);
    acc[i] = acc[i + 1] = '0';
}


void coin_jam()
{
    size_t n, k;
    cin >> n >> k;

    string tail = "3 4 5 6 7 8 9 10 11";

    string acc(n, '0');
    acc[0] = acc[1] = acc[n - 1] = acc[n - 2] = '1';

    vector<string> out;
    solve(2, k, acc, out);

    for(const auto & r: out)
        cout << r << ' ' << tail << '\n';
}

int main(const int argc, char * argv [])
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    size_t ncase;
    cin >> ncase;

    for(size_t i = 0; i < ncase; ++i, cout << '\n') {
        cout << "Case #" << (i) + 1 << ":\n";
        coin_jam();
    }

    return EXIT_SUCCESS;
}
