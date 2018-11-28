#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <limits>

using namespace std;

int main(void){
    int t,r,f0=0,f1=0,f2=0,w=0,a,b,c,d;
    vector<int> v;
    v.assign(16,0);
    FILE *in,*out;
//    in=fopen("in.txt","r");
    in=fopen("A-small-attempt0.in","r");
//    in=fopen("B-large.in","r");
    out=fopen("out.txt","w");
    fscanf(in,"%d",&t);
    for (int i=1;i<=t;i++){
        f0=0,f1=0,f2=0,w=0;
        v.assign(16,0);
        for (int j=0;j<=1;j++){
           fscanf(in,"%d",&r);   
           for (int k=1;k<=4;k++){           
               fscanf(in,"%d %d %d %d",&a,&b,&c,&d);   
               if (r==k){
                  v[a-1]++;
                  v[b-1]++;
                  v[c-1]++;
                  v[d-1]++;                                                      
                  }
               }
           }
        for (int j=0;j<16;j++){
            switch (v[j]){
                  case 0:f0++;break;
                  case 1:f1++;break;
                  case 2:f2++;w=j+1;break;                                    
                  }
            }
        fprintf(out,"Case #%d: ",i);
        if (f2==1){
              fprintf(out,"%d\n",w);              
              }
        else if (f2>1){
              fprintf(out,"Bad magician!\n");              
              }
        else if (f2<1){
              fprintf(out,"Volunteer cheated!\n");              
              }
        }
    fclose (in);
    fclose (out);
    return 0;
    }
