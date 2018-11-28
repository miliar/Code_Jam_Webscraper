#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>
#include<string>

using namespace std;
int solve(int nowpos);
string staticdata;
int main(){
    FILE *inf, *outf;
    inf=fopen("D-small-attempt0.in","r");
    outf=fopen("D-small-attempt0-result.in","w");
    
    int T,K,C,S;
    
    fscanf(inf,"%d",&T);
    for(int i=0;i<T;i++){
            fscanf(inf,"%d %d %d",&K,&C,&S);
            if(C == 1){
                 if(K > 1 && S < K){
                      fprintf(outf,"Case #%d: IMPOSSIBLE\n",i+1);
                 }else{
                       fprintf(outf,"Case #%d:",i+1);
                       for(int i=1;i<=K;i++){
                               fprintf(outf," %d",i);
                       }
                       fprintf(outf,"\n");
                 }
            }else if(S < K-1){
                  fprintf(outf,"Case #%d: IMPOSSIBLE\n",i+1);
            }else if(K==1){
                 fprintf(outf,"Case #%d: 1\n",i+1);
            }else{
                 fprintf(outf,"Case #%d:",i+1);
                 for(int i=2;i<=K;i++){
                         fprintf(outf," %d",i);
                 }
                 fprintf(outf,"\n");
            }
            
    }
//    getchar();
}
