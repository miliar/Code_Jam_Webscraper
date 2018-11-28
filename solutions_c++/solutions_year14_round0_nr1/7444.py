#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    FILE *ip, *op;
    ip=freopen("input.txt","r",stdin);
    op=freopen("op.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    int c1, c2;
    int ta, tb, tc, td, ar1[4];
    int te, tf, tg, th, ar2[4];
    for(int i=0;i<t;i++)
    {
        scanf("%d",&c1);
        c1--;
        for(int j=0;j<4;j++)
            {
                scanf("%d %d %d %d",&ta, &tb, &tc, &td);
                if(j==c1)
                {
                    ar1[0]=ta; ar1[1]=tb; ar1[2]=tc; ar1[3]=td;
                }
            }
        scanf("%d",&c2);
        c2--;
        for(int j=0;j<4;j++)
            {
                scanf("%d %d %d %d",&te, &tf, &tg, &th);
                if(j==c2)
                {
                    ar2[0]=te; ar2[1]=tf; ar2[2]=tg; ar2[3]=th;
                }
            }
            int ans=-1;
            bool match=false, error=false;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
                if(ar1[j]==ar2[k])
                {
                    if(!match)
                        {
                            match=true;
                            ans=ar1[j];
                        }
                    else
                        {
                            error=true;
                            break;
                        }
                }
        }
        if(error)
            printf("Case #%d: Bad magician!\n",i+1);
        else if(!match)
            printf("Case #%d: Volunteer cheated!\n",i+1);
        else
            printf("Case #%d: %d\n",i+1, ans);
    }
    fclose(ip);
    fclose(op);
    return 0;
}
