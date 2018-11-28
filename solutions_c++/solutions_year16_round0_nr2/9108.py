#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

long long T;
string s;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin >> T;
    for(int t = 0; t < T; t++){
        cin >> s;
        long long ans = 0, l = s.size();
        for(int i = 0; i < l - 1; i++){
            if(s[i] != s[i + 1]) ans++;
        }
        if(s[l - 1] == '-') ans++;
        cout << "Case #" << t + 1 << ": " << ans << endl;
    }
    return 0;
}

