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
        string input;
        cin >> input;
        int ans = 0;
        for(int i = 1; i < input.size(); i++)
        {
            if(input[i] != input[i - 1])
                ans++;
        }
        if(input[input.size() - 1] == '-')
            ans++;
        cout << "Case #" << cas++ << ": " << ans << endl;
    }
    return 0;
}
