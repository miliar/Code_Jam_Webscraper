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
#define NO_IO_TIE ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
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

double kiddie_pool_brute()
{
    size_t n;
    double vol, xtemp;
    cin >> n >> vol >> xtemp;

    typedef struct {
        double rate;
        double temp;
    } tap_t;

    vector<tap_t> a;
    a.reserve(n);

    for(size_t i = 0; i < n; ++ i)
    {
        double rate, temp;
        cin >> rate >> temp;
        a.push_back({rate, temp});
    }

    if(n == 1)
    {
        if(a[0].temp != xtemp)
            return -1;

        return vol / a[0].rate;
    }

    //  n == 2
    if(a[1].temp < a[0].temp)
        swap(a[0], a[1]);

    if(a[1].temp < xtemp || xtemp < a[0].temp)
        return -1;

    if(a[0].temp == a[1].temp)
        return vol / (a[0].rate + a[1].rate);

    const auto t1 = vol * (xtemp - a[0].temp) / (a[1].temp - a[0].temp) / a[1].rate;
    const auto t0 = (vol - t1 * a[1].rate) / a[0].rate;

    return max(t0, t1);
}

int main( const int argc, char * argv [])
{
    NO_IO_TIE;
    size_t ncase;
    cin >> ncase;

    for(size_t i = 0; i < ncase; ++i, cout << '\n') {
        cerr << '~' << std::flush;
        cout << CASE(i);
        const auto soln = kiddie_pool_brute();
        if(soln < 0)
            cout << "IMPOSSIBLE";
        else
            cout << setprecision(15) << soln;
    }

    return EXIT_SUCCESS;
}
