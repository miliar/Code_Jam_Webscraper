#include <fstream>
#include <cstring>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

ifstream cin("date.in");
ofstream cout("date.out");

char s[1010];

int main() {
    int t, nrt = 0;
    cin>>t;
    while (t){
        memset(s, 0, sizeof(s));
        ++nrt;
        --t;
        cout<<"Case #"<<nrt<<": ";
        int k;
        cin>>s>>k;
        int n = strlen(s) - 1;
        int sol = 0;
        for (int i = 0; i <= n; ++i) {
            if (s[i] == '-') {
                if (i + k - 1 > n) {
                    cout<<"IMPOSSIBLE\n";
                    sol = -1;
                    break;
                } else {
                    for (int j = i; j <= i + k - 1; ++j) {
                        if (s[j] == '-') {
                            s[j] = '+';
                        } else {
                            s[j] = '-';
                        }
                    }
                    ++sol;
                }
            }
        }
        if (sol >= 0) {
            cout<<sol<<"\n";
        }
    }
    return 0;
}
