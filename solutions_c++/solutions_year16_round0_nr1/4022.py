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
bool flag[10];
int cs = 0;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin>>t;
    while (t--) {
        memset(flag, 0, sizeof(flag));
        cin>>a;
        long long m = a;
        int i = 1;
        int cnt = 0;
        do {
            while (m) {
                if (!flag[m % 10])
                    flag[m % 10] = true, ++cnt;
                m /= 10;
            }
            ++i;
            m = i * a;
        } while (cnt < 10 && i < 2000000);
        printf("Case #%d: ", ++cs);
        if (i == 2000000)
            cout<<"INSOMNIA"<<endl;
        else cout<<(i - 1) * a<<endl;
    }
    return 0;
}
