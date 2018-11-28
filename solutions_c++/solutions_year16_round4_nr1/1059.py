#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

map<pair<char, int>, string> memo;

string f(char top, int k);

string g(char top, int k){
    if(k == 0){
        string value;
        value += top;
        return value;
    }

    string a = f(top, k - 1);
    string b;
    if(top == 'P'){
        b = f('R', k - 1);
    }else if(top == 'R'){
        b = f('S', k - 1);
    }else{
        b = f('P', k - 1);
    }
    return min(a + b, b + a);
}

string f(char top, int k){
    pair<char, int> q(top, k);
    if(not memo.count(q)){
        memo[q] = g(top, k);
    }
    return memo[q];
}

void addSol(vector<string>& sols, int n, int r, int p, int s, char start){
    string sol = f(start, n);
    for(const auto c : sol){
        if(c == 'P'){
            p--;
        }else if(c == 'R'){
            r--;
        }else{
            s--;
        }
    }
    if(r == 0 and p == 0 and s == 0){
        sols.push_back(sol);
    }
}

int main(){
    //ios::sync_with_stdio(false);

    int T;
    cin >> T;

    for(int tc = 1; tc <= T; tc++){
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        vector<string> sols;
        addSol(sols, n, r, p, s, 'P');
        addSol(sols, n, r, p, s, 'R');
        addSol(sols, n, r, p, s, 'S');
        
        cout << "Case #" << tc << ": ";
        if(sols.empty()){
            cout << "IMPOSSIBLE\n";
        }else{
            sort(sols.begin(), sols.end());
            cout << sols[0] << '\n';
        }
    }
}
