#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int bx[100];
int f(int a)
{
    for(int i=0;i<8;i++)
        if( bx[i]>= a )
        {
            if(bx[i]==a) return i;
            else return i-1;
        }
}
int main()
{
//    freopen("C-small-attempt0.in","r",stdin);
//    freopen("C-small-attempt0.out","w",stdout);
    bx[0] = 0;
    bx[1] = 1;
    bx[2] = 4;
    bx[3] = 9;
    bx[4] = 121;
    bx[5] = 484;
    bx[6] = 1001;
    int t;scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        printf("Case #%d: %d\n",cas++,f(b)-f(a-1));
    }

    return 0;
}
