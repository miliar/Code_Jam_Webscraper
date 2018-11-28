#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int *arr = new int[1000];
    string s;
    int t, smax, i, j, k, ans, acount;
    cin >> t;
    for(i=0; i<t; ++i) {
        for(j=0; j<6; ++j) {
            arr[j] = 0;
        }
        smax = 0;
        cin >> smax;
        cin >> s;
        for(j=0; j<=smax; ++j) {
            arr[j] = s[j] - '0';
        }
        ans = 0;
        acount = 0;
        for(k=0; k<=smax; k++) {
            if (arr[k] == 0) {
                continue;
            }
            else if(acount >= k) {
                acount += arr[k];
            }
            else {
                ans += k-acount;
                acount += arr[k]+k-acount;;
            }
        }
        cout << "Case #" << i+1 << ": " << ans << '\n';
    }
    delete[] arr;
    return 0;
}
