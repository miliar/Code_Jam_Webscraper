#include <cstdlib>
#include <cstdio>

using namespace std;

int use[20];

int main()
{
    int t,x;
    int oo=0;
    scanf("%d",&t);
    while (t--)
    {
        printf("Case #%d: ",++oo);
        int l;
        scanf("%d",&l);
        for (int i=1;i<=4;i++)
        {
            for (int j=1;j<=4;j++)
            {
                scanf("%d",&x);
                if (l==i)
                    use[x]++;
            }
        }
        scanf("%d",&l);
        for (int i=1;i<=4;i++)
        {
            for (int j=1;j<=4;j++)
            {
                scanf("%d",&x);
                if (l==i)
                    use[x]++;
            }
        }
        int ans=0;
        for (int i=1;i<=16;i++)
        {
            if (use[i]==2)
            {
                if (ans==0) ans=i;
                else ans=-1;
            }
            use[i]=0;
        }
        if (ans==0) puts("Volunteer cheated!");
        else if (ans==-1) puts("Bad magician!");
        else printf("%d\n",ans);
    }
    return 0;
}