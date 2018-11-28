#include <stdio.h>
#include <string.h>
int main()
{
    //FILE* fp,*fp2;
    int t,i,j,m,n,tmp;
    int flag[20];
    int count;
    //fp=fopen("A-small-practice.in","r");
    //fp2=fopen("A-small-practice.out","w");
    scanf("%d",&t);
    for(m=1;m<=t;m++)
    {   

        printf( "Case #%d: ",m);
        scanf("%d",&n);
        if(n==0)     {printf(fp2,"INSOMNIA\n");continue;} 
        for(i=0;i<10;i++)  flag[i]=0;
            count=0;
        i=0;
        while(1)
        {
            i+=n;
            tmp=i;
            while(tmp>0) 
            {
                
                if(flag[tmp%10]==0)  {flag[tmp%10]++;count++; if(count==10)  break;}

                tmp/=10;
            }
            printf("%d  %d\n",count,i);
            if(count==10)  break;


        }
        printf("%d\n",i);
    }
    //fclose(fp);
    //fclose(fp2);

    return 0;
} 