#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
int main(int argc, char **argv)
{
    freopen("a.small.in", "r", stdin);
    freopen("a.small.out", "w", stdout);
    ULL T;
    cin >> T;
    ULL imax = 1;
    ULL Nmax = 1;
    for (ULL t = 1; t <= T; ++t) {
        string ans;
        ULL N;
        cin >> N;
        if (N==0) ans = "INSOMNIA";
        else {
            ULL i = 1;
            set<unsigned int> st;
            for (;; ++i) {
                ULL a = N*i;
                while (a) {
                        unsigned int d = a%10;
                        st.insert(d);
                        a /= 10;
                }
                if (st.size() == 10) {
                    break;
                }
            }
            stringstream ss;
            ss << N*i;
            ans = ss.str();
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
