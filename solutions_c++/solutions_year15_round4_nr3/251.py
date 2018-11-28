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
#include <future>
//#pragma comment( linker, "/stack:10000000" )
using namespace std; 
typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef vector< vll > vvll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

ifstream in( "c.in" );
ofstream out( "c.out" );

int main() {
    int ntests;
    in >> ntests;
    for (int test = 1; test <= ntests; ++test) {
        int n;
        in >> n;
        string line;
        vvi lines(n);
        map<string, int> id;
        getline(in, line);
        for (int i = 0; i < n; ++i) {
            getline(in, line);
            istringstream iss(line);
            string word;
            while (iss >> word) {
                auto it = id.find(word);
                if (it != id.end())
                    lines[i].push_back(it->second);
                else {
                    lines[i].push_back(id.size());
                    id.insert(make_pair(word, id.size()));                    
                }                
            }
        }
        vi english(id.size()), french(id.size());
        int res = id.size();
        for (int mask = 0; mask < (1 << (n - 2)); ++mask) {
            english.assign(english.size(), 0);
            french.assign(french.size(), 0);
            for (int i = 0; i < n; ++i) {
                bool is_english = i == 0 || i > 1 && (mask & (1 << (i - 2)));
                for (int j = 0; j < lines[i].size(); ++j)
                    (is_english ? english : french)[lines[i][j]] = 1;
            }
            int cur = 0;
            for (int i = 0; i < english.size(); ++i)
                cur += english[i] && french[i];
            res = min(res, cur);
        }
        out << "Case #" << test << ": " << res << "\n";
    }
    return 0;
}