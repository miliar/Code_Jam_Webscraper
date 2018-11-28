#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<deque>
#include<bitset>
#include<time.h>
#define ll __int64
#define inf 0x7FFFFFFF
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
int record[500000];
vector<int>dp[4][200000];
int mul[5][5];
void init()
{
    mul[1][1]=1;mul[1][2]=2;mul[1][3]=3;mul[1][4]=4;
    mul[2][1]=2;mul[2][2]=-1;mul[2][3]=4;mul[2][4]=-3;
    mul[3][1]=3;mul[3][2]=-4;mul[3][3]=-1;mul[3][4]=2;
    mul[4][1]=4;mul[4][2]=3;mul[4][3]=-2;mul[4][4]=-1;
}
int cal(int aa, int bb)
{
    int m1=1,m2=1;
    if (aa<0)
    {
        m1=-1;
        aa=-aa;
    }
    if (bb<0)
    {
        m2=-1;
        bb=-bb;
    }
    return m1*m2*mul[aa][bb];
}
int main()
{
    int i,j,k;
    int n,m,t;
    init();
    //srand((unsigned)time(NULL));//int data=rand()%10000+1;
    freopen("C-small-attempt0.in","r",stdin);freopen("C-output-small.txt","w",stdout);
    scanf("%d",&t);for(int tcase=1;tcase<=t;tcase++)
    //while(scanf("%d",&n)!=EOF)
    {
        scanf("%d%d", &n,&m);
        if (m>12)
        {
            m = m-(m-12)/4*4;
        }
        char ch[20005];
        scanf("%s", ch);
        int len = strlen(ch);
        i = 1;
        for (j=1; j<=m; j++)
        {
            for (k=0; k<len; k++)
            {
                if (ch[k]=='i')
                    record[i++] = 2;//[1, i)
                else if (ch[k]=='j')
                    record[i++] = 3;
                else
                    record[i++] = 4;
            }
        }
        len = i;
        for (i=0; i<4; i++)
        for (j=0; j<len; j++)
        {
            dp[i][j].clear();
        }
        dp[0][0].push_back(1);
        for (j=1; j<len; j++)
        {
            for (i=0; i<4; i++)
            {
                if (dp[i][j-1].size()!=0)
                {
                    for (k=0; k<dp[i][j-1].size(); k++)
                    {
                        dp[i][j].push_back(cal(dp[i][j-1][k], record[j]));
                    }
                }
                if (i>0 && dp[i-1][j-1].size()!=0)
                {
                    int judge = 0;
                    for (k=0; k<dp[i-1][j-1].size(); k++)
                    {
                        if (i+1 == cal(dp[i-1][j-1][k], record[j]))
                        {
                            judge = 1;
                            break;
                        }
                    }
                    if (judge == 1)
                    {
                        dp[i][j].push_back(1);
                    }
                }
            }/*
            for (i=0; i<4; i++)
            {
                cout<<"dp["<<i<<"]["<<j<<"] is::";
                for (k=0; k<dp[i][j].size(); k++)
                {
                    cout<<dp[i][j][k]<<" ";
                }
                cout<<endl;
            }*/
        }

        int pan = 0;
        for (k=0; k<dp[3][len-1].size(); k++)
        {
            if (dp[3][len-1][k]==1)
            {
                pan = 1;
                break;
            }
        }
        if (pan == 1)
        {
            printf("Case #%d: YES\n", tcase);
        }
        else
        {
            printf("Case #%d: NO\n", tcase);
        }
    }
}
