#include <bits/stdc++.h>

using namespace std;
int T, k;
string S;
char c;
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("bla2.out", "w", stdout);
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        cin >> S; k = 0;
        cout << "Case #" << t << ": ";
        for(int i = 0; i < S.size(); i++)
            if(S[i] == '+') k++;
        if(k == S.size()) cout << 0 << "\n";
        else if(k == 0) cout << 1 << "\n";
        else
        {   k = 0;
            for(int i = 1; i < S.size(); i++)
            {
                if(S[i] != S[i-1]) k++;
            }
        if(S[S.size()-1] == '-') cout << k+1 << "\n";
            else cout << k << "\n";
        }
    }
    return 0;
}

