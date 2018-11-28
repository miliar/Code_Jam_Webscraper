#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<ctime>
#include<cctype>
#include<cmath>
#include<string>
#include<cstring>
#include<stack>
#include<queue>
#include<vector>
#include<map>
#define sqr(x) ((x)*(x))
#define LL long long
#define INF 0x3f3f3f3f
#define PI 3.14159265358979
#define eps 1e-10
#define mm

using namespace std;

int first[4][4];
int second[4][4];
bool isans1[17],isans2[17];

int r,tt,t,cnt;

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("t","r",stdin);
		freopen("t1","w",stdout);
	#endif

	scanf("%d",&tt);
	t=0;

	while (tt--)
    {
        t++;
        memset(isans1,false,sizeof(isans1));
        memset(isans2,false,sizeof(isans2));

        scanf("%d",&r);
        for (int i=0;i<4;i++)
        {
            for (int j=0;j<4;j++)
            {
                scanf("%d",&first[i][j]);
            }
        }

        for (int i=0;i<4;i++)
        {
            isans1[first[r-1][i]]=true;
        }

        scanf("%d",&r);
        for (int i=0;i<4;i++)
        {
            for (int j=0;j<4;j++)
            {
                scanf("%d",&second[i][j]);
            }
        }

        for (int i=0;i<4;i++)
        {
            isans2[second[r-1][i]]=true;
        }

        cnt=0;

        for (int i=1;i<17;i++)
        {
            if (isans1[i]&&isans2[i])
            {
                cnt++;
            }
        }

        if (cnt==1)
        {
            for (int i=1;i<17;i++)
            {
                if (isans1[i]&&isans2[i])
                {
                    printf("Case #%d: %d\n",t,i);
                }
            }
        }
        else
        {
            if (cnt==0)
            {
                printf("Case #%d: Volunteer cheated!\n",t);
            }
            else
            {
                printf("Case #%d: Bad magician!\n",t);
            }
        }
    }


	return 0;
}
