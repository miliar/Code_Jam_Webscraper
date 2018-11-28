#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void flip(char* a)
{
    int s = strlen(a);
    for(int i=0;i<s/2;i++)
    {
        char tmp = a[i];
        a[i]=a[s-i-1];
        a[s-i-1]=tmp;
    }
}
void fn(char* a,char* b)
{
    int tmp = 0;
    int ss= strlen(a);
    for(int i=0;i<ss;i++)
    {
        int cal = a[i]-'0'+tmp;
        if(i<strlen(b)) cal += b[i]-'0';
        if(cal>=10)
        {
            tmp=1;
            cal%=10;
        }
        else tmp=0;
        a[i]=cal+'0';
    }
    if(tmp==1)
    {
        int ttmp=strlen(a);
        a[ttmp]='1';
        a[ttmp+1]='\0';
    }
}
main()
{
    int ttt;
    scanf("%d",&ttt);
    for(int tt=0;tt<ttt;tt++)
    {
        printf("Case #%d: ",tt+1);
        bool chk[10]={0};
        int cnt=0;
        char a[50];
        scanf("%s",a);
        if(a[0]=='0')
        {
            printf("INSOMNIA\n");
            continue;
        }
        flip(a);
        char b[50];
        strcpy(b,a);
        while(cnt!=10)
        {
            for(int i=0;i<strlen(a);i++)
            {
                if(!chk[a[i]-'0'])
                {
                    chk[a[i]-'0']=true;
                    cnt++;
                }
            }
            if(cnt>=10)break;
            fn(a,b);
        }
        flip(a);
        printf("%s\n",a);
    }
}
