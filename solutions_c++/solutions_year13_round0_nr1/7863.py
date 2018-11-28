#include <iostream>
#include <fstream>
using namespace std;
int main(){
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.out");
    
    int cases;
    fin>>cases;
    char tictac[4][4];
    
    for(int i=0; i<cases; i++)
    {
        bool xwins= false;
        bool owins= false;
        for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                fin>>tictac[j][k];   
            }   
        }   
        
       /* for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                fout<<tictac[j][k]<<"  ";   
            }   
            fout<<endl;
        }*/
        if(((tictac[0][0] == 'X' || tictac[0][0] == 'T') && (tictac[0][1] == 'X' || tictac[0][1] == 'T') && (tictac[0][2] == 'X' || tictac[0][2] == 'T') && (tictac[0][3] == 'X' || tictac[0][3] == 'T'))
        || ((tictac[1][0] == 'X' || tictac[1][0] == 'T') && (tictac[1][1] == 'X' || tictac[1][1] == 'T') && (tictac[1][2] == 'X' || tictac[1][2] == 'T') && (tictac[1][3] == 'X' || tictac[1][3] == 'T'))
        || ((tictac[2][0] == 'X' || tictac[2][0] == 'T') && (tictac[2][1] == 'X' || tictac[2][1] == 'T') && (tictac[2][2] == 'X' || tictac[2][2] == 'T') && (tictac[2][3] == 'X' || tictac[2][3] == 'T')) 
        || ((tictac[3][0] == 'X' || tictac[3][0] == 'T') && (tictac[3][1] == 'X' || tictac[3][1] == 'T') && (tictac[3][2] == 'X' || tictac[3][2] == 'T') && (tictac[3][3] == 'X' || tictac[3][3] == 'T'))
        || ((tictac[0][0] == 'X' || tictac[0][0] == 'T') && (tictac[1][0] == 'X' || tictac[1][0] == 'T') && (tictac[2][0] == 'X' || tictac[2][0] == 'T') && (tictac[3][0] == 'X' || tictac[3][0] == 'T'))
        || ((tictac[0][1] == 'X' || tictac[0][1] == 'T') && (tictac[0][1] == 'X' || tictac[0][1] == 'T') && (tictac[2][1] == 'X' || tictac[2][1] == 'T') && (tictac[3][1] == 'X' || tictac[3][1] == 'T'))
        || ((tictac[0][2] == 'X' || tictac[0][2] == 'T') && (tictac[1][2] == 'X' || tictac[1][2] == 'T') && (tictac[2][2] == 'X' || tictac[2][2] == 'T') && (tictac[3][2] == 'X' || tictac[3][2] == 'T'))
        || ((tictac[0][3] == 'X' || tictac[0][3] == 'T') && (tictac[1][3] == 'X' || tictac[1][3] == 'T') && (tictac[2][3] == 'X' || tictac[2][3] == 'T') && (tictac[3][3] == 'X' || tictac[3][3] == 'T'))
        || ((tictac[0][0] == 'X' || tictac[0][0] == 'T') && (tictac[1][1] == 'X' || tictac[1][1] == 'T') && (tictac[2][2] == 'X' || tictac[2][2] == 'T') && (tictac[3][3] == 'X' || tictac[3][3] == 'T'))
        || ((tictac[0][3] == 'X' || tictac[0][3] == 'T') && (tictac[1][2] == 'X' || tictac[1][2] == 'T') && (tictac[2][1] == 'X' || tictac[2][1] == 'T') && (tictac[3][0] == 'X' || tictac[3][0] == 'T'))
        ){
            xwins= true;
        }
        
        if(((tictac[0][0] == 'O' || tictac[0][0] == 'T') && (tictac[0][1] == 'O' || tictac[0][1] == 'T') && (tictac[0][2] == 'O' || tictac[0][2] == 'T') && (tictac[0][3] == 'O' || tictac[0][3] == 'T'))//2
        || ((tictac[1][0] == 'O' || tictac[1][0] == 'T') && (tictac[1][1] == 'O' || tictac[1][1] == 'T') && (tictac[1][2] == 'O' || tictac[1][2] == 'T') && (tictac[1][3] == 'O' || tictac[1][3] == 'T'))
        || ((tictac[2][0] == 'O' || tictac[2][0] == 'T') && (tictac[2][1] == 'O' || tictac[2][1] == 'T') && (tictac[2][2] == 'O' || tictac[2][2] == 'T') && (tictac[2][3] == 'O' || tictac[2][3] == 'T')) 
        || ((tictac[3][0] == 'O' || tictac[3][0] == 'T') && (tictac[3][1] == 'O' || tictac[3][1] == 'T') && (tictac[3][2] == 'O' || tictac[3][2] == 'T') && (tictac[3][3] == 'O' || tictac[3][3] == 'T'))
        || ((tictac[0][0] == 'O' || tictac[0][0] == 'T') && (tictac[1][0] == 'O' || tictac[1][0] == 'T') && (tictac[2][0] == 'O' || tictac[2][0] == 'T') && (tictac[3][0] == 'O' || tictac[3][0] == 'T'))
        || ((tictac[0][1] == 'O' || tictac[0][1] == 'T') && (tictac[0][1] == 'O' || tictac[0][1] == 'T') && (tictac[2][1] == 'O' || tictac[2][1] == 'T') && (tictac[3][1] == 'O' || tictac[3][1] == 'T'))
        || ((tictac[0][2] == 'O' || tictac[0][2] == 'T') && (tictac[1][2] == 'O' || tictac[1][2] == 'T') && (tictac[2][2] == 'O' || tictac[2][2] == 'T') && (tictac[3][2] == 'O' || tictac[3][2] == 'T'))
        || ((tictac[0][3] == 'O' || tictac[0][3] == 'T') && (tictac[1][3] == 'O' || tictac[1][3] == 'T') && (tictac[2][3] == 'O' || tictac[2][3] == 'T') && (tictac[3][3] == 'O' || tictac[3][3] == 'T'))
        || ((tictac[0][0] == 'O' || tictac[0][0] == 'T') && (tictac[1][1] == 'O' || tictac[1][1] == 'T') && (tictac[2][2] == 'O' || tictac[2][2] == 'T') && (tictac[3][3] == 'O' || tictac[3][3] == 'T'))
        || ((tictac[0][3] == 'O' || tictac[0][3] == 'T') && (tictac[1][2] == 'O' || tictac[1][2] == 'T') && (tictac[2][1] == 'O' || tictac[2][1] == 'T') && (tictac[3][0] == 'O' || tictac[3][0] == 'T'))
        ){
            owins= true;
        }
        
        if(owins==true && xwins== true)
        {
            fout<<"Case #"<<i+1<<": Draw"<<endl;
            continue;  
        }
        else if(owins==true){
            fout<<"Case #"<<i+1<<": O won"<<endl;
            continue;
        }
        else if(xwins==true){
            fout<<"Case #"<<i+1<<": X won"<<endl;
            continue;   
        }
        
        bool incomplete =false;
        for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                if(tictac[j][k] == '.'){
                    incomplete = true;
                    break;   
                }
            }   
        }
        
        if(incomplete == true)
        {
            fout<<"Case #"<<i+1<<": Game has not completed"<<endl;  
            continue;
        }
        
        fout<<"Case #"<<i+1<<": Draw"<<endl;
    }
    
    
    system("pause");
    return 0;   
}
