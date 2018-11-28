#include<bits/stdc++.h>
using namespace std;
#define ll long long
int solve(string s){
    int res = 0;
    for(int i=s.size()-1; i>=0; --i){
        if(s[i] == '-'){
            res++;
            for(int j=0; j<=i; ++j){
                if(s[j] == '+'){
                    s[j] = '-';
                } else {
                    s[j] = '+';
                }
            }
        }
    }
    return res;
}
int main () {
    ios_base::sync_with_stdio(false);
    freopen("C:\\in.txt","r", stdin);
    freopen("C:\\gcj2016\\out.txt", "w", stdout);
    int TC;
    cin >> TC;
    for(int t = 1; t<=TC; ++t){
        string s;
        cin >> s;
        cout << "Case #" << t << ": ";
        cout << solve(s);
        cout << endl;
    }

    return 0;
}
