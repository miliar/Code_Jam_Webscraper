#include "bits/stdc++.h"
#include "string.h"
#include "math.h"
int tick[10];
int uni=1;
int check()
{
    int a,b,c;
    for(a=0;a<10;a++)
    {
        if(tick[a]==0)
        {
            return 0;
        }
    }
    return 1;
}

int chain()
{
    char ori_int[7];
    scanf("%s",ori_int);

    int len=strlen(ori_int);

    int now[200],ori[7];
    int a,b,c;

    for(a=0;a<200;a++)
    {
        if(a<7)
        {
            ori[a]=0;
        }
        now[a]=0;
    }

    int stock;
    for(a=len-1;a>-1;a--)
    {
        now[a]=ori_int[len-a-1]-'0';
        ori[a]=now[a];
        //printf("%d",ori[a]);
    }
    //printf("\nXXXXXXXXXX\n\n");

    int counter=0;

    for(a=0;a<len;a++)
    {
        now[a+1]+=now[a]/10;
        now[a]=now[a]%10;
        //printf("%d->",now[a]);
        tick[now[a]]=1;
    }
    //printf("\n");
    while(counter<200&&check()==0)
    {
        for(a=0;a<len;a++)
        {
            if(a<7)
            {
                now[a]+=ori[a];
            }

            if(now[a]>=10&&a==len-1)
            {
                len++;
            }
            now[a+1]+=now[a]/10;
            now[a]=now[a]%10;
            //printf("%d->",now[a]);
            tick[now[a]]=1;
        }
        counter++;
        //printf("\n");
        //printf("SWAG");
        /*
        for(a=0;a<10;a++)
        {
            printf("%d ",tick[a]);
        }
        printf("\n");
        */
    }
    int checker=0;
    printf("Case #%d: ",uni++);
    if(check()==1)
    {
        for(a=199;a>-1;a--)
        {
            if(now[a]!=0)
            {
                checker=1;
            }
            if(checker==1)
            {
                printf("%d",now[a]);
            }
        }
        printf("\n");
    }
    else
    {
        printf("INSOMNIA\n");
    }
}

main()
{
    freopen ("counting_sheep_output.txt","w",stdout);
    int time;
    scanf("%d",&time);
    int a,b,c;
    while(time-->0)
    {
        for(a=0;a<10;a++)
        {
            tick[a]=0;
        }
        chain();
    }
}
