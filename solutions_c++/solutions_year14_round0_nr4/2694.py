#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
double cmp(const double &a, const double &b){
    return b>a;
}
int main()
{
    FILE *fp,*wfp;
    fp=fopen("D-large.in","r");
    wfp=fopen("D-large.out","w+");
    int round=0,r=1;
    fscanf(fp,"%d",&round);
    while(r<=round){
        int dwar=0,war=0,n=0;
        double naomi[1100],ken[1100];
        fscanf(fp,"%d",&n);
        for(int i=0;i<n;i++)
            fscanf(fp,"%lf",&naomi[i]);
        for(int i=0;i<n;i++)
            fscanf(fp,"%lf",&ken[i]);
        sort(naomi,naomi+n,cmp);
        sort(ken,ken+n,cmp);
        int counti=0,countj=0;
        for(counti=0;counti<n;){
           if(naomi[counti]>ken[countj]){
                    dwar++;
                    counti++;
                    countj++;
           }
           else counti++;
        }
        countj=0;
        for(counti=0;countj<n;){
           if(naomi[counti]<ken[countj]){
               counti++;
               countj++;
           }
           else {
               war++;
               countj++;
           }
        }

       // for(int i=0;i<n;i++)
       //     printf("%lf ",naomi[i]);
        fprintf(wfp,"Case #%d: %d %d\n",r,dwar,war);
        r++;
    }




    fclose(fp);
    fclose(wfp);
    return 0;
}
