#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <fstream>
using namespace std;
main() {
  int tc,tci,i,j,N,P,teams,pos,w;
  FILE *fp = fopen("C:/ikj/input.txt","r");
  FILE *fp2 = fopen("C:/ikj/output.txt","w");

  fscanf(fp,"%d",&tc);
  for(tci=0;tci<tc;tci++) {
      fscanf(fp,"%d %d",&N,&P);
      teams=pow(2,N);
      for(i=0;i<teams;i++) {
          pos=teams;  //8
          w=i;
          while(w>0) {
              pos=pos/2;
              w-=1;
              w/=2;
          }
          pos=teams-pos;
          if(pos>=P) {
              i--;
              break;
          }
      }
      if(i==teams) i--;
      fprintf(fp2,"Case #%d: %d",tci+1,i);
      for(i=teams-1;i>=0;i--) {
          pos=teams;
          w=teams-i-1;
          while(w>0) {
              pos=pos/2;
              w-=1;
              w/=2;
          }
          if(P>=pos) {
              break;
          }
      }
      fprintf(fp2," %d\n",i);
  }  
}