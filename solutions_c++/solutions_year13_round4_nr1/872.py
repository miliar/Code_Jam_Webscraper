#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <fstream>
using namespace std;
main() {
  int tc,tci,i,j,N,M,mod_saving,orig_saving,a,b,c,temp,temp2,o[100000],e[100000],flag[100000],count;
  FILE *fp = fopen("C:/ikj/input.txt","r");
  FILE *fp2 = fopen("C:/ikj/output.txt","w");

  fscanf(fp,"%d",&tc);
  for(tci=0;tci<tc;tci++) {
      fscanf(fp,"%d %d",&N,&M);
      count=mod_saving=orig_saving=0;
      for(i=0;i<M;i++) {
          fscanf(fp,"%d %d %d",&a,&b,&c);
          temp = b-a;
          if(temp > 1) {
              temp2 = temp*(temp-1)/2;
              orig_saving+=temp2*c;
          }
          for(j=0;j<c;j++) {
              o[count]=a;
              e[count]=b;
              flag[count]=0;
              count++;
          }
      }
      for(i=0;i<count;i++) {
          for(j=i;j<count;j++) {
              if(o[i]>o[j]) {
                  o[i]=o[i]+o[j];
                  o[j]=o[i]-o[j];
                  o[i]=o[i]-o[j];
              }
              if(e[i]<e[j]) {
                  e[i]+=e[j];
                  e[j]=e[i]-e[j];
                  e[i]-=e[j];
              }
          }
      }
      
      for(i=count-1;i>=0;i--) {
          for(j=count-1;j>=0;j--) {
              if((flag[j]==0)&&(e[j]>=o[i])) {
                  flag[j]=1;
                  if((e[j]-o[i]) > 1) {
                      mod_saving+=(e[j]-o[i])*(e[j]-o[i]-1)/2;
                      //fprintf(fp2,"%d ",mod_saving);
                  }
                  break;
              }
          }
      }
      fprintf(fp2,"Case #%d: %d\n",tci+1,mod_saving-orig_saving);
  }  
}