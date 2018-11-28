#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>
using namespace std;
typedef long long ll;
int a[3][5][5];
int ans1[4];
int ans;
int main()
{
    int t;
    int countt=1;
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        for(int i=0; i<2; i++)
        {
            scanf("%d",&ans1[i]);
            for(int j=0;j<4;j++)
            {
                for(int k=0;k<4;k++)
                    scanf("%d",&a[i][j][k]);
            }
        }
        int cnt=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                {
                    if(a[0][ans1[0]-1][i]==a[1][ans1[1]-1][j])
                    {
                        ans=a[0][ans1[0]-1][i];
                        cnt++;
                    }
                }
        }
        if(cnt==1)
        {
            printf("Case #%d: %d\n",countt,ans);
        }
        else if(cnt>1)
        {
            printf("Case #%d: Bad magician!\n",countt);
        }
        else
        {
            printf("Case #%d: Volunteer cheated!\n",countt);
        }
        countt++;
    }
    return 0;
}
