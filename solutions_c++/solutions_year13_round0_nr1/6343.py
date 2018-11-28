#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    
    int i = 0;
    
    while(t--) {
        i++;
        
        char c[4][4];
        char a;
        int b = 0;
        
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> c[i][j];
                
                if (c[i][j] == '.') {
                    b++;
                }
            }
        }
        
        bool x = false, o = false;
        
        if ((c[0][0] == 'X' or c[0][0] == 'T') and (c[0][1] == 'X' or c[0][1] == 'T') and (c[0][2] == 'X' or c[0][2] == 'T') and (c[0][3] == 'X' or c[0][3] == 'T'))
            x = true;
        else if ((c[1][0] == 'X' or c[1][0] == 'T') and (c[1][1] == 'X' or c[1][1] == 'T') and (c[1][2] == 'X' or c[1][2] == 'T') and (c[1][3] == 'X' or c[1][3] == 'T'))
            x = true;
        else if ((c[2][0] == 'X' or c[2][0] == 'T') and (c[2][1] == 'X' or c[2][1] == 'T') and (c[2][2] == 'X' or c[2][2] == 'T') and (c[2][3] == 'X' or c[2][3] == 'T'))     
            x = true;
        else if ((c[3][0] == 'X' or c[3][0] == 'T') and (c[3][1] == 'X' or c[3][1] == 'T') and (c[3][2] == 'X' or c[3][2] == 'T') and (c[3][3] == 'X' or c[3][3] == 'T'))
            x = true;
        else if ((c[0][0] == 'O' or c[0][0] == 'T') and (c[0][1] == 'O' or c[0][1] == 'T') and (c[0][2] == 'O' or c[0][2] == 'T') and (c[0][3] == 'O' or c[0][3] == 'T'))
            o = true;
        else if ((c[1][0] == 'O' or c[1][0] == 'T') and (c[1][1] == 'O' or c[1][1] == 'T') and (c[1][2] == 'O' or c[1][2] == 'T') and (c[1][3] == 'O' or c[1][3] == 'T'))
            o = true;
        else if ((c[2][0] == 'O' or c[2][0] == 'T') and (c[2][1] == 'O' or c[2][1] == 'T') and (c[2][2] == 'O' or c[2][2] == 'T') and (c[2][3] == 'O' or c[2][3] == 'T'))     
            o = true;
        else if ((c[3][0] == 'O' or c[3][0] == 'T') and (c[3][1] == 'O' or c[3][1] == 'T') and (c[3][2] == 'O' or c[3][2] == 'T') and (c[3][3] == 'O' or c[3][3] == 'T'))
            o = true;
        else if ((c[0][0] == 'X' or c[0][0] == 'T') and (c[1][0] == 'X' or c[1][0] == 'T') and (c[2][0] == 'X' or c[2][0] == 'T') and (c[3][0] == 'X' or c[3][0] == 'T'))
            x = true;
        else if ((c[0][1] == 'X' or c[0][1] == 'T') and (c[1][1] == 'X' or c[1][1] == 'T') and (c[2][1] == 'X' or c[2][1] == 'T') and (c[3][1] == 'X' or c[3][1] == 'T'))
            x = true;
        else if ((c[0][2] == 'X' or c[0][2] == 'T') and (c[1][2] == 'X' or c[1][2] == 'T') and (c[2][2] == 'X' or c[2][2] == 'T') and (c[3][2] == 'X' or c[3][2] == 'T'))
            x = true;
        else if ((c[0][3] == 'X' or c[0][3] == 'T') and (c[1][3] == 'X' or c[1][3] == 'T') and (c[2][3] == 'X' or c[2][3] == 'T') and (c[3][3] == 'X' or c[3][3] == 'T'))
            x = true;
        else if ((c[0][0] == 'O' or c[0][0] == 'T') and (c[1][0] == 'O' or c[1][0] == 'T') and (c[2][0] == 'O' or c[2][0] == 'T') and (c[3][0] == 'O' or c[3][0] == 'T'))
            o = true;
        else if ((c[0][1] == 'O' or c[0][1] == 'T') and (c[1][1] == 'O' or c[1][1] == 'T') and (c[2][1] == 'O' or c[2][1] == 'T') and (c[3][1] == 'O' or c[3][1] == 'T'))
            o = true;
        else if ((c[0][2] == 'O' or c[0][2] == 'T') and (c[1][2] == 'O' or c[1][2] == 'T') and (c[2][2] == 'O' or c[2][2] == 'T') and (c[3][2] == 'O' or c[3][2] == 'T'))
            o = true;
        else if ((c[0][3] == 'O' or c[0][3] == 'T') and (c[1][3] == 'O' or c[1][3] == 'T') and (c[2][3] == 'O' or c[2][3] == 'T') and (c[3][3] == 'O' or c[3][3] == 'T'))
            o = true;
        else if ((c[0][0] == 'X' or c[0][0] == 'T') and (c[1][1] == 'X' or c[1][1] == 'T') and (c[2][2] == 'X' or c[2][2] == 'T') and (c[3][3] == 'X' or c[3][3] == 'T'))
            x = true;
        else if ((c[0][3] == 'X' or c[0][3] == 'T') and (c[1][2] == 'X' or c[1][2] == 'T') and (c[2][1] == 'X' or c[2][1] == 'T') and (c[3][0] == 'X' or c[3][0] == 'T'))
            x = true;
        else if ((c[0][0] == 'O' or c[0][0] == 'T') and (c[1][1] == 'O' or c[1][1] == 'T') and (c[2][2] == 'O' or c[2][2] == 'T') and (c[3][3] == 'O' or c[3][3] == 'T'))
            o = true;
        else if ((c[0][3] == 'O' or c[0][3] == 'T') and (c[1][2] == 'O' or c[1][2] == 'T') and (c[2][1] == 'O' or c[2][1] == 'T') and (c[3][0] == 'O' or c[3][0] == 'T'))
            o = true;
            
        if (x)
            cout << "Case #" << i << ": " << "X won";
        else if (o)
            cout  << "Case #" << i << ": " << "O won";
        else if (not x and not o and b)
            cout  << "Case #" << i << ": " << "Game has not completed";
        else
            cout  << "Case #" << i << ": " << "Draw";
            
        cout << endl;
    }
    
    return 0;
}