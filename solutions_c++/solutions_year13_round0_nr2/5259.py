#include <iostream>
#include <fstream>
using namespace std;
int main () {
    ifstream in ("lawnmover.in");
    ofstream out ("lawnmover.out");
    int quantity;
    in >>quantity;
    for (int i=0;i<quantity;i++){
        int height, width;
        in >> height;
        in >>width;
        int grass[height][width];
        bool is_possible=true;
        bool visited[height][width];
        for (int j=0;j<height;j++){
            for (int g=0;g<width;g++){
                in >> grass[j][g];
                if (grass[j][g]==2){
                   visited[j][g]=true;
                }else{
                      visited[j][g]=false;
                }
            }
        }
    
       for (int j=0;j<width;j++){
             if (grass[0][j]==1 /*&& (visited[0][j]==false || visited[height-1][j]==false)*/ && grass[height-1][j]==1){
             bool all_same=true;
             for (int i=0;i<height;i++){
                 if (grass[i][j]==2){all_same=false;}
                 }
             if (all_same==true){
                    for (int i=0;i<height;i++){
                        visited[i][j]=true;
                     }             
                 }
                 
             }
       }
       
       
       for (int i=0;i<height;i++){
           if (grass[i][0]==1 /*&& (visited[i][0]==false || visited[i][width-1]==false)*/ && grass[i][width-1]==1){
              bool all_same=true;
              for (int j=0;j<width;j++){
               if(grass[i][j]==2){all_same=false;}
               }
               if (all_same==true){
              for (int j=0;j<width;j++){
                  visited[i][j]=true;
              }
              } 
           }
       }
    
    
       for (int j=0;j<height;j++){
            for (int g=0;g<width;g++){
                if(visited[j][g]==false){
                   is_possible=false;                         
                }
            }        
            
       }
       if (is_possible==true){
            out << "Case #"<<(i+1)<<": YES\n";
            }else{
                  out << "Case #"<<(i+1)<<": NO\n";
            }
        
    }
    
   
}
