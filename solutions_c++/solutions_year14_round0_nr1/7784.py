#include <stdio.h>

using namespace std;

int chk[20]={0};
int main()
{
    int T;
    scanf("%d",&T);
    for(int k=1;k<=T;k++)
    {
        for(int i=0;i<=16;i++) chk[i]=0;
        int a,b;
        scanf("%d",&a);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&b);
                if(i==a) chk[b]++;
            }
        }
        scanf("%d",&a);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&b);
                if(i==a) chk[b]++;
            }
        }
        int cnt=0;
        for(int i=1;i<=16;i++) if(chk[i]==2) cnt++;
        if(cnt==0) printf("Case #%d: Volunteer cheated!\n",k);
        else if(cnt>1) printf("Case #%d: Bad magician!\n",k);
        else {for(int i=1;i<=16;i++) if(chk[i]==2) printf("Case #%d: %d\n",k,i);}

    }
    return 0;
}
