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



int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {

        int n;
        cin>>n;
        string s;
        cin>>s;

        int tot = 0;
        int need = 0;

        for (int i=0; i<=n; i++) {
            int k = s[i] - '0';

            if (i > tot) {
                int tmp = i - tot;
                tot += tmp;
                need += tmp;
            }

            tot += k;
        }

        printf("Case #%d: %d\n", cas, need);


    }

    return 0;

}
