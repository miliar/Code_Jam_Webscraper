#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <set>
#include <map>
#include <stack>
using namespace std;

int main() {
    freopen("input.txt","r", stdin);
    freopen("output.txt","w",stdout);
    int T;
    double eps = 0.0000000001;
    cin>>T;
    for (int t=1;t<=T;++t) {
        cout<<"Case #"<<t<<": ";
        double c,f,x, ans, base, ans2;
        cin >> c >> f >> x;
        ans = x / 2;
        base = 0;
        for (int i = 1; i < 100000000; ++i) {
            base += c / (2 + f* (i - 1));
            ans2 = base + x / (2 + f * i);
            if (ans2 < ans - eps)
                ans = ans2;
            else
                break;
        }

        cout << fixed << setprecision(7) << ans << endl;
    }
    return 0;
}
