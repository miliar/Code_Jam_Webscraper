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
{   freopen("A-large.in", "r", stdin);
    freopen("result.txt", "w", stdout);
    int i,j,T,num;
    scanf("%d",&T);
    char str[1005];
    for(i=1;i<T+1;i++)
    {
    scanf("%d %s",&num,str);
    int mx=0;
    int p1=0,p2=0;
    for(j=0;j<num+1;j++)
    {
    p2=(str[j]-'0');
    mx=max(mx,j-p1);
    p1+=p2;
    }
    printf("Case #%d: %d\n",i,mx);
    }
}
