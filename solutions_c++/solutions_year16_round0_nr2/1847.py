#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

void solve()
{
    string s;
    cin >> s;
    int n = s.length();
    int cnt = 0;
    if (s[n-1] == '-') cnt++; 
    for (int i = 0; i < n-1; i++)
        if (s[i] != s[i+1]) cnt++;
    cout << cnt << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++){
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
