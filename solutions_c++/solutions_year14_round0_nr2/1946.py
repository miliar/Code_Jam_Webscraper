#include<stdio.h>
using namespace std;

int main()
{
    FILE *fp,*fp1;
    fp = fopen("B-large.in","r");
    fp1 = fopen("file3.txt","w");
    int t,k,i;
    double c,f,x;
    fscanf(fp,"%d",&t);
    for(k=1;k<=t;k++)
    {
        fscanf(fp,"%lf%lf%lf",&c,&f,&x);
        double temp = 2,temp1,temp2;
        temp1 = x/temp;
        temp2 = c/temp + x/(temp+f);
        double ans=0;
        while(temp1>temp2)
        {
            ans+=c/temp;
            temp+=f;
            temp1 = x/temp;
            temp2 = c/temp + x/(temp+f);
        }
        ans+=x/temp;
        fprintf(fp1,"Case #%d: %.7lf\n",k,ans);




        /*
        fscanf(fp,"%lf%lf%lf",&c,&f,&x);
        double max = (f*(x-c))/c;
        int terns = (int)((max-2)/f);
        double ans = c/2;
        if(terns<0)
            fprintf(fp1,"Case #%d: %.7lf\n",k,x/2);
        else if(terns==0)
        {
            ans=(c/2)+(x/(2+f));
            fprintf(fp1,"Case #%d: %.7lf\n",k,ans);
        }
        else
        {
            for(i=1;i<=terns;i++)
                ans+=c/(2+i*f);
            ans+=x/(2+i*f);
            fprintf(fp1,"Case #%d: %.7lf\n",k,ans);

        }*/

    }
    return 0;
}
