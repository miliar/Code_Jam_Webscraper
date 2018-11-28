#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int main(void)
{
    freopen("A1.in","r",stdin);
    freopen("A1.out","w",stdout);

    int T;
    scanf("%d",&T);
    int tt;
    char S[10005];
    //Z
    int num[109];
    int i,j;
    for(tt = 1;tt<=T;tt++)
    {
        memset(num,0,sizeof(num));
        scanf("%s",S);
        int len = strlen(S);
        //Z
        for(i = 0;i<len;i++)
        {


            if(S[i]=='Z')
            {
                num[0]++;
            }
            if(S[i]=='W')
            {
                num[2]++;
            }
            if(S[i]=='U')
                num[4]++;
            if(S[i]=='X')
                num[6]++;
            if(S[i]=='G')
                num[8]++;
            if(S[i]=='R')
                num[3]++;
            if(S[i]=='O')
                num[1]++;
            if(S[i]=='F')
                num[5]++;
            if(S[i]=='S')
                num[7]++;
            if(S[i]=='I')
                num[9]++;
        }
        num[1] = num[1]-num[0]-num[4]-num[2];
        num[3] = num[3]-num[0]-num[4];
        num[5] = num[5]-num[4];
        num[7] = num[7]-num[6];
        num[9] = num[9]-num[5]-num[6]-num[8];
        printf("Case #%d: ",tt);
        for(i=0;i<=9;i++)
        {
            for(j=0;j<num[i];j++)
                printf("%d",i);
        }
        printf("\n");
    }
    return 0;
}
