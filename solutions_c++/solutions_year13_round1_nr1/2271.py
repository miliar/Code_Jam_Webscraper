#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T = 0;
    cin >> T;
    for (int i = 0; i < T; i++) {
        long long r = 0, 
                  t = 0;
        cin >> r >> t;
        long long total = 0,
                  common_radius = r;
        bool black = true;
        while (t > 0) {
            if (black) {
                long long square = (common_radius+1)*(common_radius+1) - (common_radius*common_radius);
                t -= square;
                if (t >= 0)
                    total++;
            }
            black = !black;
            common_radius++;
        }
        cout << "Case #" << i+1 << ": " << total << endl;
    }
    return 0;
}

