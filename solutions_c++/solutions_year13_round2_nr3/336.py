#include <iostream>
#include <cstdio>
#include <algorithm>
#define nwords 521196
#define debug(args...) fprintf(stderr,args)
using namespace std;

int dp[60][60];
char str[1010];

char palavra[nwords][100];


int get(int pos,int qnt){
    
    //debug("get pos = %d qnt = %d\n",pos,qnt);
    if(pos > strlen(str))return 999999;
    if(pos == strlen(str))return 0;
    
    if(dp[pos][qnt+6]+1)return dp[pos][qnt+6];
    
    int ret = 999999;
    
     for(int i=0;i<nwords;i++){
         
         int ok = 1;
         int last_change = qnt;
         int changes = 0;
         
         for(int j=0;j<strlen(palavra[i]);j++){
                
                if(str[pos+j] != palavra[i][j]){
                        
                        if(pos+j-last_change < 5){ok = 0;goto www;}
                        last_change = pos+j;
                        changes++;
                    
                    }}
                
                if(ok){
                 //   debug(" -> %s\n",palavra[i]);
                 //   getchar();
                 int k = changes+get(pos+strlen(palavra[i]),last_change);
                 int last = ret;
                 ret = min(ret,k);
                 
                 if(k < last){
                   //  debug("dp[%d][%d] (-> %s) := %d\n",pos,qnt,palavra[i],ret);
                 //   getchar();]
                    if(k == 0)return dp[pos][qnt+6] = 0;
                    }
                       
                //    debug("ret (%d;%d) := %d\n",pos,qnt,ret);
                 //   getchar();
                
                
                
            }
            
            www:;
            
        }
    return dp[pos][qnt+6] = ret;
    
}


main(){
    
    
    FILE* fin = fopen("file.txt","r");
    for(int i=0;i<nwords;i++){
        fscanf(fin," %s",palavra[i]);
        //cout << palavra[i] << endl;   
}
    
    int te;
    scanf("%d",&te);
    
    for(int t=1;t<=te;t++){
        
        scanf(" %s",str);
        memset(dp,-1,sizeof(dp));
        
        printf("Case #%d: %d\n",t,get(0,-5));   
        
        
    }}
