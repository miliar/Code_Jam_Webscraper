#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int
main(void)
{
    int T;
    int N, M;
    int t, i, j;
    int height[100][100];
    int v[100], h[100];

    cin >> T;

    for(t=1;t<=T;t++) {
        cin >> N >> M;
        for(i=0;i<100;i++) {
            v[i] = h[i] = 0;
        }
        for(i=0;i<N;i++) {
            for(j=0;j<M;j++) {
                cin >> height[i][j];
                v[i] = max(v[i], height[i][j]);
                h[j] = max(h[j], height[i][j]);
            }
        }
        bool flg = true;
        for(i=0;i<N;i++) {
            for(j=0;j<M;j++) {
                if (height[i][j] != min(v[i],h[j])) {
                    flg = false;
                }
            }
        }

        cout << "Case #" << t << ": " << (flg ? "YES" : "NO")  << endl;
    }
    
    return 0;
}
