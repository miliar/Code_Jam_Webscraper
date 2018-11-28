
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#pragma warning( disable : 4244 4267 4018 4996 4800 )
//#pragma comment( linker, "/stack:10000000" )
using namespace std; 
typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef vector< vll > vvll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

ifstream in( "d.in" );
ofstream out( "d.out" );

int main() {
    int ntests;
    in >> ntests;
    for (int test = 1; test <= ntests; ++test) {        
        int p;
        in >> p;
        vi e(p), cnt(p), acc(p);
        vi res;
        for (auto & x : e) in >> x;
        for (auto & x : cnt) in >> x;
        int nzero = cnt[0];
        for (auto & x : cnt)
            x /= nzero;
        while (nzero > 1) {
            nzero /= 2;
            res.push_back(0);
        }
        --cnt[0];
        int lo = 0, hi = p - 1;
        for (;;) {
            while (lo <= hi && !cnt[lo]) ++lo;
            while (lo <= hi && !cnt[hi]) --hi;
            if (lo > hi) break;
            int cur = e[lo];
            res.push_back(cur);
            int mid = hi;
            acc.assign(acc.size(), 0);
            for (int i = hi; i >= lo; --i) {
                int x = cnt[i] - acc[i];
                cnt[i] -= x;
                while (e[mid] > e[i] - cur) --mid;
                acc[mid] += x;
            }            
        }
        out << "Case #" << test << ": ";
        for (int i = 0; i < res.size(); ++i)
            out << res[i] << ' ';
        out << "\n";
    }
    return 0;
}