#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

int cnt[3];
int tot[3];
int v[5000][2];
int m, n;

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {

        cin>>n;
        m = 1<<n;
        for (int i=0; i<3; i++) cin>>cnt[i];

        bool found = 0;
        string s = "";

        for (int i=0; i<3; i++) {

            for (int j=0; j<3; j++) {
                tot[j] = 0;
            }

            v[0][0] = i;
            for (int j=1; j<=n; j++) {

                for (int k=0; k<(1<<(j-1)); k++) {

                    v[2*k][1] = v[k][0];
                    v[2*k+1][1] = (v[k][0]+1)%3;

                }

                for (int k=0; k<(1<<(j)); k++) {
                    v[k][0] = v[k][1];
                }

            }

            for (int j=0; j<m; j++) tot[v[j][0]]++;

            bool good = true;
            for (int j=0; j<3; j++) if (cnt[j] != tot[j]) {
                good = 0;
            }

            if (good) {

                string str = "";
                str.resize(m);

                for (int j=0; j<m; j++) {
                    if (v[j][0]==0) {
                        str[j] = 'R';
                    }
                    if (v[j][0]==1) {
                        str[j] = 'P';
                    }
                    if (v[j][0]==2) {
                        str[j] = 'S';
                    }
                }

                //cout<<i<<" "<<str<<endl;

                for (int j=1; j<=n; j++) {

                    int len = (1<<j);

                    for (int k=0; k<m; k+=len) {

                        string l = str.substr(k, len/2);
                        string r = str.substr(k+len/2, len/2);

                        //cout<<i<<" "<<l<<" "<<r<<endl;

                        if (l > r) {
                            str = str.substr(0, k) + r + l + str.substr(k+len, m-k-len);
                        }

                    }

                }

                if (!found) {
                    found = 1;
                    s = str;
                }
                else if (s > str) {
                    s = str;
                }

            }

        }

        if (!found) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
        }
        else {
            printf("Case #%d: %s\n", cas, s.c_str());
        }

    }

    return 0;

}
