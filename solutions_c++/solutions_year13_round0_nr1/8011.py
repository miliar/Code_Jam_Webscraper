#include <iostream>

using namespace std;

int main()
{

    char pole[4][4];
    int X,O;
    bool dot;
    bool done;
    int n;
    cin >>n;
    for(int i =0; i< n; i++)
    {
        dot = false;
        done = false;
        for(int j =0; j<4;j++)
        {
            X = 0; O=0;
            for(int k =0;k<4;k++)
            {
                cin>> pole[j][k];
                if(pole[j][k] == 'X' || pole[j][k] == 'T')
                    X++;
                    else if(pole[j][k]== 'O' || pole[j][k] == 'T')
                    O++;
                    else if(pole[j][k] == '.')
                        dot= true;
            }
            if(X==4)
             {   cout << "Case #" << i+1 << ": X won\n"; done = true;}
                else if(O==4)
                   { cout << "Case #" << i+1 << ": O won\n"; done = true;}
        }
        
        if(done == false)
              for(int k =0; k<4;k++)
             {
                X = 0; O=0;
                for(int j =0;j<4;j++)
                {
                    if(pole[j][k] == 'X' || pole[j][k] == 'T')
                        X++;
                        else if(pole[j][k]== 'O' || pole[j][k] == 'T')
                        O++;
                } 
                    if(X==4)
                     {   cout << "Case #" << i+1 << ": X won\n"; done = true;}
                        else if(O==4)
                           { cout << "Case #" << i+1 << ": O won\n"; done = true;} 
               } 
         
        if(done == false)     
        {
            if((pole[0][0] == 'X' || pole [0][0] == 'T') && (pole[1][1] == 'X' || pole [1][1] == 'T') && (pole[2][2] == 'X' || pole [2][2] == 'T') && (pole[3][3] == 'X' || pole [3][3] == 'T'))
                {   cout << "Case #" << i+1 << ": X won\n"; done = true;}
             else if((pole[0][0] == 'O' || pole [0][0] == 'T') && (pole[1][1] == 'O' || pole [1][1] == 'T') && (pole[2][2] == 'O' || pole [2][2] == 'T') && (pole[3][3] == 'O' || pole [3][3] == 'T'))
                { cout << "Case #" << i+1 << ": O won\n"; done = true;} 
             else if((pole[0][3] == 'X' || pole [0][3] == 'T') && (pole[1][2] == 'X' || pole [1][2] == 'T') && (pole[2][1] == 'X' || pole [2][1] == 'T') && (pole[3][0] == 'X' || pole [3][0] == 'T'))
                {   cout << "Case #" << i+1 << ": X won\n"; done = true;}
              else if((pole[0][3] == 'O' || pole [0][3] == 'T') && (pole[1][2] == 'O' || pole [1][2] == 'T') && (pole[2][1] == 'O' || pole [2][1] == 'T') && (pole[3][0] == 'O' || pole [3][0] == 'T'))
                { cout << "Case #" << i+1 << ": O won\n"; done = true;} 
       }
       
       if(done == false)
            if(dot == true)
                cout << "Case #" << i+1 << ": Game has not completed\n";
                else
                cout << "Case #" << i+1<< ": Draw\n";         
 
    }
    
return 0;
}    
    
    
    
    
    
    
    
    
    
    
    
