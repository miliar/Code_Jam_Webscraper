#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>


using namespace std;

typedef long long LL;

string solve(string s){
    string res;
    for(int i = 0; i < s.size(); ++i){
        string left = string() + s[i] + res;
        string right = res + s[i];
        if(left > right){
            res = left;
        }else{
            res = right;
        }
    }
    return res;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        string s;
        cin >> s;
        cout << "Case #" << t << ": " << solve(s) << endl;
    }
    return 0;
}

