#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;



int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cas=0;
    int T;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d: ",++cas);
        int i,a,b,d,f[20];
        memset(f,0,sizeof(f));
        scanf("%d",&a);
        for(i=1;i<=16;i++)
        {
            scanf("%d",&d);
            if(i>(a-1)*4&&i<=a*4)
            {
                f[d]++;
            }
        }
        scanf("%d",&b);
        for(i=1;i<=16;i++)
        {
            scanf("%d",&d);
            if(i>(b-1)*4&&i<=b*4)
            {
                f[d]++;
            }
        }
        int fl=0,xx=0;
        for(i=1;i<=16;i++)
        {
            if(f[i]==2)
            {
                fl++;
                xx=i;
            }
        }
        if(fl==0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(fl==1)
        {
            printf("%d\n",xx);
        }
        else
        {
            printf("Bad magician!\n");
        }
    }





    fclose(stdin);
    fclose(stdout);


    return 0;
}