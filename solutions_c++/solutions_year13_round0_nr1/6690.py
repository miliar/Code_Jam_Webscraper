
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;
const char X ='X';
const char O ='O';
const char T = 'T';


int  checkWin (char arr[4][4])
{
    //1 x wins, 0 draw , -1 o wins
    //doagonals
    if ((arr[0][0] == X || arr[0][0] == T )&& (arr[1][1] == X ||arr[1][1] == T) 
            && (arr[2][2] == X || arr[2][2] ==T) && (arr[3][3] ==X || arr[3][3] == T) )
        return 1;
    else if ((arr[0][0] == O || arr[0][0] == T )&& (arr[1][1] == O ||arr[1][1] == T) 
            && (arr[2][2] == O || arr[2][2] ==T) && (arr[3][3] ==O || arr[3][3] == T) )
        return -1;
    else if ((arr[0][3] == X || arr[0][3] == T )&& (arr[1][2] == X ||arr[1][2] == T) 
            && (arr[2][1] == X || arr[2][1] ==T) && (arr[3][0] ==X || arr[3][0] == T) )
        return 1;
    else if ((arr[0][3] == O || arr[0][3] == T )&& (arr[1][2] == O ||arr[1][2] == T) 
            && (arr[2][1] == O || arr[2][1] ==T) && (arr[3][0] ==O || arr[3][0] == T) )
        return -1;
    
    //rows
    else if  ((arr[0][0] == X || arr[0][0] == T )&& (arr[0][1] == X ||arr[0][1] == T) 
            && (arr[0][2] == X || arr[0][2] ==T) && (arr[0][3] ==X || arr[0][3] == T) )
        return 1;
    else if ((arr[0][0] == O || arr[0][0] == T )&& (arr[0][1] == O ||arr[0][1] == T) 
            && (arr[0][2] == O || arr[0][2] ==T) && (arr[0][3] ==O || arr[0][3] == T) )
        return -1;
    else if ((arr[1][0] == X || arr[1][0] == T )&& (arr[1][1] == X ||arr[1][1] == T) 
            && (arr[1][2] == X || arr[1][2] ==T) && (arr[1][3] ==X || arr[1][3] == T) )
        return 1;
    else if ((arr[1][0] == O || arr[1][0] == T )&& (arr[1][1] == O ||arr[1][1] == T) 
            && (arr[1][2] == O || arr[1][2] ==T) && (arr[1][3] ==O || arr[1][3] == T) )
        return -1;
    else if ((arr[2][0] == X || arr[2][0] == T )&& (arr[2][1] == X ||arr[2][1] == T) 
            && (arr[2][2] == X || arr[2][2] ==T) && (arr[2][3] ==X || arr[2][3] == T) )
        return 1;
    else if  ((arr[2][0] == O || arr[2][0] == T )&& (arr[2][1] == O ||arr[2][1] == T) 
            && (arr[2][2] == O || arr[2][2] ==T) && (arr[2][3] ==O || arr[2][3] == T) )
        return -1;
    else if ((arr[3][0] == X || arr[3][0] == T )&& (arr[3][1] == X ||arr[3][1] == T) 
            && (arr[3][2] == X || arr[3][2] ==T) && (arr[3][3] ==X || arr[3][3] == T) )
        return 1;
    else if ((arr[3][0] == O || arr[3][0] == T )&& (arr[3][1] == O ||arr[3][1] == T) 
            && (arr[3][2] == O || arr[3][2] ==T) && (arr[3][3] ==O || arr[3][3] == T) )
        return -1;
    
    //columns
    else if ((arr[0][0] == X || arr[0][0] == T )&& (arr[1][0] == X ||arr[1][0] == T) 
            && (arr[2][0] == X || arr[2][0] ==T) && (arr[3][0] ==X || arr[3][0] == T) )
        return 1;
    else if ((arr[0][0] == O || arr[0][0] == T )&& (arr[1][0] == O ||arr[1][0] == T) 
            && (arr[2][0] == O || arr[2][0] ==T) && (arr[3][0] ==O || arr[3][0] == T) )
        return -1;
    else if ((arr[0][1] == X || arr[0][1] == T )&& (arr[1][1] == X ||arr[1][1] == T) 
            && (arr[2][1] == X || arr[2][1] ==T) && (arr[3][1] ==X || arr[3][1] == T) )
        return 1;
    
    else if ((arr[0][1] == O || arr[0][1] == T )&& (arr[1][1] == O ||arr[1][1] == T) 
            && (arr[2][1] == O || arr[2][1] ==T) && (arr[3][1] ==O || arr[3][1] == T) )
        return -1;
    else if ((arr[0][2] == X || arr[0][2] == T )&& (arr[1][2] == X ||arr[1][2] == T) 
            && (arr[2][2] == X || arr[2][2] ==T) && (arr[3][2] ==X || arr[3][2] == T) )
        return 1;
    else if ((arr[0][2] == O || arr[0][2] == T )&& (arr[1][2] == O ||arr[1][2] == T) 
            && (arr[2][2] == O || arr[2][2] ==T) && (arr[3][2] ==O || arr[3][2] == T) )
        return -1;
    else if ((arr[0][3] == X || arr[0][3] == T )&& (arr[1][3] == X ||arr[1][3] == T) 
            && (arr[2][3] == X || arr[2][3] ==T) && (arr[3][3] ==X || arr[3][3] == T) )
        return 1;
    else if ((arr[0][3] == O || arr[0][3] == T )&& (arr[1][3] == O ||arr[1][3] == T) 
            && (arr[2][3] == O || arr[2][3] ==T) && (arr[3][3] ==O || arr[3][3] == T) )
        return -1;
    return 0;
}

bool isDots(char arr[4][4])
{
    bool isdots;
    int n=0;
     for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            if (arr[i][j] == '.')
                n=9;
        }
    }
    
    if (n ==9)
        isdots = true;
    else isdots =false;
    
    return isdots;
}


int main() {
   
    int N;
    ifstream ifs ("input.ini");
    ofstream ofs ("Output.ini");
    ifs >> N;
    cout << N<<endl;
    
    char arr[4][4] = {{},{},{},{}};
    
    for(int i=1; i<=N; i++)
    {
   
        for(int k =0; k<4; k++)
        {
            for (int m =0; m<4; m++)
            {
                ifs >> arr[k][m];
               
            }
            
        }
        
        int compare = checkWin(arr);
        bool isdots = isDots(arr);
        
        if (compare == 1 )
        {
            ofs << "Case #"<<i<<": X won"<<endl;
        }
        else if (compare == -1)
        {
            ofs << "Case #"<<i<<": O won"<<endl;
        }
        
        else if (compare == 0 && isdots == false)
        {
            ofs << "Case #"<<i<<": Draw"<<endl;
        }
        
        else if (compare == 0 && isdots == true)
        {
            ofs << "Case #"<<i<<": Game has not completed"<<endl;
        }
    }
    
   
    
       
    
    
   
        

    return 0;
}
