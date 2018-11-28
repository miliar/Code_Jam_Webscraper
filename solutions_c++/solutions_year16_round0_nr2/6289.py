#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
using namespace std;

char flip(char c){
    if(c == '+') return '-';
    return '+';
}

string maneuver(string s, int n){
    int start = 0;
    int end = n;
    while(start <= end){
        char a = flip(s[start]);
        char b = flip(s[end]);
        s[start] = b;
        s[end] = a;
        start++;
        end--;
    }
    return s;
}

int solve(string s, int l){
    
    if(s[l] == '+'){
        while(l >=0 && s[l] == '+'){
            l--;
        }

        // yay!
        if(l < 0){
            return 0;
        }

        return solve(s, l);
    }
    else if(s[0] == '+'){
        int idx = 0;
        while(idx <= l && s[idx] == '+'){
            s[idx] = '-';
            idx++;
        }

        // yay!
        if(idx > l){
            return 0;
        }

        return 1 + solve(s, l);
    }
    else{
        s = maneuver(s, l);
        return 1 + solve(s, l);
    }
}

int main(){
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);

    int t;
    string s;
    cin >> t;
    for(int c = 1; c <= t; c++){
        cin >> s;
        cout << "Case #" << c << ": " << solve(s, s.size() - 1) << endl;
    }

    return 0;
}