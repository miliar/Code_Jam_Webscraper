#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;

const inline int __GET_INT(){int ret;scanf("%d",&ret);return ret;}
#define INPT_INT __GET_INT()

typedef long long LL;

int a[10005];
bool taken[10005];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int caseCnt = INPT_INT;

    for(int cNo = 1;cNo<=caseCnt;++cNo)
    {
        int N = INPT_INT, X = INPT_INT;

        for(int i = 0;i<N;++i) a[i] = INPT_INT;

        sort(a,a+N);

        int res = 0;
        memset(taken,0,sizeof(taken));

        for(int i = N-1;i>=0;--i) if(!taken[i])
        {
            ++res;
            taken[i] = true;

            for(int j = i-1;j>=0;--j) if(!taken[j] && a[i]+a[j]<=X)
            {
                taken[j] = true; break;
            }
        }

        printf("Case #%d: ",cNo);
        printf("%d\n",res);
    }
    return 0;
}
