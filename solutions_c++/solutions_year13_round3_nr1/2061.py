#include<cstdio>
#include<string.h>
#include<cstdlib>
int x[200],mark[105][105],k;
void run()
{
    char str[1005],blank;
    int i=0,n,c=0,a=0,l,ans=0;
    scanf("%c",&blank);
    while(1)
    {
        scanf("%c",&str[i]);
        if(str[i]==' ')
        {
            str[i]='\0';
            break;
        }
        i++;
    }
    scanf("%d",&n);
    l=strlen(str);
    for(int j=0;j<l;j++)
    {
        if(str[j]!='a'&&str[j]!='e'&&str[j]!='i'&&str[j]!='o'&&str[j]!='u')
        {
            c++;
            if(c>=n)
            {
                x[a]=j-n+1;
                a++;
            }
        }
        else
            c=0;
    }

    for(int p=0;p<l;p++)
        for(int q=p+n-1;q<l;q++)
    {
        for(int r=0;r<a;r++)
            if(p<=x[r]&&q>=x[r]+n-1)
            {
                ans+=1;
                break;
            }
    }

    printf("Case #%d: %d\n",k,ans);


}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
        run();
}
