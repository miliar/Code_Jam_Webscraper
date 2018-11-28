#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <cstdio>
#include <ctime>

using namespace std;


bool used[10000][10000];

int main(int argc, char **argv){
    freopen("/Users/Arseniy/All/Int/input.txt", "r", stdin);
    freopen("/Users/Arseniy/All/Int/int/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o=0;o<t;o++){
        int r, c, n;
        cout << "Case #" << o+1 <<": ";
        cin >> r >> c >> n;
        int ans = 4*r*c;
        for (int q = 0; q < (1 << (r*c)); q++){
            int m = 0;
            for (int i=0;i<r;i++)
                for (int j=0;j<c;j++){
                    if ((q >> (i*c+j)) & 1){
                        used[i][j] = true;
                        m++;
                    }else
                        used[i][j] = false;
                }
            if (m != n){
                continue;
            }
            int tmp = 0;
            for (int i=0;i<r;i++)
                for (int j=0;j<c;j++){
                    if (used[i][j]){
                        if ((j < c-1) && (used[i][j+1]))
                            tmp++;
                        if ((j > 0) && (used[i][j-1]))
                            tmp++;
                        if ((i > 0) && (used[i-1][j]))
                            tmp++;
                        if ((i < r-1) && (used[i+1][j]))
                            tmp++;
                    }
                }
            tmp /=2;
            ans = min(ans, tmp);
        }
        
        cout << ans << endl;
    }

    return 0;
}