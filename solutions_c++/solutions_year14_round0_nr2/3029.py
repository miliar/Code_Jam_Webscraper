#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    cout.precision(15);
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ": ";
        double c,f,x;
        cin >> c >> f >> x;
        double sp = 2;
        double ans = x/sp;
        double q = 0;
        for (int i=0;i<1000000;i++){
            double tmp = c/sp + x/(sp+f) + q;
            ans = min(ans, tmp);
            q += c/sp;
            sp += f;
        }
        cout << ans << endl;
    }
    return 0;
}
