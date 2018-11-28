#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int n,i=1,j,k,max,p,con,cnt,m;
    char st[8];
    scanf("%d",&n);
    while(i<=n)
    {
        p=0;
        cnt=0;
        con=0;
        m=0;
        scanf("%d",&max);
        scanf("%s",st);
        m=st[0]-'0';
        for(j=1; st[j]; j++)
        {
            cnt=(st[j]-'0');
            if(cnt!=0)
            {
                if(m>=j)
                {
                    con=m+cnt;
                    m=con;
                }
                else
                {
                    p+=j-m;
                    m=m+p+cnt;
                }
            }
        }
        printf("Case #%d: %d\n",i,p);
        i++;
    }
    return 0;
}
