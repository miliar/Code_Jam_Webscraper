#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

int f(int n){
    if (n == 0){
        return -1;
    }
    int res = 0, cur = 1;
    set <int> s;
    for (int i = 0; i < 10; i++){
        s.insert(i);
    }

    while ((int)s.size() > 0){
        int k = n * cur;

        while (k > 0){
            if (s.find(k%10) != s.end())
                s.erase(k%10);
            k /= 10;
        }
        cur++;
    }

    return (cur - 1) * n;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++){
        int n;
        cin >> n;

        int e = f(n);
        if (e == -1){
            cout << "Case #" << i + 1 << ": " << "INSOMNIA\n";
        }
        else
            cout << "Case #" << i + 1 << ": " << e << "\n";
    }
}
