#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    
    for(int i = 0; i < n; ++i)
    {
        cout << "Case #" << i+1 << ": ";
        vector<char> col(4);
        vector<char> diag(2);
        vector<char> fil(4);
        bool dot = false;
        bool win = false;
        
        int j = 0;
        char c;
        while(!win and j < 4)
        { 
            for(int k = 0; k < 4; ++k)
            {
                cin >> c;
                if(c == '.') dot = true;

                if(j == k)
                {
                    if(j == 0) diag[0] = c;
                    else if(c != 'T' and diag[0] != c) diag[0] = '.';
                }
                
                if(3-j == k)
                {
                    if(j == 0) diag[1] = c;
                    else if(c != 'T' and diag[1] != c) diag[1] = '.';
                }

                if(k == 0) fil[j] = c;
                else if(c != 'T' and fil[j] != c) fil[j] = '.';

                if(j == 0) col[k] = c;
                else if(c != 'T' and col[k] != c) col[k] = '.';
            }
            
            if(fil[j] != '.')
            {
                cout << fil[j] << " won" << endl;
                win = true;
                ++j;
                for(; j < 4; ++j)
                {
                    cin >> c;
                    cin >> c;
                    cin >> c;
                    cin >> c;
                }                    
            }
            else
                ++j;
        }
        
        if(!win)
        {
            j = 0;
            while(!win and j < 4)
            {
                if(col[j] != '.')
                {
                    cout << col[j] << " won" << endl;
                    win = true;
                }
                ++j;
            }
        }
        
        if(!win)
        {
            if(diag[0] != '.')
            {
                cout << diag[0] << " won" << endl;
                win = true;
            }
        }
           
        if(!win)
        { 
            if(diag[1] != '.')
            {
                cout << diag[1] << " won" << endl;
                win = true;
            }
        }
        
        if(!win)
        {
            if(!dot)
                cout << "Draw" << endl;
            else
                cout << "Game has not completed" << endl;
        }
    }
}
