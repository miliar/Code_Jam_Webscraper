#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

int a[10001];

int st(int a, int b){
    if (a == 1) return b;
    if (b == 1) return a;
    if (a == -1) return -b;
    if (b == -1) return -a;
    if (a == b)
        return -1;
    if (a == -b)
        return 1;
    int m = 1;
    if (a < 0){
        m *= -1;
        a *= -1;
    }
    if (b < 0){
        m *= -1;
        b *= -1;
    }
    if (a > b){
        swap(a, b);
        m *= -1;
    }
    if (a == 2 && b == 3) return m * 4;
    if (a == 2 && b == 4) return m * (-3);
    if (a == 3 && b == 4) return m * 2;
}

int get(int l, int x){
    int ans = 1;
    for (int i = 0; i < x; i++){
        ans = st(ans, l);
    }
    return ans;
}

int main()
{
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int ct = 0; ct < t; ct++)
    {
        int n, x;
        string s;
        cin >> n >> x >> s;
        for (int i = 0; i < n; i++){
            if (s[i] == 'i'){
                a[i] = 2;
            }
            else if (s[i] == 'j'){
                a[i] = 3;
            }
            else{
                a[i] = 4;
            }
        }
        int l = 1;
        int xi = -1;
        int xk = -1;
        for (int i = 0; i < n; i++){
            l = st(l, a[i]);
            if (l == 2 && xi == -1) xi = i;
        }
        int l1 = l;
        if (xi == -1){
            for (int j = 1; j < min(x, 4); j++){
                for (int i = 0; i < n; i++){
                    l1 = st(l1, a[i]);
                    if (l1 == 2){
                        xi = j * x + i;
                        break;
                    }
                }
                if (xi != -1) break;
            }
        }
        if (xi == -1){
            cout << "Case #" << ct + 1 << ": No\n";
            continue;
        }
        l1 = 1;
        for (int j = x - 1; j >= max(x - 4, 0); j--){
            for (int i = n - 1; i >= 0; i--){
                l1 = st(a[i], l1);
                if (l1 == 4){
                    xk = j * x + i;
                    break;
                }
            }
            if (xk != -1) break;
        }
        if (xk == -1){
            cout << "Case #" << ct + 1 << ": No\n";
            continue;
        }
        if (xi >= xk){
            cout << "Case #" << ct + 1 << ": No\n";
            continue;
        }
        if (get(l, x % 4) == -1){
            cout << "Case #" << ct + 1 << ": Yes\n";
        }
        else{
            cout << "Case #" << ct + 1 << ": No\n";
        }
    }
    return 0;
}
