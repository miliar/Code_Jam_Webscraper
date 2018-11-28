#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>


using namespace std;

int main(int argc, char *argv[])
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t; 
    cin >> t;
    for(int i = 0; i < t; i++)
    {
            string b;
            vector<string>a;
            for(int j = 0; j < 4; j++)
            {
                  cin >> b;
                  a.push_back(b);  
            }
            
            int O = 0;
            int X = 0;
            int point = 0;
            int T = 0;
            
            bool WO = false;
            bool WX = false;
            bool pass = true;
            
            for(int y = 0; y < 4; y++)
            {
                    T=0;
                    X=0;
                    O=0;
                    for(int x = 0; x < 4; x++)
                    {
                         if(a[y][x] == 'X') X++;
                         if(a[y][x] == 'O') O++;
                         if(a[y][x] == 'T') T++;
                         if(a[y][x] == '.') point++; 
                         //cout <<y << x << endl;
                    }
                    
                    if(X == 4){WX = true; pass = false;} //cout <<"Case #" <<i+1<<": X won" << endl;
                    if(O == 4){WO = true; pass = false;} //cout <<"Case #" <<i+1<<": O won" << endl;
                    if(X == 3 && T > 0){WX = true; pass = false;}
                    if(O == 3 && T > 0){WO = true; pass = false;}
                    
                    T=0;
                    X=0;
                    O=0;
                    
                    for(int z = 0; z < 4; z++)
                    {
                         if(a[z][y] == 'X') X++;
                         if(a[z][y] == 'O') O++;
                         if(a[z][y] == 'T') T++;
                         if(a[z][y] == '.') point++; 
                         //cout <<y << x << endl;
                    }
                    
                    if(X == 4){WX = true; pass = false;} //cout <<"Case #" <<i+1<<": X won" << endl;
                    if(O == 4){WO = true; pass = false;} //cout <<"Case #" <<i+1<<": O won" << endl;
                    if(X == 3 && T > 0){WX = true; pass = false;}
                    if(O == 3 && T > 0){WO = true; pass = false;}                    
                    
                    
            }
            
            
            if(pass){
            T=0;
            X=0;
            O=0;
            
            if(a[0][0] == 'X') X++;
            if(a[1][1] == 'X') X++;
            if(a[2][2] == 'X') X++;
            if(a[3][3] == 'X') X++;
            
            if(a[0][0] == 'O') O++;
            if(a[1][1] == 'O') O++;
            if(a[2][2] == 'O') O++;
            if(a[3][3] == 'O') O++; 
            
            if(a[0][0] == 'T') T++;
            if(a[1][1] == 'T') T++;
            if(a[2][2] == 'T') T++;
            if(a[3][3] == 'T') T++; 
            
            if(a[0][0] == '.') point++;
            if(a[1][1] == '.') point++;
            if(a[2][2] == '.') point++;
            if(a[3][3] == '.') point++;
            
            if(X == 4){WX = true; pass = false;} //cout <<"Case #" <<i+1<<": X won" << endl;
            if(O == 4){WO = true; pass = false;} //cout <<"Case #" <<i+1<<": O won" << endl;
            if(X == 3 && T > 0){WX = true; pass = false;}
            if(O == 3 && T > 0){WO = true; pass = false;}  
            
            T=0;
            X=0;
            O=0;
            
            if(a[0][3] == 'X') X++;
            if(a[1][2] == 'X') X++;
            if(a[2][1] == 'X') X++;
            if(a[3][0] == 'X') X++;
            
            if(a[0][3] == 'O') O++;
            if(a[1][2] == 'O') O++;
            if(a[2][1] == 'O') O++;
            if(a[3][0] == 'O') O++; 
            
            if(a[0][3] == 'T') T++;
            if(a[1][2] == 'T') T++;
            if(a[2][1] == 'T') T++;
            if(a[3][0] == 'T') T++; 
            
            if(a[0][3] == '.') point++;
            if(a[1][2] == '.') point++;
            if(a[2][1] == '.') point++;
            if(a[3][0] == '.') point++;            
                                 
            if(X == 4){WX = true; pass = false;} //cout <<"Case #" <<i+1<<": X won" << endl;
            if(O == 4){WO = true; pass = false;} //cout <<"Case #" <<i+1<<": O won" << endl;
            if(X == 3 && T > 0){WX = true; pass = false;}
            if(O == 3 && T > 0){WO = true; pass = false;}
       }
       
       if(WX)
       {
             cout <<"Case #" <<i+1<<": X won" << endl;
       }
       else if(WO)
       {
            cout <<"Case #" <<i+1<<": O won" << endl;
       }
       else if(point > 0)
       {
            cout <<"Case #" <<i+1<<": Game has not completed" << endl;
       }
       else
       {
           cout <<"Case #" <<i+1<<": Draw" << endl;
       }
            
                                              
            
                   
    }  
    //system("PAUSE");
    return EXIT_SUCCESS;
}
