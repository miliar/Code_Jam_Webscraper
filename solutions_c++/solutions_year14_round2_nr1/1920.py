#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <limits.h>
#include <algorithm>
#define LL long long
//#define LL __int64
#define abs(x) ((x)>0?(x):-(x))
#define Ee 2.718281828459045
#define Pi acos(-1.0)
#define eps 1e-10
#define INF 1 << 28
using namespace std;
int min(int a,int b)
{
    if(a>b)a=b;
    return a;
}
int max(int a,int b)
{
    if(a<b)a=b;
    return a;
}
int main()
{
    freopen("A--small-attempt0.in","r",stdin);
    freopen("data.out","w",stdout);

    int t,case1=1;
    scanf("%d",&t);
    char s[105][105];
    while(t--)
    {
        int n;
        scanf("%d",&n);
        for(int i=0; i<n; i++)
        {
            scanf("%s",s[i]);
        }
        int len1=strlen(s[0]);
        int len2=strlen(s[1]);
        int i=0,j=0;
        bool flat=false;
        int cnt1,cnt2,cnt=0;
        while(i<len1&&j<len2)
        {
            if(s[0][i]==s[1][j])
            {
                cnt1=0;
                while(s[0][i]==s[0][i+1])
                {
                    i++;
                    cnt1++;
                }
                cnt2=0;
                while(s[1][j]==s[1][j+1])
                {
                    j++;
                    cnt2++;
                }
                cnt+=abs(cnt1-cnt2);
            }
            else
            {
                break;
            }
            i++;
            j++;
        }
        if(i!=len1||j!=len2)
        {
            printf("Case #%d: Fegla Won\n",case1++);
        }
        else
            printf("Case #%d: %d\n",case1++,cnt);
    }
    return 0;
}
