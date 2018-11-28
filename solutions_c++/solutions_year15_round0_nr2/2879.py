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

const int MaxN = 11000;

int n;
int a[MaxN];

int main()
{
    //freopen("B-small-attempt1.in.txt", "r", stdin);
    //freopen("B-small-attempt1.out.txt", "w", stdout);
    freopen("B-large.in.txt", "r", stdin);
    freopen("B-large.out.txt", "w", stdout);
    int TestCase;
    cin >> TestCase;
    for (int Test = 1; Test <= TestCase; ++Test)
    {
        cin >> n;
        int ans = 0x7FFFFFFF;
        for (int i = 0; i < n; cin >> a[i++]);
        sort(a, a+n);
        for (int i = 1; i <= a[n-1]; ++i)
        {
            int overhead = 0;
            for (int j = 0; j < n; ++j)
                overhead += (a[j]+i-1)/i-1;
            ans = min(ans, overhead+i);
        }
        cout << "Case #" << Test << ": " << ans << endl;
    }
    return 0;
}
