#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main () {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        int res = 0;
        int m = 0;
        cin >> m;
        res = m;
        if (res == 0) {
            cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
            continue;
        }
        int a[10];
        memset (a, 0, sizeof(a));
        bool t = false;
        while (!t) {
            int tmp = res;
            while (tmp != 0) {
                a[tmp % 10] = 1;
                tmp = tmp/10;
            }
            bool check = true;
            for (int i=0; i<10; i++){
                if (a[i] == 0) {
                    check = false;
                    break;
                }
            }
            if (check) {
                cout << "Case #" << i+1 << ": " << res << endl;
                t = true;
            } else {
                res += m;
            }
        }
    } 
    return 0;
}
