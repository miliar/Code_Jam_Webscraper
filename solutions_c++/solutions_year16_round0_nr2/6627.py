#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
int main(){
    int i,solusi,temp,t,len,j,isMin;
    char s[101],c;
    FILE *in,*out;
    in=fopen("B-large.in","r");
    out=fopen("output.txt","w");
    fscanf(in,"%d",&t);
    fscanf(in,"%c",&c);
    for(i=1;i<=t;i++){
      solusi=0;
      fscanf(in,"%s",s);
      len=strlen(s);
      for(j=0;j<len;j++){
        if(s[j]=='-'){
          temp=j+1;
          while(temp<len && s[temp]!='+'){
            temp++;
          }
          solusi++;
          j=temp-1;
        }
        else if(s[j]=='+'){
          isMin=0;
          temp=j+1;
          while(temp<len && s[temp]!='-'){
            temp++;
          }
          if(temp<len)
            isMin=1;
          if(isMin==1){
            while(temp<len && s[temp]!='+'){
              temp++;
            }
            if(temp<len){
              j=temp-1;
            }
            else{
              j=temp;
            }
            solusi+=2;
          }
        }
      }
      fprintf(out,"Case #%d: %d\n",i,solusi);
    }
    return 0;
}
