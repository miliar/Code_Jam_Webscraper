#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int t;
    int cas=1;
   // freopen("C:\\Users\\Defoliate\\Desktop\\input.txt","r",stdin);
    //freopen("C:\\Users\\Defoliate\\Desktop\\output.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        char a[5][5];
        for(int i=0;i<4;i++)
            scanf("%s",a[i]);
        int c=0;
        int dx=0,xd=0,d0=0,od=0;
        int ans=4;
        for(int i=0;i<4;i++)
        {
            int cx=0,co=0;
            int rx=0,ro=0;
            for(int j=0;j<4;j++)
            {
                if(a[i][j]!='.')
                    c++;

                if(a[i][j]=='X')
                    cx++;
                else if(a[i][j]=='O')
                    co++;
                else if(a[i][j]=='T')
                {
                    co++;
                    cx++;
                }

                if(a[j][i]=='X')
                    rx++;
                else if(a[j][i]=='O')
                    ro++;
                else if(a[j][i]=='T')
                {
                    rx++;
                    ro++;
                }
            }
            //ans 1 X   2 O    3Draw   4 incomp

            if(rx==4 || cx==4)
            {
                ans=1;
                goto exit;
            }
            else if (ro==4 || co==4)
            {
                ans=2;
                goto exit;
            }

            if(a[i][i]=='O')
                d0++;
            else if(a[i][i]=='X')
                dx++;
            else if(a[i][i]=='T')
            {
                d0++;
                dx++;
            }

            if(a[i][3-i]=='O')
                od++;
            else if(a[i][3-i]=='X')
                xd++;
            else if(a[i][3-i]=='T')
            {
                xd++;
                od++;
            }
        }
        if(xd==4 || dx==4)
            ans=1;
        else if (d0==4 || od==4)
            ans=2;
        if(c==16)
            ans=3;

        exit:;
        if(ans==1)
            printf("Case #%d: X won\n",cas++);
        else if(ans==2)
            printf("Case #%d: O won\n",cas++);
        else if(ans==3)
            printf("Case #%d: Draw\n",cas++);
        else if(ans==4)
            printf("Case #%d: Game has not completed\n",cas++);

    }
    return 0;
}
