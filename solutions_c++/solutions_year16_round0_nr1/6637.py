#include<stdio.h>
FILE *fi = fopen("A-large.in","a+");
FILE *fo = fopen("output.txt","w+");
void countdigit(int num,int mult,int &counter,bool A[])
{
    int check = 1;
    num = num*mult;
    while(num/check !=0)
    {
        int checker = (num%(check*10) - num%(check))/(check);
        //fprintf(fo," %d",checker);
        if(!A[checker])
        {
            counter--;
            A[checker]=true;
        }
        if(counter == 0)
        {
            fprintf(fo,"%d\n",num);
            break;
        }
        check = check * 10;
        //fprintf(fo,"\n%d\n",counter);
    }

}
main()
{
    int t;
    fscanf(fi,"%d",&t);
    int temp;
    for(int i=1;i<=t;i++)
    {
        int counter = 10;
        fscanf(fi,"%d",&temp);
        fprintf(fo,"Case #%d: ",i);
        if(temp==0)
        {
            fprintf(fo,"INSOMNIA\n");
            continue;
        }
        bool A[12];
        for(int k =0;k<=9;k++)
            A[k]=false;
        int mult = 1;
        while(1)
        {
            countdigit(temp,mult,counter,A);
            if(counter == 0)
                break;
            mult++;
        }
    }
}
