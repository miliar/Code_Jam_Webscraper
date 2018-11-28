#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;
int re[5][5];
int c[5];
void get()
{
    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        scanf("%d",&re[i][j]);
}
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int cas;
    int T = 1;
    scanf("%d",&cas);
    while(cas--)
    {
        int a,b;
        scanf("%d",&a);
        get();
        for(int i=1;i<=4;i++)
            c[i] = re[a][i];
        scanf("%d",&b);
        get();
        int ans = -1;
        for(int i=1;i<=4;i++)
        {
            int flag = 0;
            for(int j=1;j<=4;j++)
                if(c[i]==re[b][j])
                flag = 1,ans = c[i];
            if(!flag) c[i] = -1;
        }
        int tmp =0 ;
        for(int i=1;i<=4;i++)
            if(c[i]!=-1) tmp++;
        printf("Case #%d: ",T);T++;
        if(tmp==1)
            printf("%d\n",ans);
        else if(tmp==0)
            printf("Volunteer cheated!\n");
        else
            printf("Bad magician!\n");
    }
    return 0;
}
