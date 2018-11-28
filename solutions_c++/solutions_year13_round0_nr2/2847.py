#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream in("in.in");    
    ofstream out("out.out");    
    
    long long num;    
    in>>num;
    
    
    for(long long k=0;k<num;k++){
                   out<<"Case #"<<k+1<<": ";
      int x,y;
      in>>x>>y;
      int b[x][y];

      for(int i=0;i<x;i++){
        for(int j=0;j<y;j++){
           in>>b[i][j];       
        }
      }  
      
      for(int i=0;i<x;i++){       
        for(int j=0;j<y;j++){                    
          bool row=true;
          bool col=true;
          
          for(int l=0;l<x;l++){
            if(l!=i && b[l][j]>b[i][j]) col=false;        
          }
          for(int l=0;l<y;l++){
            if(l!=j && b[i][l]>b[i][j]) row=false;        
          }

          if(!row && !col){
            out<<"NO"<<endl;
            goto next;
          }
        }
      }   
      
      out<<"YES"<<endl;
          
      next:true;
    }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
