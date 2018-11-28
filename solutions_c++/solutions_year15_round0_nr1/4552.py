#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const int MAXN = 2000;
int shy[MAXN];

int main() {
    int tc;
    cin >> tc;
    for(int ii=1;ii<=tc;++ii) {
        memset(shy, 0, sizeof(shy));
        int S;
        string cnt;
        cin >> S >> cnt;

        for(int i=0;i<cnt.size();++i)
            shy[i] = cnt[i]-'0';

        int ans = 0;
        int standing = 0;
        for(int i=0;i<cnt.size();++i) {
            if(standing < i) {
                ans += i-standing;
                standing = i;
            }
            standing += shy[i];
        }

        cout << "Case #" << ii << ": " << ans << "\n";
    }
    return 0;
}
