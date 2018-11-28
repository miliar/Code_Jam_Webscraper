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
#include <ctime>
#include <string.h>
using namespace std;
int main()
{
    freopen("C:/Users/Mohsin Shiraz/Desktop/C.in","r",stdin);
	freopen("C:/Users/Mohsin Shiraz/Desktop/test.out","w",stdout);
    unsigned long long a[39] = {1, 4, 9,121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
    int i,T,j,count=0;
    unsigned long long m,s;
    scanf("%d",&T);
    for(j=1;j<=T;j++)
    {
        scanf("%llu%llu",&m,&s);
    for(i=0;i<=38;i++)
    {
        if(a[i]>=m && a[i]<=s)
        {
            count++;
        }
    }
     printf("Case #%d: %d\n",j,count);
        count=0;
    }
    return 0;
}
