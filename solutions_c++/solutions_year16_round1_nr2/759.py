#include <cstdlib>
#include <bitset>
#include <functional>
#include <utility>
#include <tuple>
#include <limits>
#include <cstdint>
#include <cctype>
#include <string>
#include <array>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <random>
#include <numeric>
#include <iostream>
#include <sstream>

using namespace std;

void comp(int tc){
    int n;
    cin >> n;
    unordered_map<int, int> m;
    for(int i=0; i<2*n-1; ++i){
        for(int j=0; j<n; ++j){
            int v;
            cin >> v;
            ++m[v];
        }
    }
    
    vector<int> res;
    for(auto &p : m){
        if(p.second & 1){
            res.push_back(p.first);
        }
    }
    
    sort(res.begin(), res.end());
    if(res.size() != n){
        cerr << "Incorrect" << endl;
    }
    
    cout << "Case #" << tc << ": ";
    for(int v : res){
        cout << v << " ";
    }
    cout << endl;
}

int main(){
    int T;
    cin >> T;
    for(int tc=1; tc<=T; ++tc){
        comp(tc);
    }
}