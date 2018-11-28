#include<stdio.h>
#include<string.h>
main()
{
    int time;
    int i,n,m,c;
    int counter = 1;
    char s[505];
    FILE* fi = fopen("B-large.in","r");
    FILE* fo = fopen("pancake.txt","w");
    fscanf(fi,"%d",&time);
    while(time--)
    {
        fscanf(fi," %s",s);
        n = strlen(s);
        m = n-1;
        c = 0;
        while(s[m]=='+'&&m>=0) m--;
        for(i=0;i<=m;i++) if(s[i]!=s[i+1]) c++;
        fprintf(fo,"Case #%d: %d\n",counter++,c);
    }
    scanf(" ");
}
