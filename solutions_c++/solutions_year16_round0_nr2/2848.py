#include <stdio.h>
#include <string.h>
int main()
{
    //FILE* fp,*fp2;
    int t,i,j,m,n;
    int last;
    int flag[100];
    int count;
    char tmp;
    //fp=fopen("A-small-practice.in","r");
    //fp2=fopen("A-small-practice.out","w");
    scanf("%d",&t);
    scanf("%c",&tmp);
    for(m=1;m<=t;m++)
    {   
        j=0;
        tmp=0;
        printf( "Case #%d: ",m);
        while(1)
        {
            scanf("%c",&tmp);
            if(tmp=='\n')  break;
            if(tmp=='+')    flag[j++]=1;
            else            flag[j++]=0;
        } 
        count=0;
        last=1;
        for(i=j-1;i>=0;i--)
        {
            if(flag[i]!=last){last=flag[i];count++;}
        }




    printf("%d\n",count );
    }
    //fclose(fp);
    //fclose(fp2);

    return 0;
} 