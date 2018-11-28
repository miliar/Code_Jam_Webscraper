#include<stdio.h>
int main()
{
    freopen("input6.in","r",stdin);
    freopen("output6.txt","w",stdout);
    int t;
    scanf("%d",&t);
    char ch;
    int l=0;
    scanf("%c",&ch);
 //   fflush(stdin);
    while(l<t)
    {   l++;
        bool fm=0;
        bool prev,now;
        int i=0,npm=0;
        scanf("%c",&ch);
        if(ch=='-')
        {
            prev=0;
            fm=1;
        }
        else prev=1;
        while((ch=getchar())!='\n')
        {
            if(ch=='+') now=1;
            else now=0;
            if(prev==1&&now==0)
            {
                npm++;
            }
            prev=now;
        }
        int ans=fm+2*npm;
        printf("Case #%d: %d\n",l,ans);
    }
    return 0;
}
