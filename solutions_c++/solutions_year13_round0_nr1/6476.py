#include <cstdlib>
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
    bool Result=false;
    ifstream inp("A-large.in");
    ofstream out("out.txt");
    char matrix[4][4];
    int n;
    inp>>n;
    
    for(int i=0;i<n;i++){  // main loop
            
            Result=false;
            
            // read from file to char array
            for(int k=0;k<4;k++){
                    for(int y=0;y<4;y++){
                            inp>>matrix[k][y];
                           
                            }
                    
                    }
            
            // Main logic
            int dot=0;
            int X=0;
            int T=0;
            int O=0;

            
            
            //horizontal check
           for(int a=0;a<4;a++){
                   X=0;
                   T=0;
                   O=0;
                   dot=0;
                    for(int z=0;z<4;z++){
                    
                    
                    if(matrix[a][z]=='X')
                    X++;
                    
                    if(matrix[a][z]=='O')
                    O++;
                    
                     
                    if(matrix[a][z]=='T')
                    T++;                                                          
                    
                    
                    
                   }    
                   
                   if(X==4||(X==3&&T==1)){
                                          Result=true;
                                          out<<"Case #"<<(i+1)<<": X won";
                                          break;
                                          }
                                          
                                          
                    if(O==4||(O==3&&T==1)){
                                          
                                          out<<"Case #"<<(i+1)<<": O won";
                                          Result=true;
                                          break;
                                          }                                         
                                          
                                          
                                          
                                          
                   } 
                   
                  //vertical check 
                   
            if(Result==false){    
                   
                   dot=0;
                   X=0;
                   T=0;
                   O=0;
            
              for(int b=0;b<4;b++){
                   X=0;
                   T=0;
                   O=0;
                   dot=0;
                    for(int c=0;c<4;c++){
              
                    
                    if(matrix[c][b]=='X')
                    X++;
                    
                    if(matrix[c][b]=='O')
                    O++;
                    
                    

                    if(matrix[c][b]=='T')
                    T++;                                                          
                    
                    
                    
                   }    
                
                   if(X==4||(X==3&&T==1)){
                                          Result=true;
                                          out<<"Case #"<<(i+1)<<": X won";
                                          break;
                                          }
                                          
                                          
                    if(O==4||(O==3&&T==1)){
                                          
                                          out<<"Case #"<<(i+1)<<": O won";
                                          Result=true;
                                          break;
                                          }                                         
                                          
                                          
                                          
                                          
                   } 
                           
           //diagnal check
           if(Result==false){
                   X=0;
                   T=0;
                   O=0;
                   dot=0;         
                   
                   
                      for(int v=0;v<4;v++){
                   
                    if(matrix[v][v]=='X')
                    X++;
                    
                    if(matrix[v][v]=='O')
                    O++;
                    
             
                     
                    if(matrix[v][v]=='T')
                    T++;  

                                         }
                                    
                                   
                                     
                                    
                        if(X==4||(X==3&&T==1)){
                                          Result=true;
                                          out<<"Case #"<<(i+1)<<": X won";
                                        
                                          }
                                          
                                          
                    if(O==4||(O==3&&T==1)){
                                          
                                          out<<"Case #"<<(i+1)<<": O won";
                                          Result=true;
                                         
                                          }                                       
                                     
                                     
                                     
                                     
                             
                             
                             
                             }
                             
           //diagnol from right 
                           //diagnal check
           if(Result==false){
                   X=0;
                   T=0;
                   O=0;
                   dot=0;         
                   
                   
                      for(int v=0,p=3;v<4;v++,p--){
                   
                    if(matrix[v][p]=='X')
                    X++;
                    
                    if(matrix[v][p]=='O')
                    O++;
                    
             
                     
                    if(matrix[v][p]=='T')
                    T++;  

                                         }
                                    
                                   
                                     
                                    
                        if(X==4||(X==3&&T==1)){
                                          Result=true;
                                          out<<"Case #"<<(i+1)<<": X won";
                                        
                                          }
                                          
                                          
                    if(O==4||(O==3&&T==1)){
                                          
                                          out<<"Case #"<<(i+1)<<": O won";
                                          Result=true;
                                         
                                          }                                       
                                     
                                     
                                     
                                     
                             
                             
                             
                             }
                             
                             
                             
          if(Result==false){
                           
            for(int k=0;k<4;k++){
                    for(int y=0;y<4;y++){
                            if(matrix[k][y]=='.'){
                                       out<<"Case #"<<(i+1)<<": Game has not completed";
                                          Result=true;
                                          break;
                                                  }
                           
                            }
                            if(Result==true){
                                             break;
                                             }
                    
                    }
            
                    
                    
                      if(Result==false){
                                          out<<"Case #"<<(i+1)<<": Draw";
                                          Result=true;
                                        
                                        
                                        } 
                       
                            }                   
           
            }
            out<<endl;
            }
    system("PAUSE");
    return EXIT_SUCCESS;
}
