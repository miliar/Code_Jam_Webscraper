#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
using namespace std;
int chr2int (char a) {
    return a - '0';
}
int main() {
    //freopen("a.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int T, Smax;
    string str;
    cin >> T;
    int Sum[1010];
    for(int c = 0; c < T; c++) {
        int ans = 0;
        cout << "Case #" << c + 1 << ": ";
        memset(Sum, 0, sizeof(Sum));
        cin >> Smax >> str;
        Sum[0] = chr2int(str[0]);
        for(int i = 1; i <= Smax; i++) {
            int s = chr2int(str[i]);
            Sum[i] = Sum[i - 1] + s;
            if(i > Sum[i - 1]) {
                ans += (i - Sum[i - 1]);
                Sum[i] += (i - Sum[i - 1]);
            }
        }
        cout << ans << endl;
    }
    return 0;
}
