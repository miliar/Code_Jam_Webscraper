/* @coder: Sidharth Gupta */

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>


#define MOD 109546051211ll
#define MIN(a,b) ((a)>(b)?(b):(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) MAX(a,-(a))
#define SET(a,b) memset(a, b, sizeof(a))
#define EVEN(a) ((a&1)==0)
#define SQR(a) ((a)*(a))
#define EPS 0.0001

typedef long long int lli;
typedef unsigned long long int llui;
typedef unsigned int uint;

using namespace std;

int main() {

    int t, T;
    char s[2005];
    int mp[30];

    scanf("%d", &T);

    for(t=1;t<=T;++t) {
        SET(mp, 0);

        scanf("%s", s);
        for(int i=0;s[i];++i) {
            ++mp[s[i]-'A'];
        }

        string ans = "";
        int a[10] = {0};

        a[0] = mp['Z'-'A'];
        mp['E'-'A'] -= mp['Z'-'A']; mp['R'-'A'] -= mp['Z'-'A']; mp['O'-'A'] -= mp['Z'-'A'];

        a[2] = mp['W'-'A'];
        mp['T'-'A'] -= mp['W'-'A']; mp['O'-'A'] -= mp['W'-'A'];

        a[6] = mp['X'-'A'];
        mp['S'-'A'] -= mp['X'-'A']; mp['I'-'A'] -= mp['X'-'A'];

        a[8] = mp['G'-'A'];
        mp['E'-'A'] -= mp['G'-'A'];
        mp['I'-'A'] -= mp['G'-'A'];
        mp['H'-'A'] -= mp['G'-'A'];
        mp['T'-'A'] -= mp['G'-'A'];

        a[7] = mp['S'-'A'];
        mp['E'-'A'] -= mp['S'-'A'];
        mp['E'-'A'] -= mp['S'-'A'];
        mp['V'-'A'] -= mp['S'-'A'];
        mp['N'-'A'] -= mp['S'-'A'];

        a[5] = mp['V'-'A'];
        mp['F'-'A'] -= mp['V'-'A'];
        mp['I'-'A'] -= mp['V'-'A'];
        mp['E'-'A'] -= mp['V'-'A'];

        a[4] = mp['U'-'A'];
        mp['F'-'A'] -= mp['U'-'A'];
        mp['O'-'A'] -= mp['U'-'A'];
        mp['R'-'A'] -= mp['U'-'A'];

        a[1] = mp['O'-'A'];
        mp['N'-'A'] -= mp['O'-'A'];
        mp['E'-'A'] -= mp['O'-'A'];

        a[9] = mp['I'-'A'];
        mp['N'-'A'] -= mp['I'-'A'];
        mp['N'-'A'] -= mp['I'-'A'];
        mp['E'-'A'] -= mp['I'-'A'];

        a[3] = mp['T'-'A'];

        for(int i=0;i<=9;++i) {
            for(int j=0;j<a[i];++j) {
                ans += (char)((int)('0')+i);
            }
        }

        printf("Case #%d: ", t);
        cout << ans;
        if(t!=T) printf("\n");
    }

    return 0;
}
