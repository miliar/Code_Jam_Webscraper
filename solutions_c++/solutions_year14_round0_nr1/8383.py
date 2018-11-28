#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
using namespace std;

int main() {
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        int ans, ans1, x;
        scanf("%d", &ans);
        int res[20];
        memset(res, 0, sizeof(res));
        for(int j = 0; j < 4; j++) {
            for(int k = 0; k < 4; k++) {
                cin >> x;
                if(j == ans-1) {
                    ++res[x];
                }
            }
        }
        scanf("%d", &ans1);
        for(int j = 0 ; j < 4; j++) {
            for(int k = 0; k < 4; k++) {
                cin >> x;
                if(j == ans1-1) {
                    ++res[x];
                }
            }
        }
        int ct = 0, r;
        for(int k = 0; k < 17; k++) {
            if(res[k] > 1) {
                    ct++;
                    r = k;
            }
        }
        if(ct == 1) cout << "Case #" << i << ": " <<  r << endl;
        if(ct > 1) cout << "Case #" << i << ": " << "Bad magician!" << endl;
        if(ct == 0) cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;

    }
    return 0;
}
