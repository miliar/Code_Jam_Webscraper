#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    FILE *fp;
    fp=fopen("A-large.in","r");
    FILE *fpa;
    fpa=fopen("ans.txt","w");
    int i,j,k,test[10],T,t,flag;
    long long int bignum,backup,num;
    fscanf(fp,"%d",&T);
    for(t=1;t<=T;t++)
    {
        for(i=0;i<10;i++)
            test[i]=0;
        fscanf(fp,"%lld",&num);
        for(i=1;i<100;i++)
        {
            bignum=i*num;
            backup=bignum;
            if(bignum==num && i!=1)
            {
                flag=1;
                break;
            }
            while(bignum!=0)
            {
                flag=0;
                j=bignum%10;
                bignum=bignum/10;
                test[j]=1;
                for(k=0;k<10;k++)
                {
                    if(test[k]!=1)
                    {
                        flag=1;
                        break;
                    }
                }

                if(flag==0)
                    break;
            }
            if(flag==0)
            {
                fprintf(fpa,"Case #%d: %lld\n",t,backup);
                break;
            }
        }
        if(flag==1)
            fprintf(fpa,"Case #%d: INSOMNIA\n",t);
    }
    fclose(fp);
    fclose(fpa);
    return 0;
}
