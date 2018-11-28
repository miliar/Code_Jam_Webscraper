#include <stdio.h>
#include <string.h>
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    char ch[1005],in[5000];
    int number,cas=1,test;
    gets(ch);
    sscanf(ch,"%d",&test);
    while(test--)
    {
        gets(in);
        sscanf(in,"%d %s",&number,ch);
        printf("Case #%d: ",cas++);
        if(number==0)
        {
            puts("0");
            continue;
        }
        int stand=ch[0]-'0',frnd=0;
        for(int i=1;i<=number;i++)
        {
           // printf("i and stand %d %d\n",i,stand);
            if(ch[i]=='0')continue;
            if(stand<i)
            {
                frnd=i-stand;
                stand+=frnd;
            }
            stand+=(ch[i]-'0');
            //printf("stand after %d\n",stand);
        }
        printf("%d\n",frnd);
    }
    return 0;
}
