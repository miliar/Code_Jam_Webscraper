#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <ctime>
#include <iterator>
#include <utility>
#include <numeric>
#include <functional>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>

using namespace std;

int n;
string a;

int main()
{
    freopen("A-large.in.txt", "r", stdin);
    freopen("A-large.out.txt", "w", stdout);
    int TestCase;
    cin >> TestCase;
    for (int Test = 1; Test <= TestCase; ++Test)
    {
        cin >> n >> a;
        int ans = 0;
        int cnt = 0;
        for (int i = 0; a[i]; cnt += a[i++]-'0')
            if (a[i] && ans+cnt < i)
                ans = max(ans, i-cnt);
        cout << "Case #" << Test << ": " << ans << endl;
    }
    return 0;
}
