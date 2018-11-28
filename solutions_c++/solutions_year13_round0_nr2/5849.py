#include <iostream>
#include <fstream>
#include <conio.h>

using namespace std;

int mat[12][12];
int n,m;
     

int check (int x, int y)
{
    int uni;
    
    //cout<<x<<" "<<y<<endl;
    uni=1;
    for (int j=0;j<m;j++){
        if (mat[x][j]!=1){
           uni=0;
           break;
           }
        }
    if (uni==1)  return 1;

    //cout<<"row failed"<<endl;
        
    uni=1;
    for (int j=0;j<n;j++){
        if (mat[j][y]!=1){
           uni=0;
           break;
           }
        }
    if (uni==1)  return 1;
    
return 0;
    
}




int main ()

{
    ofstream out;
    out.open ("B_output.txt");
    ifstream in;
    in.open ("B_input.txt");
    
    
    int nt;
    in>>nt;
    for (int t=1;t<=nt;t++){
        in>>n>>m;
        
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                in>>mat[i][j];
                }
            }
        
        
        int pos=1;
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                if (mat[i][j]==1){               
                   //cout<<check (i,j)<<endl;
                   if (check(i,j)==0){                
                      pos=0;
                      break;  
                      }
                   }
                }
            }
 
        out<<"Case #"<<t<<": ";           
        if (pos==1)
           out<<"YES"<<endl;
        else out<<"NO"<<endl; 
        
       
        
        }       
            
    
getch ();    
    
}
