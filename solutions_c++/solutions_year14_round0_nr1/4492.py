#include <cstdio>
#include <iostream>

using namespace std;

int main (){
    
    int t, ans, res, aux, resp;
    int matrx[4][4];
    int matry[4][4];
    scanf("%d", &t);
    
    for (int i=1;i<=t;i++){
        
        aux=0; resp=0;
        
        scanf("%d", &ans);
        ans--;
                
        for (int k=0;k<4;k++)
            for (int j=0;j<4;j++)
                cin>>matrx[k][j];
        
        scanf("%d", &res);
        res--;
        
        for (int k=0;k<4;k++)
            for (int j=0;j<4;j++)
                cin>>matry[k][j];
        
        for (int k=0;k<4;k++){
            //if (aux==2) break;
            for (int j=0;j<4;j++){
                
                if (matrx[ans][k]==matry[res][j]||aux==2){
                   if (aux==1||aux==2){
                      aux=2;
                      break;
                      }else{aux=1; resp=matrx[ans][k];}
                   }
                
                }
            }
        if (aux==1){
           printf("Case #%d: %d\n", i, resp);
           }else{
                 if (aux==2){
                    printf("Case #%d: Bad magician!\n", i );
                    }else
                         printf("Case #%d: Volunteer cheated!", i);
                 }
        }
    
return 0;
    }
