#include <cstdio>
#include <cstring>
using namespace std;
char shy[2005];
int main(void)
{
    int ca,cases;
    int i,j,k;
    int smax;
    int now;
    int needed;
    freopen("A-large.in","r+",stdin);
    freopen("A_large_out.txt","w+",stdout);
    scanf("%d",&cases);
    for (ca=1;ca<=cases;ca++)
    {
        scanf("%d",&smax);
        scanf("%s",shy);
        now=0;
        needed=0;
        for (i=0;i<=smax;i++)
        {
            j=shy[i]-'0';
            if (now<i&&j>0)
            {
                needed+=i-now;
                now=i;
            }
            now+=j;
        }
        printf("Case #%d: %d\n",ca,needed);
    }
    return 0;
}
