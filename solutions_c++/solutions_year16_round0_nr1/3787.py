#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <cmath>
using namespace std;
bool pd[10];
int T;
int main()
{
//    freopen("A1in.txt","r",stdin);
//    freopen("A1out.txt","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;++i)
    {
        int size = 0;
        memset(pd,0,sizeof(pd));
        int x,y;
        scanf("%d",&x);
        //y = x;
        int ans = x;
        for(int j=1;j<=100;++j)
        {
            y = x*j;
            ans = y;
            while(y)
            {
                int z = y % 10;
                if(!pd[z])
                {
                    pd[z]=true;
                    ++size;
                }
                if(size==10)break;
                y/=10;
            }
            if(size==10)break;
        }
        if(size==10)
        {
            printf("Case #%d: %d\n",i,ans);
        }else
        {
            printf("Case #%d: INSOMNIA\n",i);
        }
    }
    return 0;
}