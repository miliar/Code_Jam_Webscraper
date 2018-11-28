#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int t, T, n;
    cin >> T;
    for (t = 1; t <= T; t++){
        cin >> n;
        vector<double> a(n), b(n);
        for (int i = 0; i < n; i++){
            cin >> a[i];
        }
        for (int i = 0; i < n; i++){
            cin >> b[i];
        }
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        int c = 0;
        for (int i = 0; i < n; i++){
            if (a[i] > b[c]){
                c++;
            }
        }
        int d = 0;
        for (int i = 0; i < n; i++){
            vector<double>::iterator it = upper_bound(b.begin(), b.end(), a[i]);
            if (it == b.end()){
                b.erase(b.begin());
                d++;
            }else{
                b.erase(it);
            }
        }
        cout << "Case #" << t << ": " << c << ' ' << d << '\n';
    }
}
