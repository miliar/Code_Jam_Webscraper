#include <iostream>
#include <cstdio>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

#define i64 long long

struct node
{
    int a[5][5];
    int row;


    void get()
    {
        scanf("%d",&row);
        int i,j;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
    }
};


node a,b;


int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    int i;
    for(i=1;i<=T;i++)
    {
        a.get();
        b.get();
        int j,k;
        int cnt=0,ans;
        for(j=1;j<=4;j++)
        {
            for(k=1;k<=4;k++)
            {
                if(a.a[a.row][j]==b.a[b.row][k])
                {
                    cnt++;
                    ans=a.a[a.row][j];
                    break;
                }
            }
        }
        printf("Case #%d: ",i);
        if(1==cnt) printf("%d\n",ans);
        else if(0==cnt) puts("Volunteer cheated!");
        else puts("Bad magician!");
    }
}




