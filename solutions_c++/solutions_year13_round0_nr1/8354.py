#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <fstream>
using namespace std;

char map[6][6]; 


int main(){
    int i,j,k,t,kong;
    ifstream fin("A-small-attempt1.in");
    ofstream fout("xxx.out");
    while(fin>>t){
          k=1;
          while(k<=t){
                    memset(map,0,sizeof(map));
                    kong = 0;
                           for(i=1;i<=4;i++){
                                  for(j=1;j<=4;j++){
                                         fin>>map[i][j];
                                         if(map[i][j]=='O'){
                                                  map[i][0]++;                   
                                                  map[0][j]++;
                                         }                  
                                         if(map[i][j]=='X'){
                                                  map[i][5]++;
                                                  map[5][j]++;                   
                                         }
                                         if(map[i][j]=='T'){
                                                  map[i][0]++;                   
                                                  map[0][j]++;                                                                     
                                                  map[i][5]++;
                                                  map[5][j]++;                                                              
                                         } 
                                         if(map[i][j]=='.') kong = 1;                                                
                                  }                                                                       
                           }
                           for(i=1;i<5;i++){
                                   switch(map[i][i]){
                                          case 'O' : map[0][0]++;break;
                                          case 'X' : map[5][5]++;break;
                                          case 'T' : map[0][0]++;map[5][5]++;break;                      
                                   }
                                   switch(map[i][5-i]){
                                          case 'O': map[5][0]++;break;
                                          case 'X': map[0][5]++;break;
                                          case 'T': map[5][0]++;map[0][5]++;break;  
                                   }            
                           }
                           int flag = 0;
                           for(i=1;i<5;i++){
                                   if(map[0][i]==4||map[i][0]==4){                 
                                            flag = 1;
                                            break;
                                   }
                                   if(map[5][i]==4||map[i][5]==4){
                                             flag = 2;
                                             break;                               
                                   }         
                           }
                           if(map[0][0]==4||map[5][0]==4) flag = 1;
                           if(map[0][5]==4||map[5][5]==4) flag = 2; 
                           if(!flag){
                                     if(kong == 1) flag = 4;
                                     else flag = 3;          
                           }                        
                           fout<<"Case #"<<k<<": ";
                           switch(flag){
                                        case 1:fout<<"O won"<<endl;break;
                                        case 2:fout<<"X won"<<endl;break;
                                        case 3:fout<<"Draw"<<endl;break;                                        
                                        case 4:fout<<"Game has not completed"<<endl;break;                                        
                           }  
                           k++;                         
                     
                     
                     
          }                      
    }       
    return 0;   
}
