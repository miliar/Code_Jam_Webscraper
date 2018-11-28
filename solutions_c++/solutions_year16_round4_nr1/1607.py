#include <cstdlib>
#include <bitset>
#include <functional>
#include <utility>
#include <cstddef>
#include <initializer_list>
#include <tuple>

#include <memory>

#include <limits>

#include <cctype>
#include <cstring>
#include <string>

#include <array>
#include <vector>
#include <deque>
#include <list>
#include <forward_list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>

#include <algorithm>

#include <iterator>

#include <cmath>
#include <complex>
#include <valarray>
#include <random>
#include <numeric>
#include <ratio>

#include <ios>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstdio>

#include <regex>

#include <type_traits>

using namespace std;

map<pair<char, char>, char> win =
{ {{'p','r'}, 'p'},
  {{'r','p'}, 'p'},
  {{'p','s'}, 's'},
  {{'s','p'}, 's'},
  {{'r','s'}, 'r'},
  {{'s','r'}, 'r'},
};


bool works(vector<char> v) {
    vector<char> tmp;
    while(v.size() > 1) {
        for(int i=0; i<(int)v.size()-1; i+=2){
            if(v[i] == v[i+1]){
                return false;
            }
            tmp.push_back(win[{v[i], v[i+1]}]);
        }
        v.clear();
        v.swap(tmp);
    }
    return true;
}

void comp(int tc){
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    vector<char> v;
    v.insert(v.end(), p, 'p');
    v.insert(v.end(), r, 'r');
    v.insert(v.end(), s, 's');
    
    cout << "Case #" << tc << ": ";
    
    do {
        if(works(v)) {
            for(char c : v) {
                cout << (char)toupper(c);
            }
            cout << endl;
            return;
        }
        
    } while(next_permutation(v.begin(), v.end()));
    
    cout << "IMPOSSIBLE" << endl;
}

int main(){
    int T;
    cin >> T;
    for(int tc=1; tc<=T; ++tc){
        comp(tc);
    }
}