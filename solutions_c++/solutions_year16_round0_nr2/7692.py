#include<stdio.h>
#include<string.h>
char a[115];
void flip(int j)
{
    int i;
    for(i=0;i<=j;i++)
    {
        if(a[i]=='+')
            a[i]='-';
        else
            a[i]='+';
    }
}
int main()
{
    int T,p=1;
    scanf("%d",&T);
    while(T--)
    {

        int i,j,l,ans=0;
        scanf("%s",&a);
        l=strlen(a);
        for(i=l-1;i>=0;i--)
        {
            if(a[i]=='-')
            {
                ans++;
                flip(i);
            }
        }
        printf("Case #%d: %d\n",p,ans);
        p++;
    }
}
