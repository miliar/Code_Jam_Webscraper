#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>


using namespace std;
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("Alarge.txt", "w", stdout);
    int t,sum,ans,smax,j;
    char str[1001];
    cin>>t;
    for(int k = 1;k <= t;k++)
    {
        //j = -1;
        sum = 0;ans = 0;
        cin>>smax;
        cin>>str;
        for(int i = 0; i <= smax; i++)
        {
            if(sum < i)
            {
                ans += (i - sum);
                sum += (i - sum);
            }
            sum += (str[i] - '0');
        }
        cout<<"Case #"<<k<<": "<<ans<<"\n";
    }
    return 0;
}
