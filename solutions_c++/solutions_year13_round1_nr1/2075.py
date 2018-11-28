#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    FILE *fp,*fp1;
    fp=fopen("input.txt","r");
    fp1=fopen("output.txt","w");
    int t,i,r,m,k,c=0,a;
    fscanf(fp,"%d",&t);
    for(i=1;i<=t;i++)
    {
        c=0;
        fscanf(fp,"%d %d",&r,&m);
        for(k=r;;k=k+2)
        {
            a=(((k+1)*(k+1))-(k*k));
            m=m-a;
            if(m>=0)
            {
                c++;
            }
            else
            break;
        }
        fprintf(fp1,"Case #%d: %d\n",i,c);
    }
    fclose(fp1);
    fclose(fp);
    return 0;
}
