#include <iostream>
#include <algorithm>
#include <cstdio>
#include <utility>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#define pii pai<int,int>
#define debug
using namespace std;

char v[6][6];

int ok(int a,int b){
    
    if(a == '.' ||b=='.')return 0;
    
    if(a== 'T' || b== 'T')return 1;
    
    return (a==b)?1:0;
    
}



char best(char a,char b){
     if(a=='T')return b;
     return a;
     }

main(){
       
       int te;
       scanf("%d",&te);
   
       
       for(int t=1;t<=te;t++){
       
       printf("Case #%d: ",t);
       
       for(int i=0;i<4;i++){
               
                       
                       scanf(" %s",&v[i]);
                    }
      ;
                    
       int ponto=0;
       int foi=0;
       
       for(int i=0;i<4;i++){
               
               if(ok(v[i][0],v[i][1]) && ok(v[i][0],v[i][2]) && ok(v[i][0],v[i][3]) && ok(v[i][1],v[i][2])  && ok(v[i][2],v[i][3])&& ok(v[i][1],v[i][3])){
                           if(!foi)
                            printf("%c won\n",best(v[i][0],v[i][1]));
                            foi=1;
                            }
               if(ok(v[0][i],v[1][i]) && ok(v[0][i],v[2][i]) && ok(v[0][i],v[3][i]) && ok(v[1][i],v[2][i]) && ok(v[1][i],v[3][i]) && ok(v[2][i],v[3][i])
               
               ){if(!foi)
                            printf("%c won\n",best(v[0][i],v[1][i]),i);
                            
                            foi=1;}
                            
               
               if(v[i][0]=='.' || v[i][1]=='.' || v[i][2]=='.' || v[i][3]=='.')ponto =1;
               
               }
               
       if(ok(v[0][0],v[1][1]) && ok(v[0][0],v[2][2]) && ok(v[0][0],v[3][3]) && ok(v[1][1],v[2][2])  && ok(v[1][1],v[3][3]) && ok(v[2][2],v[3][3]) 
       ){                     if(!foi);
                              printf("%c won\n",best(v[0][0],v[1][1]));
                              foi=1;
                              } 
                              
       if(ok(v[0][3],v[1][2]) && ok(v[0][3],v[2][1]) && ok(v[0][3],v[3][0]) && ok(v[1][2],v[2][1]) && ok(v[1][2],v[3][0]) && ok(v[2][1],v[3][0])
       
       ){if(!foi)
                              printf("%c won\n",best(v[0][3],v[1][2]));
                              foi=1;
                              } 
               
       if(!foi){
       if(ponto)printf("Game has not completed\n");   
       else printf("Draw\n");
            }
         
               }

}
