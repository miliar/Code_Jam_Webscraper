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
    freopen("outsmall00.txt", "w", stdout);
    int T,t,a1,a2,a[5][5],b[5][5],i,j,c,k;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&a1);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            scanf("%d",&a[i][j]);
        scanf("%d",&a2);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            scanf("%d",&b[i][j]);
        c=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a[a1][i]==b[a2][j])
                    {
                        c++;
                        k=a[a1][i];
                    }
            }
        }
        printf("Case #%d: ",t);
        if(c==1)
            printf("%d\n",k);
        else if(c==0)
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
    }
    return 0;
}
