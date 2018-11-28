#include<cstdio>
#include<cstring>
char c[102],tmp[102];
int main()
{
    int t,n,chk,k;
    int ans=0;
    scanf("%d",&t);
    for(int tcase=1; tcase<=t; tcase++)
    {
        scanf("%s",c);
        n=strlen(c);
        for(int i=0;i<n;i++) tmp[i]=c[i];
        k=n-1;
        ans=0;
        while(1)
        {
            chk=0;
            for(int i=k; i>=0; i--)
            {
                if(c[i]=='-')
                {
                    chk=1;
                    break;
                }
                else k--;
            }
            if(chk==0)
                break;
            else
            {
                ans++;
                int p=-1;
                for(int i=0;i<=k;i++)
                {
                    if(c[i]=='+') p=i;
                    else break;
                }
                if(p!=-1)
                {
                    for(int i=0;i<=p;i++)
                        tmp[i]='-';
                    ans++;
                }
                for(int i=0;i<=k;i++)
                {
                    if(tmp[k-i]=='-')
                    c[i]='+';
                    else c[i]='-';
                }
                for(int i=0;i<=k;i++) tmp[i]=c[i];

            }
        }
        printf("Case #%d: %d\n",tcase,ans);
    }
    return 0;
}
