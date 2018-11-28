#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

int main()
{
    //fflush(stdin);
    freopen("tic4.txt","r",stdin);
    freopen("final5.txt","w",stdout);
    int i,j,k,m=0,x=0,y=0,t=0,dot=0,T,flag=-1;
    char tic[4][4],c;

    scanf("%d",&T);
    scanf("%c",&c);
    for(i=1;i<=T;i++)
    {
        x=0; y=0; t=0; dot=0;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
                scanf("%c",&tic[j][k]);
            scanf("%c",&c);
        }

        if(flag==-1 && dot>0)
        {
            printf("Case #%d: Game has not completed\n",i);
        }
        else if(flag==-1 && dot==0)
        {
            printf("Case #%d: Draw\n",i);
        }
        scanf("%c",&c);
    }
    return 0;
}
