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

inline vector<string>
tokenize(const string & line)
{
    vector<string> out(1, "");

    for(const auto i: line)
        if(i == ' ')
            out.push_back("");
        else
            out.back().push_back(i);

    const auto pred = [](const string & wrd){
        return wrd.length() == 0;
    };

    out.erase(remove_if(begin(out), end(out), pred), end(out));
    return out;
}

inline int64_t
xbilingual_brute(const int mask,
                 vector<pair<bool, bool>> val,
                 const vector<vector<size_t>> & a)
{
    const size_t n = a.size();
    int bit = 1;

    for(size_t i = 2; i < n; ++i, bit <<= 1)
        if(bit & mask)
            for(const auto & j: a[i])
                val[j].first = true;
        else
            for(const auto & j: a[i])
                val[j].second = true;

    int64_t out = 0;
    for(const auto & pr: val)
        out += pr.first && pr.second;

    return out;
}


int64_t
bilingual_brute()
{
    size_t n;
    cin >> n;
    string line;
    getline(cin, line);

    size_t count = 0;
    map<string, size_t> m;
    vector<vector<size_t>> a(n);

    for(size_t i = 0; i < n; ++ i) {
        getline(cin, line);
        const auto tok = tokenize(line);
        // DEBUG(tok);
        for(const auto & wrd: tok)
        {
            const auto iter = m.find(wrd);
            if(iter != end(m))
                a[i].push_back(iter->second);
            else
            {
                m[wrd] = count;
                a[i].push_back(count);
                ++ count;
            }
        }
    }

    vector<pair<bool, bool>> val(count, {false, false});

    for(const auto i: a[0])
        val[i].first = true;

    for(const auto i: a[1])
        val[i].second = true;


    int64_t out = count + 1;

    for(int mask = 0; mask < (1 << (n - 2)); ++ mask)
        out = min(out, xbilingual_brute(mask, val, a));

    return out;
}

int main( const int argc, char * argv [])
{
    NO_IO_TIE;
    size_t ncase;
    cin >> ncase;

    for(size_t i = 0; i < ncase; ++i, cout << '\n') {
        cerr << '~' << std::flush;
        cout << CASE(i) << bilingual_brute();
    }

    return EXIT_SUCCESS;
}
