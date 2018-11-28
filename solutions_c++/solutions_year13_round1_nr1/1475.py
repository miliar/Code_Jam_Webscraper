#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    FILE *fp,*fo;
    fp=fopen("input.txt","r");
    fo=fopen("output.txt","w");
    int t,i,r,p,j,count=0,area;
    fscanf(fp,"%d",&t);
    for(i=1;i<=t;i++)
    {
        count=0;
        fscanf(fp,"%d%d",&r,&p);
        for(j=r;;j=j+2)
        {
            area=(((j+1)*(j+1))-(j*j));
            p=p-area;
            if(p>=0)
            {
                count++;
            }
            else
            break;
        }
        fprintf(fo,"Case #%d: %d\n",i,count);
    }
    fclose(fo);
    fclose(fp);
    return 0;
}
