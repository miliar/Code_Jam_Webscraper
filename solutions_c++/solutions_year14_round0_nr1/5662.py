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
#define ll __int64
#define inf 0x7FFFFFFF
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
int main()
{
    int i,j,k;
    int n,m,t;
    int a[20];
    freopen("A-small-attempt0.in","r",stdin);freopen("A-output.txt","w",stdout);
    scanf("%d",&t);for(int tcase=1;tcase<=t;tcase++)
    //while(scanf("%d",&n)!=EOF)
    {
        memset(a,0,sizeof(a));
        scanf("%d",&n);
        for(i=1;i<=4;i++)
        {
            int x,y,z,o;
            scanf("%d%d%d%d",&x,&y,&z,&o);
            if(i==n)
            {
                a[x]+=1;a[y]+=1;a[z]+=1;a[o]+=1;
            }
        }
        scanf("%d",&n);
        for(i=1;i<=4;i++)
        {
            int x,y,z,o;
            scanf("%d%d%d%d",&x,&y,&z,&o);
            if(i==n)
            {
                a[x]+=1;a[y]+=1;a[z]+=1;a[o]+=1;
            }
        }
        int judge=0;
        int get;
        for(i=1;i<=16;i++)
        {
            if(a[i]==2)
            {
                judge++;
                get=i;
            }
        }
        printf("Case #%d: ",tcase);
        if(judge==0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(judge>1)
        {
            printf("Bad magician!\n");
        }
        else
        {
            printf("%d\n",get);
        }
    }
    fclose(stdin);
    fclose(stdout);
}
