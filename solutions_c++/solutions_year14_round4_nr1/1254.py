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

int a[10010];

int main()
{
    freopen("data_packing.in","r",stdin);
    freopen("data_packing.out","w",stdout);
    int tc, nt=1;
    cin>>tc;
    while (tc--)
    {
        int n, x;
        cin>>n>>x;
        for (int i=0;i<n;i++) scanf("%d", &a[i]);
        sort(a,a+n);
        int ret=0, i=0, j=n-1;
        while (i<=j)
        {
            if (a[j]+a[i]<=x)
            {
                i++;
                j--;
                ret++;
            }
            else if (a[j]<=x)
            {
                j--;
                ret++;
            }
        }
        printf("Case #%d: %d\n", nt++, ret);
    }
}
