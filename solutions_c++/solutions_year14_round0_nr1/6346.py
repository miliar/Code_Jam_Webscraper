#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;
int main(){
    FILE *in,*out;
    in=fopen("A-small-attempt0.in","r");
    out=fopen("output.txt","w");
    int t,k=1,i,j;
    fscanf(in,"%d",&t);
    while(k<=t){
            int c1,c2,d=0,ans;
    int a[4][4],b[4][4];
        fscanf(in,"%d",&c1);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            fscanf(in,"%d",&a[i][j]);
            //fprintf(out,"%d\n",a[1][1]);

        fscanf(in,"%d",&c2);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            fscanf(in,"%d",&b[i][j]);
         for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            if(a[c1-1][i]==b[c2-1][j])
       {
        ans=a[c1-1][i];
        //fprintf(out,"%d\n",ans);
        d++;
        }
   if(d==1)
    fprintf(out,"Case #%d: %d\n",k,ans);
   else if(d>1)
    fprintf(out,"Case #%d: Bad magician!\n",k);
    else if(d==0)
    fprintf(out,"Case #%d: Volunteer cheated!\n",k);



k++;
}
}
