#include<stdio.h>
#include<stdlib.h>
int main()
{
        FILE* in;
        FILE* out;
        in=fopen("A-large (1).in","r");
        out=fopen("OUTPUT.txt","w");
        int num[10];
        int t,i,j,k,d,flag,flag1;
        long int n,n1,no;
        fscanf(in,"%d",&t);
        for(i=1;i<=t;i++)
        {
                flag=0;
                flag1=0;
                for(j=0;j<10;j++)
                {
                        num[j]=0;
                }
                fscanf(in,"%ld",&n);
                j=1;
                n1=-1;
                while(flag==0 && flag1==0)
                {
                        no=n*j;
                        if(n1==no)
                                flag1=1;
                        n1=no;
                        while(no>0)
                        {
                                d=no%10;
                                num[d]=1;
                                no=no/10;
                        }
                        for(k=0;k<10;k++)
                        {
                                if(num[k]==0)
                                        break;
                        }
                        if(k==10)
                                flag=1;
                        j++;
                }
                if(flag==1)
                        fprintf(out,"Case #%d: %ld\n",i,n1);
                else
                        fprintf(out,"Case #%d: INSOMNIA\n",i);
        }
}
