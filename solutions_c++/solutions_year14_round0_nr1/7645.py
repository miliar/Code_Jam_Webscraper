#include <cstdio>
#include <vector>
#define P 1000000007
#define LL long long
using namespace std;
int a[4],b[4],c[4],tot;
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int cnt,x,y;
    LL n,ans;
    scanf("%d",&cnt);
    for (int run=1;run<=cnt;run++)
    {
        scanf("%d",&x);
        for (int i=0;i<4;i++)
        {
            if (i!=x-1)
                for (int j=0;j<4;j++)
                    scanf("%d",&y);
            else
                for (int j=0;j<4;j++)
                    scanf("%d",a+j);
        }
        scanf("%d",&x);
        for (int i=0;i<4;i++)
        {
            if (i!=x-1)
                for (int j=0;j<4;j++)
                    scanf("%d",&y);
            else
                for (int j=0;j<4;j++)
                    scanf("%d",b+j);
        }
        tot=0;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                if (a[i]==b[j])
                {
                    c[tot++]=a[i];
                    break;
                }
        printf("Case #%d: ",run);
        if (tot==1) printf("%d\n",c[0]);
        else if (tot>1) printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }
    return 0;
}
