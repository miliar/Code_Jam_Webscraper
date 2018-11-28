#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
int tempAngka[10001],angka[10001];
char s[10001],c;
int main(){
    int t,i,j,tambah,isAda[10],finish,len,tempLen;
    FILE *in,*out;
    in=fopen("A-large.in","r");
    out=fopen("output.txt","w");    
    fscanf(in,"%d",&t);
    fscanf(in,"%c",&c);
    for(i=1;i<=t;i++){
      memset(isAda,0,sizeof(isAda));
      memset(angka,0,sizeof(angka));
      memset(tempAngka,0,sizeof(tempAngka));
      strcpy(s,"");
      
      finish=0;
      fscanf(in,"%s",s);
      fprintf(out,"Case #%d: ",i);
      if(strcmp(s,"0")==0){
        fprintf(out,"INSOMNIA\n");
        continue;
      }
      
      len=strlen(s);
      tempLen=len/2;
      for(j=0;j<tempLen;j++){
        c=s[j];
        s[j]=s[len-j-1];
        s[len-j-1]=c;
      }
      
      for(j=0;j<len;j++){
        angka[j]=s[j]-'0';
        if(isAda[angka[j]]==0){
          finish++;
          isAda[angka[j]]=1;
        }
      }
      
      while(finish!=10){
        tambah=0;
        for(j=0;j<len;j++){
          tempAngka[j]=s[j]-'0'+angka[j]+tambah;
          if(tempAngka[j]>=10){
            tempAngka[j]-=10;
            tambah=1;
          }
          else
            tambah=0;
          s[j]=tempAngka[j]+'0';
          if(isAda[tempAngka[j]]==0){
            finish++;
            isAda[tempAngka[j]]=1;
          }
        }
        if(tambah>0){
          s[len]='1';
          len++;
          if(isAda[1]==0){
            finish++;
            isAda[1]=1;
          }
        }
      }
      
      for(j=len-1;j>=0;j--){
          fprintf(out,"%c",s[j]);
        }
      fprintf(out,"\n");
    }
    return 0;
}
