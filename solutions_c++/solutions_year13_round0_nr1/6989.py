#include <iostream>
#include <fstream>



using namespace std;

int main(){
    
    fstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("output.txt");
    
    int test,count;
    in>>test;
    count=1;
    
    while(test>0){
          bool xwon,owon,ghnc;
          xwon=owon=ghnc=false; 
          char **arr;
          arr =  new char*[4];
          for(int i=0;i<4;i++){
                  arr[i] =  new char[4];
                  in>>arr[i];
                  cout<<arr[i]<<endl;        
          }
          cout<<endl;
          
          for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                        if(arr[i][j]=='.'){
                              ghnc = true;                                
                        }
                                          
                        //check verticle
                        for(int x=0;x<4;x++){
                                if(arr[i][x]==arr[i][j] || arr[i][x]=='T'){
                                       
                                      if(x==3){
                                            if(arr[i][j]=='X'){xwon = true;}
                                            if(arr[i][j]=='O'){owon = true;}   
                                      } 
                                       
                                       
                                                                                
                                } else {
                                     break;     
                                }        
                        }
                        //check horizontal
                        for(int x=0;x<4;x++){
                                if(arr[x][j]==arr[i][j] || arr[x][j]=='T'){
                                       
                                      if(x==3){
                                            if(arr[i][j]=='X'){xwon = true;}
                                            if(arr[i][j]=='O'){owon = true;}   
                                      } 
                                       
                                       
                                                                                
                                } else {
                                     break;     
                                }        
                        }
                        
                        
                        
                        
                                     
                }                            
          }
          
          //check diagonal
                        for(int x=0,y=0;x<4&&y<4;x++,y++){
                                if(arr[x][y]=='X' || arr[x][y]=='T'){
                                       
                                      if(x==3){
                                            xwon = true;
                                            //if(arr[x][y]=='O'){owon = true;}   
                                      } 
                                       
                                       
                                                                                
                                } else {
                                     break;     
                                }        
                        }
                        
                        for(int x=0,y=0;x<4&&y<4;x++,y++){
                                if(arr[x][y]=='O' || arr[x][y]=='T'){
                                       
                                      if(x==3){
                                            //if(arr[x][y]=='X'){xwon = true;}
                                            owon = true;   
                                      } 
                                       
                                       
                                                                                
                                } else {
                                     break;     
                                }        
                        }
                        
                        
                        
                        for(int x=3,y=0;x>-1&&y<4;x--,y++){
                                if(arr[x][y]=='X' || arr[x][y]=='T'){
                                       
                                      if(x==0){
                                            xwon = true;
                                            //if(arr[x][y]=='O'){owon = true;}   
                                      } 
                                       
                                       
                                                                                
                                } else {
                                     break;     
                                }        
                        }
                        for(int x=3,y=0;x>-1&&y<4;x--,y++){
                                if(arr[x][y]=='O' || arr[x][y]=='T'){
                                       
                                      if(x==0){
                                            //if(arr[x][y]=='X'){xwon = true;}
                                            owon = true;   
                                      } 
                                       
                                       
                                                                                
                                } else {
                                     break;     
                                }        
                        }
                  
          if(xwon){
                   out<<"Case #"<<count<<": "<<"X won"<<endl;         
          } else if(owon){
                   out<<"Case #"<<count<<": "<<"O won"<<endl;              
          } else if(ghnc){
                   out<<"Case #"<<count<<": "<<"Game has not completed"<<endl;              
          } else {
                   out<<"Case #"<<count<<": "<<"Draw"<<endl;       
          }
          
                  
          //out<<"Case #"<<count<<": "<<endl;//edit later        
          test--;
          count++;                      
    } 
    in.close();
    out.close();
       
    //system("pause");
    return 0;    
}
