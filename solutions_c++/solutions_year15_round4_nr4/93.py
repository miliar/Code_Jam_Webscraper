
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

vvi p;

int dx[] = {0, 1, 0, -1, 0};
int dy[] = {1, 0, -1, 0, 0};

bool domove(int & c, int & r, int move) {
    c += dx[move];
    if (c < 0) c = p.size() - 1;
    if (c == p.size()) c = 0;
    r += dy[move];
    if (r < 0 || r == p[0].size()) return false;
    return true;
}

bool check(int c, int r, int move) {
    if (!domove(c, r, move))
        return true;
    if (p[c][r] == 0)
        return true;
    int zeros = 0, matches = 0;
    for (int i = 0; i < 4; ++i) {
        int cc = c; int rr = r;
        if (!domove(cc, rr, i))
            continue;
        if (p[cc][rr] == 0) 
            ++zeros;
        else if (p[c][r] == p[cc][rr])
            ++matches;
    }
    return p[c][r] - matches >= 0 && p[c][r] - matches <= zeros;
}

int result = 0;

void solve(int c, int r) {
    if (r == p[0].size()) {
        ++c; r = 0;
    }
    if (c == p.size()) {
        bool good = true;
        for (int i = 1; i < p.size(); ++i) {
            int l = 0; r = i;
            bool current = true;
            for (int j = 0; j < p.size(); ++j) {
                if (p[l] < p[r])
                    break;
                if (p[l] > p[r]) {
                    current = false; break;
                }
                ++l;
                ++r; if (r == p.size()) r = 0;
            }
            if (!current) {
                good = false;
                break;
            }
        }
        if (good)
            ++result;
        return;
    }
    for (int i = 3; i >= 1; --i) {
    //for (int i = 1; i < 4; ++i) {
        p[c][r] = i;
        bool valid = true;
        for (int j = 0; j < 5; ++j) {
            if (!check(c, r, j)) {
                valid = false;
                break;
            }
        }
        if (valid)
            solve(c, r + 1);
    }
    p[c][r] = 0;
}

int solution[7][7];

int main() {
    for (int c = 3; c <= 6; ++c) {
        for (int r = 2; r <= 6; ++r) {
            //c = 4; r = 2;
            p = vvi(c, vi(r, 0));            
            result = 0;
            solve(0, 0);
            solution[c][r] = result;
        }
    }
    int ntests;
    in >> ntests;
    for (int test = 1; test <= ntests; ++test) {
        int r, c;
        in >> r >> c;
        //p.resize(c, vi(r));
        //solve(0, 0);
        out << "Case #" << test << ": " << solution[c][r] << "\n";
    }
    return 0;
}