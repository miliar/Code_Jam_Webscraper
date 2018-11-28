#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    freopen("/Users/pfctgeorge/Documents/Programs/Google Code Jam 2015 Qualification/A.txt","r",stdin);
    freopen("/Users/pfctgeorge/Documents/Programs/Google Code Jam 2015 Qualification/A.out","w",stdout);
    int T;
    cin >> T;
    int ca = 0;
    while (T--) {
        int sm;
        string s;
        cin >> sm;
        cin >> s;
        for (int i = 0; i <= 100005; i++) {
            int now = i;
            bool flag = true;
            for (int j = 0; j < s.size(); j++) {
                if (now >= j) {
                    now += s[j] - '0';
                } else {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                cout << "Case #" << ++ca << ": " << i << endl;
                break;
            }
        }
    }
}