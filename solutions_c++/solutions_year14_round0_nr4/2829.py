#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    cout.precision(15);
    vector<double> a, b;
    vector<bool> f;
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ": ";
        int n;
        cin >> n;
        a.assign(n, 0);
        b.assign(n, 0);
        f.assign(n, true);
        for (int i=0;i<n;i++)
            cin >> a[i];
        for (int i=0;i<n;i++)
            cin >> b[i];
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        int c = 0, d = 0;
        for (int i=n-1;i>=0;i--){
            bool s = true;
            for (int j=0;j<n;j++){
                if ((f[j]) && (a[i] < b[j])){
                    s = false;
                    f[j] = false;
                    break;
                }
            }
            if (s){
                d++;
                for (int j=0;j<n;j++){
                    if (f[j]){
                        f[j] = false;
                        break;
                    }
                }
            }
        }
        int r = n-1;
        int l = 0;
        int e = n-1;
        while (l <= r){
            if (a[r] > b[e]){
                r--;
                c++;
            }else{
                l++;
            }
            e--;
        }
        cout << c << ' ' << d << endl;
    }
    return 0;
}
