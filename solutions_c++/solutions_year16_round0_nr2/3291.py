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
    inf=fopen("B-large.in","r");
    outf=fopen("B-large-result.in","w");
    
    int T;
    
    fscanf(inf,"%d",&T);
    for(int i=0;i<T;i++){
            char input[1024];
            fscanf(inf,"%s",&input);
            string nowdata(input);
            staticdata=nowdata;
            int ret = solve(staticdata.size()-1);
            
            
            fprintf(outf,"Case #%d: %d\n",i+1,ret);
            
    }
//    getchar();
}

int solve(int nowpos){
    if(nowpos==0){
                       if(staticdata[nowpos]=='+')return 0;
                       else return 1;                   
    }else{
          char lastchar = staticdata[nowpos];
          for(int i=nowpos-1;i>=0;i--){
                  if(staticdata[i] == lastchar)continue;
                  else{
                           if(lastchar=='+') return solve(i);
                           else return 2 + solve(i);
                  }        
          }
          if(lastchar=='+') return 0;
          else return 1;
          
    }
}
