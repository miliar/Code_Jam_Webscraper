#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

int f(string s){

    int p = 0, res = 0, n = (int)s.size();

    for (int i = 0; i < n; i++){
        if (i > 0){
            if (s[i] != s[i - 1])
                res++;
        }
    }
    res++;

    if (s[n - 1] == '+')
        res--;

    return res;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        string s;
        cin >> s;

        cout << "Case #" << i + 1 << ": " << f(s) << "\n";
    }
}
