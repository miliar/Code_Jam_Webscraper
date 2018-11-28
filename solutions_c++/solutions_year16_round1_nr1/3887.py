#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
int main()
{
    FILE* in,*out;
    int i,len,j,z,t;
    char solusi[5005],s[5005],c;
    in=fopen("A-large.in","r");
    out=fopen("solusi.txt","w");
    fscanf(in,"%d",&t);
    fscanf(in,"%c",&c);
    for(i=1;i<=t;i++){
       fscanf(in,"%s",s);
       len=strlen(s);
       strcpy(solusi,"");
       solusi[0]=s[0];
       for(j=1;j<len;j++){
         if(solusi[0]<=s[j]){
           for(z=j;z>0;z--)
             solusi[z]=solusi[z-1];
           solusi[0]=s[j];
         }
         else{
           solusi[j]=s[j];
         }
       } 
       solusi[len]='\0';
       fprintf(out,"Case #%d: %s\n",i,solusi);
    }
    return 0;
}
