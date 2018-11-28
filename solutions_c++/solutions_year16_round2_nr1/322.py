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

inline string
getting_the_digits()
{
    vector<string> digit({"ZERO", "ONE", "TWO", "THREE", "FOUR",
            "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"});

    string str;
    cin >> str;

    size_t acc = str.size();
    array<size_t, 26> cnt;
    cnt.fill(0);

    for(const auto i: str)
        ++ cnt[i - 'A'];

    string out;

    const auto drop = [&cnt, &acc, &out, &digit](const size_t idx) {
        out += '0' + (char) idx;
        acc -= digit[idx].size();
        for(const auto i: digit[idx])
            -- cnt[i - 'A'];
    };

    while(0 < acc)
    {
        if     (cnt['Z' - 'A']) drop(0);
        else if(cnt['W' - 'A']) drop(2);
        else if(cnt['U' - 'A']) drop(4);
        else if(cnt['X' - 'A']) drop(6);
        else if(cnt['G' - 'A']) drop(8);
        else if(cnt['O' - 'A']) drop(1);
        else if(cnt['R' - 'A']) drop(3);
        else if(cnt['F' - 'A']) drop(5);
        else if(cnt['V' - 'A']) drop(7);
        else drop(9);
    }

    sort(begin(out), end(out));
    return out;
}

int main(const int argc, char * argv [])
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    size_t ncase;
    cin >> ncase;

    for(size_t i = 0; i < ncase; ++i, cout << '\n')
        cout << CASE(i) << getting_the_digits();

    return EXIT_SUCCESS;
}
