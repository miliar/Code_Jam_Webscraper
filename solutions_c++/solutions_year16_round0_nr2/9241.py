#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n,u,k = 0;
    string s;
    char prev;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> n;

    for(int i=0;i<n;i++){
        cin >> s;
        k = 0;
        u = 1;
        prev = s[0];
        for(int j=1; ;j++){
            if(u == s.length() && s[0] == '+') break;

            if(s[j] == prev){  u++; prev = s[j]; }
            else {
                for(int v = 0; v<u; v++){
                    if(s[v] == '+') s[v] = '-';
                    else
                        if(s[v] == '-') s[v] = '+';
                }
                k++; j = 0; u = 1; prev = s[0];
            }
        }
        cout << "Case #" << i+1 << ": " << k << "\n";
    }


    return 0;
}
