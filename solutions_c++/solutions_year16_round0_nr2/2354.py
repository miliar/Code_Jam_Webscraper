#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int solve(string s){
    s += '+';
    int res = 0;
    for(int i = 1; i < s.length(); i++){
        if(s[i] != s[i-1]){
            res ++;
        }
    }
    return res;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int qqq = 1; qqq <= T; qqq++){
        string s;
        cin >> s;
        int res = solve(s);
        cout << "Case #" << qqq << ": " << res << endl;
    }
    return 0;
}
