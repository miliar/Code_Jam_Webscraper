#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int T;
int h[17];

int main () {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("ret.out","w",stdout);
    cin >> T;
    for (int i = 1;i <= T;i ++) {
        memset(h,0,sizeof(h));
        int a , t;
        cin >> a;
        for (int j = 1;j <= 4;j ++)
            for (int k = 1;k <= 4;k ++) {
                cin >> t;
                if (a == j) h[t] ++;
            }
        cin >> a;
        for (int j = 1;j <= 4;j ++)
            for (int k = 1;k <= 4;k ++) {
                cin >> t;
                if (a == j) h[t] ++;
            }
        int ret = 0;
        for (int j = 1;j <= 16;j ++)
            if (h[j] > 1) ret ++;
        cout << "Case #" << i << ": ";
        if (!ret) cout << "Volunteer cheated!" << endl;
        if (ret == 1) {
           for (int j = 1;j <= 16;j ++)
               if (h[j] == 2) cout << j << endl;   
        }
        if (ret > 1) cout << "Bad magician!" << endl;
    }
    return 0;
}
