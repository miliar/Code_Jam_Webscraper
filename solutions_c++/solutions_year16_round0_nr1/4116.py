#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define eps 1e-9
#define PB push_back
#define LL long long
#define INF 0x3f3f3f3f

template<class T> void checkMax(T &a, T b)
{
    a = max(a, b);
}
template<class T> void checkMin(T &a, T b)
{
    a = min(a, b);
}

int main()
{
    int t, cas = 1;
    cin >> t;
    while(t--)
    {
        int n, vis[10] = {0}, cnt = 0;
        cin >> n;
        if(n != 0)
        {
            LL ans = 0;
            while(cnt != 10)
            {
                ans += n;
                LL temp = ans;
                while(temp)
                {
                    if(vis[temp % 10] == 0) cnt++;
                    vis[temp % 10] = 1;
                    temp /= 10;
                }
            }
            cout << "Case #" << cas++ << ": " << ans << endl;
        }
        else
        {
            cout << "Case #" << cas++ << ": INSOMNIA" << endl;
        }
    }
    return 0;
}
