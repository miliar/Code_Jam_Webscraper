#include<cstdio>
#include<cstring>


int t;
char s[110];
int val[110],p;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    scanf("%d",&t);

    for(int i=1;i<=t;i++)
    {
        scanf("%s",&s);
        int len=strlen(s);
        for(int j=0;j<len;j++)
        {
            val[j]=0;
        }
        if(s[0]=='-')
        {
            val[0]=1;
        }
        p=0;
        for(int j=1;j<len;j++)
        {
            if(s[j]=='+')
            {
                val[j]=val[j-1];
            }
            else
            {
                if(s[j-1]=='-')
                {
                    val[j]=val[j-1];
                }
                else
                {
                    val[j]=val[p]+2;
                }
                p=j;
            }
        }
        printf("Case #%d: %d\n",i,val[len-1]);
    }
}
