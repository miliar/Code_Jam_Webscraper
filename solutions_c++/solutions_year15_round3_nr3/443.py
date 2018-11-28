#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
using namespace std;
int C,D,V;
int a[100];
int can[32];
int can2[32];
int main()
{
    freopen("C:\\codejam15\\C-small-attempt0.in","r",stdin);
    freopen("C:\\codejam15\\C-small-attempt0.out","w",stdout);
    int T,cas=1;
    int n,m;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d %d %d",&C,&D,&V);
        for(int i=0;i<D;i++)
            scanf("%d",&a[i]);
        bool ok = false;
        int d = D;
        while(!ok)
        {
            memset(can,0,sizeof(can));
            //memset(can2,0,sizeof(can2));
            can[a[0]] = 1;
            for(int i=1;i<d;i++)
            {
                for(int j=V-1;j>0;j--)
                    if(can[j])
                        can[j+a[i]] = 1;
                can[a[i]] = 1;
            }
            int cur = -1;
            for(int i=1;i<=V;i++)
                if(!can[i]){
                    cur = i;
                    break;
                }
            if(cur == -1)
                ok = true;
            else a[d++] = cur;
        }
        printf("Case #%d: %d\n",cas++,d-D);
    }
    return 0;
}
