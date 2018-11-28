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
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#define ll long long
using namespace std;

int len,ans;
char str[1010];
int sum[1010];
int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("OUT.out","w",stdout);
    int T;
    int Case=1;
    scanf("%d",&T);
    while(T--)
    {
        ans=0;
        scanf("%d",&len);
        scanf("%s",str);
        memset(sum,0,sizeof sum);
        sum[0]=str[0]-'0';
        for(int i=1;i<=len;i++)
        {
            if(sum[i-1]<i)
            {
                ans+=i-sum[i-1];
                sum[i-1]=i;
            }
            sum[i]=sum[i-1]+(str[i]-'0');
        }
        printf("Case #%d: %d\n",Case++,ans);
    }
    return 0;
}

