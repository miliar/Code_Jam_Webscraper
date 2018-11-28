#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

int main()
{
//    freopen("input.txt", "r", stdin);
//    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        int n;
        cin >> n;
        int n0 = n;

        cout << "Case #" << t << ": ";
        if(n == 0) {
            cout << "INSOMNIA";
        } else {
            int l = 10;
            vector< bool > notFound(10, true);
            int iter = 0;
            while(true) {
                int x = n;
                while(x) {
                    int d = x % 10;
                    x /= 10;
                    if(notFound[d]) {
                        --l;
                        notFound[d] = false;
                    }
                }
                if(!l) {
                    break;
                }
                n += n0;
                ++iter;
                if(iter >= 10000) {
                    cerr << n0 << endl;
                    return 0;
                }
            }
            cout << n;
        }
        cout << endl;
    }

    return 0;
}
