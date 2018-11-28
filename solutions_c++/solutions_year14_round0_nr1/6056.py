#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <stack>
#include <bitset>
#include <string>
#include <set>
#include <queue>

using namespace std;
#define i64 long long

int a[4][4],b[4][4];
int x,y;
map<int,int> mp;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int i,j,cases,k,found=0,fn;

    scanf("%d",&cases);
    //printf("%d\n",cases);

    for(k=1;k<=cases;++k)
    {
        mp.clear();
        found=0;
        scanf("%d",&x);
        --x;
        for(i=0;i<4;++i)
        {
            for(j=0;j<4;++j)
            {
                scanf("%d",&a[i][j]);
            }
        }

        scanf("%d",&y);
        --y;
        for(i=0;i<4;++i)
        {
            for(j=0;j<4;++j)
            {
                scanf("%d",&b[i][j]);
            }
        }

        for(i=0;i<4;++i)
        {
            if(!mp[a[x][i]])
            {
                ++mp[a[x][i]];
            }
        }

        for(i=0;i<4;++i)
        {
            if(mp[b[y][i]]==1)
            {
                ++found;
                ++mp[b[y][i]];
                fn=b[y][i];
            }
        }

        if(found==0)
        {
            printf("Case #%d: Volunteer cheated!\n",k);
        }
        else if(found==1)
        {
            printf("Case #%d: %d\n",k,fn);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",k);
        }
    }


    return 0;
}

