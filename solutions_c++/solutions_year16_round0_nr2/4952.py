#include <cstdio>
#include <cstring>
int t;
char ch[123];
int b[123];
int as=0;
int val(int a,int b)
{
    if(b==0) return a;
    else return 1-a;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen ("out.out","w",stdout);
    scanf("%d",&t);
    for(int xyz=1;xyz<=t;xyz++)
    {
        int as=0;
        int ct=0;
        printf("Case #%d: ",xyz);
        scanf("%s",ch);
        int n=strlen(ch);
        for(int i=0;i<n;i++)
        {
            if(ch[i]=='-') b[i+1]=1;
            else b[i+1]=0;
        }
        for(int i=n;i>=1;i--)
        {
            if(val(b[i],as)==1)
            {
                as=1-as;
                ++ct;
            }
        }
        printf("%d\n",ct);
    }
}
