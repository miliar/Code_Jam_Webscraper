#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <unordered_map>

using namespace std;

bool isOk(vector<char> v){
    vector<char> vv;
    while(v.size() > 1){
        vv.resize(0);
        for(int i = 0; i < v.size(); i = i+2){
            if(v[i] == v[i+1]) return false;
            char c = v[i];
            if(c == 'S' && v[i+1] == 'R') c = 'R';
            if(c == 'P' && v[i+1] == 'S') c = 'S';
            if(c == 'R' && v[i+1] == 'P') c = 'P';
            vv.push_back(c);
        }
        v = vv;
    }
    return true;
}

int main(){
    int T;
    cin >> T;
    for(int t = 0; t < T; t++){
        int n;
        int P, R, S;
        bool ok = false;
        cin >> n >> R >> P >> S;
        vector<char> v;
        for(int i = 0; i < P; i++) v.push_back('P');
        for(int i = 0; i < R; i++) v.push_back('R');
        for(int i = 0; i < S; i++) v.push_back('S');
        cout << "Case #" << t + 1 << ": ";
        do{
            if(isOk(v)){
                for(auto c: v) cout << c; cout << endl;
                ok = true;
                break;
            }
        } while(next_permutation(v.begin(), v.end()));
        if(!ok) cout << "IMPOSSIBLE\n";
    }
    return 0;
}
