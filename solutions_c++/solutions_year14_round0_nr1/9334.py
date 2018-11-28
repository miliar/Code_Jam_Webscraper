#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int N = 18;

bool va[18],vb[18];

int main()
{
    freopen("A-small-attempt5.in","r",stdin);
    freopen("A-small-attempt5.out","w",stdout);
    int T,a,b,ncase = 0;
    scanf("%d",&T);
    while(T--)
    {
        memset(va,false,sizeof(va));
        memset(vb,false,sizeof(vb));
        scanf("%d",&a);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            {
                int num;
                scanf("%d",&num);
                if(i == a)
                {
                    va[num] = true;
                }
            }
        scanf("%d",&b);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            {
                int num;
                scanf("%d",&num);
                if(i == b)
                {
                    vb[num] = true;
                }
            }
        pair<int,int> ans;
        for(int i=1;i<=16;i++)
            if(va[i] && vb[i])
            {
                ans.first++;
                ans.second = i;
            }
        if(ans.first == 0)
            printf("Case #%d: Volunteer cheated!\n",++ncase);
        else if(ans.first == 1)
            printf("Case #%d: %d\n",++ncase,ans.second);
        else
            printf("Case #%d: Bad magician!\n",++ncase);
    }
    return 0;
}
