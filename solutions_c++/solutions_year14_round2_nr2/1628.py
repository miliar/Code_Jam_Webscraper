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
{   freopen("B-small-attempt0.in", "r", stdin);
    freopen("result.txt", "w", stdout);
    int T,A,B,K;
    scanf("%d",&T);
    int i,j,k;
    for(i=1;i<T+1;i++)
    {
        scanf("%d %d %d",&A,&B,&K);
        int ctr=0;
        for(j=0;j<A;j++)
        {
            for(k=0;k<B;k++)
            {
                if((j&k)<K)
                    ctr++;
            }
        }
        printf("Case #%d: %d\n",i,ctr);
    }
}
