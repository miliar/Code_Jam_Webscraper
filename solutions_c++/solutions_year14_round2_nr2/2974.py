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
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("outsmall00.txt", "w", stdout);
    int T,t,A,B,K,i,j,c;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d%d%d",&A,&B,&K);
        c=0;
        for(i=0;i<A;i++)
        {
            for(j=0;j<B;j++)
            {
                if((i&j)<K)
                    c++;
            }
        }
        printf("Case #%d: %d\n",t,c);
    }
    return 0;
}
