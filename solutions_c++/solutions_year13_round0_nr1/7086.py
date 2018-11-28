#include <iostream>
#include <cstdlib>
using namespace std;

int main(){
    int n;
    
    char input[4][4];
    cin >> n;
    int t=1;
    start :
    while(t<=n){
              int empty = 0;
              for(int i=0;i<4;i++){
                      for(int j=0;j<4;j++){
                              cin >> input[i][j];
                      }
              }
              int *dg= (int*)calloc(4,sizeof(int));
              int *gd= (int*)calloc(4,sizeof(int));    
              for(int i=0;i<4;i++){
                      int *row= (int*)calloc(4,sizeof(int));
                      int *col= (int*)calloc(4,sizeof(int));
                                      
                      for(int j=0;j<4;j++){
                              if(input[i][j]  == 'X'){
                                              row[0] += 1;
                              }else if(input[i][j] == 'T'){
                                    row[1] += 1;
                              }else if(input[i][j] == 'O'){
                                    row[2] += 1;
                              }else{
                                    empty = 1;
                                    row[3] += 1;
                              }
                              if(input[j][i]  == 'X'){
                                              col[0] += 1;
                              }else if(input[j][i] == 'T'){
                                    col[1] += 1;
                              }else if(input[j][i] == 'O'){
                                    col[2] += 1;
                              }else{
                                    empty = 1;
                                    col[3] += 1;
                              }
                              if( i== j){
                                  if(input[j][i]  == 'X'){
                                              dg[0] += 1;
                                  }else if(input[j][i] == 'T'){
                                    dg[1] += 1;
                                  }else if(input[j][i] == 'O'){
                                    dg[2] += 1;
                                  }else{
                                        empty = 1;
                                    dg[3] += 1;
                                  }
                              }
                              if( j == (3-i)){
                                  if(input[i][j]  == 'X'){
                                              gd[0] += 1;
                                  }else if(input[i][j] == 'T'){
                                        gd[1] += 1;
                                  }else if(input[i][j] == 'O'){
                                        gd[2] += 1;
                                  }else{
                                        empty = 1;
                                    gd[3] += 1;
                                  }
                              }         
                      }
                      if( (gd[0] + gd[1] == 4)||(dg[0] + dg[1] == 4)||(col[0] + col[1] == 4)||(row[0] + row[1] == 4) ){
                          cout << "Case #"<<t++<<": X won\n";
                          goto start;
                      }else if(  (gd[1] + gd[2] == 4)|| (dg[1] + dg[2] == 4)|| (col[1] + col[2] == 4)|| (row[1] + row[2] == 4)){
                            cout << "Case #"<<t++<<": O won\n";
                            goto start;
                      }
              }
              if(empty == 0){
                       cout << "Case #"<<t++<< ": Draw\n";
                       goto start;
              }else{
                    cout << "Case #" << t++ << ": Game has not completed\n";
                    goto start;
              }                          
    }
  //  system("pause");
    return 0;
}
            
              
    
