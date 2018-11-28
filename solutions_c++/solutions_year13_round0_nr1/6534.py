#include <iostream>
#include <fstream>
#include <conio.h>

using namespace std;

char mat[4][4];
    

int check (char player)
{
    int won;
   
    for (int i=0;i<4;i++){
        won=1;
        for (int j=0;j<4;j++){
            if (mat[i][j]!=player && mat[i][j]!='T'){
               won=0;
               break;
            }
        }
        if (won==1)
           return 1;
    }
    
    for (int i=0;i<4;i++){
        won=1;
        for (int j=0;j<4;j++){
            if (mat[j][i]!=player && mat[j][i]!='T'){
               won=0;
               break;
            }
        }
        if (won==1)
           return 1;
    }
    
    won=1;
    for (int j=0;j<4;j++){
        if (mat[j][j]!=player && mat[j][j]!='T'){
           won=0;
           break;
        }
    }
    if (won==1)
       return 1;
    
    won=1;
    for (int j=0;j<4;j++){
        if (mat[j][3-j]!=player && mat[j][3-j]!='T'){
           won=0;
           break;
        }
    }
    if (won==1)
       return 1;
     
               
return 0;

}





int main ()

{
    ofstream out;
    out.open ("A_output.txt");
    ifstream in;
    in.open ("A_input.txt");
    
    
    int nt;
    in>>nt;
    for (int t=1;t<=nt;t++){
    
    int complete=1;
    
    for (int i=0;i<4;i++){
        for (int j=0;j<4;j++){
            in>>mat[i][j];
            if (mat[i][j]=='.')
               complete=0;
        }
    }
    
    out<<"Case #"<<t<<": ";
    if (check('X')==1)
       out<<"X won"<<endl;
    else if (check('O')==1)
       out<<"O won"<<endl;
    else if (complete==0)
       out<<"Game has not completed"<<endl;
    else out<<"Draw"<<endl;        
       
        
}       
            
    
getch ();    
    
}
