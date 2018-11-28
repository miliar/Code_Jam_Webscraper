#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main()
{
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("A-small-attempt0.out","w",stdout);
    int t;
    int a[20];
    int row;
    int tem;
    int flag;
    int ans;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        printf("Case #%d: ", cas);
        flag = 0;
        memset(a,0,sizeof(a));
        scanf("%d",&row);
        for (int i=0;i<16;++i)
        {
            scanf("%d", &tem);
            if (i >= (row-1)*4 && i < row*4)
                a[tem] ++;
        }
        scanf("%d",&row);
        for (int i=0;i<16;++i)
        {
            scanf("%d", &tem);
            if (i >= (row-1)*4 && i < row*4)
                a[tem] ++;
        }
        for (int i=1;i<=16;++i)
            if (a[i] == 2) {flag ++;ans = i;}
        if (flag==0) puts("Volunteer cheated!");
        else if (flag == 1) printf("%d\n", ans);
        else puts("Bad magician!");
    }
}
