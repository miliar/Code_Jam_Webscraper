#include "bits/stdc++.h"
#include "string.h"
int uni=1;
int chain()
{
    char pancake[500];
    scanf("%s",pancake);
    int len;
    len=strlen(pancake);
    pancake[len]=pancake[len-1];
    int a,b,c;
    int flip_time=0;
    int now=pancake[0];
    for(a=0;a<len;a++)
    {
        if(pancake[a]!=pancake[a+1])
        {
            flip_time++;
            now=pancake[a+1];
        }
    }
    printf("Case #%d: ",uni++);
    if(now=='-')
    {
        flip_time++;
    }
    printf("%d\n",flip_time);
}

main()
{
    freopen("Revenge_of_pancake_output.txt","w",stdout);
    int time;
    scanf("%d",&time);
    while(time-->0)
    {
        chain();
    }
}
