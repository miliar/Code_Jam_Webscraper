#include<cstdio>
#include<string.h>
#include<stdlib.h>

main()
{
    freopen("abc.txt","w",stdout);
    int t;
    int h;
    char s[105];
    int ed,stl;
    int k,p;
    int i,j;
    scanf("%d",&t);
    for(h=1;h<=t;h++)
    {
        scanf("%s",s);
        ed=strlen(s)-1;
        stl=strlen(s);
        k=0;
        p=0;
        while(k<stl)
        {
            if(s[ed]=='-')
            {
                for(i=0;i<=ed;i++)
                {
                    if(s[i]=='+')
                    {
                        s[i]='-';
                    }
                    else
                    {
                        s[i]='+';
                    }
                }
                p++;
                //printf("%s\n",s);
            }
            else
            {
                k++;
                ed--;
            }
        }
        printf("Case #%d: %d\n",h,p);
    }
}
