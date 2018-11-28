#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cctype>
#include <cstring>
#include <sstream>
#include <iostream>
#include <iomanip>
//#include <gmp.h>
#ifdef HOME_RUN
# include <debug.hpp>
# include <dump.hpp>
# include <cassert>
#else
# define TR(x) do{}while(0)
# ifdef assert
#  indef assert
# endif
# define assert(x) do{}while(0)
#endif
using namespace std;

#define ALL(C) (C).begin(), (C).end()
#define forIter(I,C) for( auto I : (C) )
#define forNF(I,S,C) for( int I=(S); I<int(C); ++I )
#define forN(I,C) forNF(I,0,C)
#define forEach(I,C) forN(I,(C).size())
typedef vector<int> VI; typedef vector<VI> VVI; typedef vector<string> VS;
typedef unsigned u32; typedef long long i64; typedef unsigned long long u64;

size_t line_number;
void input_error(const string& m = string()) {
    cerr << "Input failed at line " << line_number << ": " << m << endl; exit(1);
}
void check_space(const string& s) { for ( auto c : s ) assert(isspace(c&255)); }
string get_str(istream& in) {
    string ret; ++line_number; if ( !getline(in, ret) ) input_error(); return ret;
}
istream& skip_endl(istream& in) { check_space(get_str(in)); return in; }
istream& skip_eof(istream& in) { string s;
    while ( ++line_number, getline(in, s) ) check_space(s);
    if ( !in.eof() ) input_error(); return in;
}

map<string, int> str_index;
int get_index(const string& s) {
    return str_index.insert(make_pair(s, str_index.size())).first->second;
}
inline int get_str_index(istream& in) { return get_index(get_str(in)); }

/////////////////////////////////////////////////////////////////////////////

const int INF = 999999999;

u32 N, D;
struct RNG
{
    u32 s, a, c, r;
    u32 get() {
        return s = (u64(s)*a+c)%r;
    }
};
istream& operator>>(istream& in, RNG& r)
{
    return in >> r.s >> r.a >> r.c >> r.r >> skip_endl;
}
RNG rs, rm;
struct Empl
{
    u32 id, m, s;
    vector<u32> ss;
    bool included;
    
    void init(int id, int m, int s) {
        this->id = id;
        this->m = id? m%id: 0;
        this->s = s;
        ss.clear();
        included = false;
    }
};
vector<Empl> ee;

u32 cnt, s0;

u32 count_included(u32 id)
{
    assert(id < N);
    Empl& e = ee[id];
    if ( e.s > s0+D || e.s < s0 ) return 0;
    u32 r = 1;
    for ( auto i : e.ss ) {
        r += count_included(i);
    }
    return r;
}

void include(u32 id)
{
    assert(id < N);
    Empl& e = ee[id];
    assert(e.s >= s0);
    assert(e.s <= s0+D);
    if ( e.included ) return;
    e.included = true;
    ++cnt;
    for ( auto i : e.ss ) {
        u32 s = ee[i].s;
        if ( s >= s0 && s <= s0+D ) {
            include(i);
        }
    }
}

void exclude(u32 id)
{
    assert(id < N);
    Empl& e = ee[id];
    if ( !e.included ) return;
    e.included = false;
    --cnt;
    for ( auto i : e.ss ) {
        exclude(i);
    }
}

int num_cases = 1, part_cases = 0;
int main(int argc, const char** argv)
{
    cin >> num_cases >> skip_endl;
    if ( argc == 2 ) {
        part_cases = atoi(argv[1]);
    }
    forN ( nc, num_cases ) {
        cin >> N >> D >> skip_endl;
        cin >> rs;
        cin >> rm;
        ee.clear();
        ee.resize(N);
        ee[0].init(0, 0, rs.s);
        //TR(D); TR(0|ee[0].s);
        for ( u32 i = 1; i < N; ++i ) {
            ee[i].init(i, rm.get(), rs.get());
            //TR(i|ee[i].m|ee[i].s);
            if ( i ) {
                u32 m = ee[i].m;
                ee[m].ss.push_back(i);
            }
        }

        // error check
        if ( !cin ) input_error();
        // main code

        multimap<u32, u32> eeBySal;
        for ( auto& e : ee ) {
            eeBySal.insert(make_pair(e.s, e.id));
        }

        u32 result = 0;

        /*
        for ( s0 = max(ee[0].s, D)-D; s0 <= ee[0].s+D; ++s0 ) {
            u32 cnt = count_included(0);
            TR(s0|cnt);
            result = max(result, cnt);
        }
        */
        
        cnt = 0;
        s0 = ee[0].s;
        include(0);
        auto si = eeBySal.lower_bound(s0), sj = eeBySal.upper_bound(s0+D);
        //TR(s0|cnt);
        result = cnt;
        while ( si != eeBySal.begin() ) {
            s0 = prev(si)->first;
            if ( s0+D < ee[0].s ) break;
            while ( si != eeBySal.begin() && prev(si)->first == s0 ) {
                --si;
                if ( ee[ee[si->second].m].included )
                    include(si->second);
            }
            while ( prev(sj)->first > s0+D ) {
                --sj;
                exclude(sj->second);
            }
            result = max(result, cnt);
            //TR(s0|cnt);
        }
        
        
        // output
        cout << "Case #"<<nc+1<<": ";
        cout << result;
        cout << endl;
    }
    cin >> skip_eof;
}
