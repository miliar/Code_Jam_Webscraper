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
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;
typedef long long LL;

int main()
{
    freopen("cookie_clicker_alpha.in","r",stdin);
    freopen("cookie_clicker_alpha.out","w",stdout);
    int tc, nt=1;
    cin>>tc;
    while (tc--)
    {
        double c, f, x, rate=2, ret=1000000000, cur_t=0;
        cin>>c>>f>>x;
        int mx=(int)x/c+1;
        for (int i=0;i<=mx;i++)
        {
            double t=x*1./rate;
            ret=min(ret,cur_t+t);
            cur_t+=c*1./rate;
            rate+=f;
        }
        printf("Case #%d: %.7lf\n", nt++, ret);
    }
}
