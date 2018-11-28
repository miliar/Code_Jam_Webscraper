#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(){
    string s;
    int t;
    cin >> t;
    for(int test = 1; test <= t; test++){
        cin >> s;
        string ans = s.substr(0, 1);
        for(int i = 1; i < s.size(); i++){
            if(s[i] >= ans[0] )
                ans = s[i] + ans;
            else
                ans = ans + s[i];
        }
        cout << "Case #" << test << ": " <<ans << endl;
    }
    return 0;
}
