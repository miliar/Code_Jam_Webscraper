#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <limits>
#include <algorithm>
#include <ctime>
#include <cstring>

using namespace std;

const int MAXV = 10000;
long long a;
char s[10000];
int cs = 0;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    cin>>t;
    while (t--) {
        cin>>s;
        int n = strlen(s);
        bool flag = false;
        int ans = 0;
        for (int i = n - 1; i >= 0; --i) {
            if ((s[i] == '-') ^ flag) {
                ++ans;
                flag ^= true;
            }
        }


        printf("Case #%d: ", ++cs);
        cout<<ans<<endl;
    }
    return 0;
}
