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
{   freopen("A-small-attempt0.in", "r", stdin);
    freopen("result.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    int a1,a2,i,j,k;
    int matrix1[4][4],matrix2[4][4];
    for(i=1;i<T+1;i++)
    {
        scanf("%d",&a1);
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
                scanf("%d",&matrix1[j][k]);
        }
        scanf("%d",&a2);
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
                scanf("%d",&matrix2[j][k]);
        }
        int ar1[17],ar2[17];
        for(j=0;j<17;j++)
        {
            ar1[j]=0;ar2[j]=0;
        }
        for(j=0;j<4;j++)
            ar1[matrix1[a1-1][j]]=1;
        for(j=0;j<4;j++)
            ar2[matrix2[a2-1][j]]=1;
        int ele,ctr=0;
        for(j=1;j<17;j++)
        {
            if(ar1[j]==1 && ar2[j]==1)
                {ctr++;ele=j;}
        }
        if(ctr==0)
            printf("Case #%d: Volunteer cheated!\n",i);
        else if(ctr==1)
            printf("Case #%d: %d\n",i,ele);
        else
                printf("Case #%d: Bad magician!\n",i);
    }
}
