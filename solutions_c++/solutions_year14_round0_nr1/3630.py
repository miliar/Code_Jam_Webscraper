#include<cstdio>
using namespace std;
int cnt[20];
int main()
{
    int tc,t;
    freopen("A-small-attempt1.in","r",stdin);
    scanf("%d",&tc);
    for(t = 1 ; t<=tc ; t++)
    {
        int i,j,a,x;
        //int cnt[20] = {0};
        for(i = 1 ; i<18 ; i++)
        cnt[i] = 0;

        scanf("%d",&a);
        for(i = 1 ; i<=4 ; i++)
        {
            for(j = 1 ; j<=4 ; j++)
            {
                scanf("%d",&x);
                if(i == a)
                cnt[x]++;
            }
        }
        scanf("%d",&a);
        for(i = 1 ; i<=4 ; i++)
        {
            for(j = 1 ; j<=4 ; j++)
            {
                scanf("%d",&x);
                if(i == a)
                cnt[x]++;
            }
        }
        int c = 0;
        for(i = 1 ; i<=16 ; i++)
        {
            if(cnt[i] == 2)
            {
                c++;
                a = i;
            }
        }
        printf("Case #%d: ",t);
        if(c == 0) printf("Volunteer cheated!\n");
        else if(c == 1) printf("%d\n",a);
        else printf("Bad magician!\n");
    }
    return 0;
}
