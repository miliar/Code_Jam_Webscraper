
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

#ifdef LOCAL
ifstream in( "d.in" );
#else
istream & in = cin;
#endif
//ostream & out = cout;
ofstream out( "d.out" );

int m, n;
vs str;
map<string, int> tries[4];
int max_nodes;
int cnt;

void add(map<string, int>& trie, string const & s, int cnt) {
    for (int len = 1; len <= s.size(); ++len) {
        string str = s.substr(0, len);
        auto it = trie.find(str);
        if (it == trie.end())
            trie[str] = cnt;
        else {
            it->second += cnt;
            if (it->second == 0)
                trie.erase(it);
        }
    }    
}

void search(int idx) {
    if (idx == m) {
        int sum  = 0;
        for (int i = 0; i < n; ++i) {
            sum += tries[i].size();
            if (tries[i].size())
                ++sum;
        }
        if (sum > max_nodes) {
            max_nodes = sum;
            cnt = 1;
        } else if (sum == max_nodes)
            ++cnt;
        return;            
    }
    for (int i = 0; i < n; ++i) {
        add(tries[i], str[idx], 1);
        search(idx + 1);
        add(tries[i], str[idx], -1);
    }
}

int main() {
    int ntests;
    in >> ntests;
    for (int test = 1; test <= ntests; ++test) {        
        max_nodes = cnt = 0;
        in >> m >> n;
        str = vs(m);
        for (int i = 0; i < m; ++i)
            in >> str[i];

        search(0);
        out << "Case #" << test << ": " << max_nodes << " " << cnt << "\n";
    }
    return 0;
}