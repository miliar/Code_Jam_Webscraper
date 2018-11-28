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
    string s;
    cin >> s;
    deque<char> res;
    for(char c : s){
        if(res.empty()){
            res.push_back(c);
        }else{
            if(c >= res.front()){
                res.push_front(c);
            }else{
                res.push_back(c);
            }
        }
    }

    cout << "Case #" << tc << ": " << string(res.begin(), res.end()) << endl;
    
}

int main(){
    int T;
    cin >> T;
    for(int tc=1; tc<=T; ++tc){
        comp(tc);
    }
}