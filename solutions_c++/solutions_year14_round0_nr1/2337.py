
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
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <stdint.h>

using namespace std;
#define LL_max 200000000000
#define mod 1000000007

#define LL long long
#define mp make_pair
#define pb push_back

int main()
{
    int t,ans1,ans2,a[4][4],b[4][4],fl,gl,ans,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        ++ca;
        fl=1;
        gl=1;
        scanf("%d",&ans1);
        ans1--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&ans2);
        ans2--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&b[i][j]);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a[ans1][i]==b[ans2][j]&&fl)
                {
                    ans=a[ans1][i];
                    fl=0;
                }
                else if(a[ans1][i]==b[ans2][j]&&!fl)
                {
                    printf("Case #%d: Bad magician!\n",ca);
                    gl=0;
                    break;
                }
            }
            if(!gl)
                break;
        }
        if(!fl&&gl)
            printf("Case #%d: %d\n",ca,ans);
        else if(gl)
            printf("Case #%d: Volunteer cheated!\n",ca);
        else if(fl&&gl)
            continue;

    }
    return 0;
}
