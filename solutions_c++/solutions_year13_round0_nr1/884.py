#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
#define MAXLEN 110
using namespace std;

int main()
{
    int t, count = 1;
    ifstream fin("A-large.in");
    ofstream fout("A.out");
    
    fin >> t;
    
    while (t--)
    {
        vector <string> status(4, "....");
        int i, j, flag = 0;
        
        for (i = 0; i < 4; i++)
            fin >> status[i];
            
        fout << "Case #" << count++ << ": "; 
            
        for (i = 0; i < 4; i++)
        {
            for (j = 0; j < 4; j++)
                if (status[i][j] != 'X' && status[i][j] != 'T')
                    break;
                    
            if (j == 4)
            {
                fout << "X won" << endl;
                flag = 1;
                break;
            }
            
            for (j = 0; j < 4; j++)
                if (status[i][j] != 'O' && status[i][j] != 'T')
                    break;
                    
            if (j == 4)
            {
                fout << "O won" << endl;
                flag = 1;
                break;
            }
        }
        
        if (flag == 1)
            continue;
        
        for (j = 0; j < 4; j++)
        {
            for (i = 0; i < 4; i++)
                if (status[i][j] != 'X' && status[i][j] != 'T')
                    break;
                    
            if (i == 4)
            {
                fout << "X won" << endl;
                flag = 1;
                break;
            }
            
            for (i = 0; i < 4; i++)
                if (status[i][j] != 'O' && status[i][j] != 'T')
                    break;
                    
            if (i == 4)
            {
                fout << "O won" << endl;
                flag = 1;
                break;
            }
        }
        
        if (flag == 1)
            continue;
        
        for (i = 0; i < 4; i++)
            if (status[i][i] != 'X' && status[i][i] != 'T')
                break;
                
        if (i == 4)
        {
            fout << "X won" << endl;
            flag = 1;
        }
        
        if (flag == 1)
            continue;
        
        for (i = 0; i < 4; i++)
            if (status[i][3-i] != 'X' && status[i][3-i] != 'T')
                break;
                
        if (i == 4)
        {
            fout << "X won" << endl;
            flag = 1;
        }
        
        if (flag == 1)
            continue;
        
        for (i = 0; i < 4; i++)
            if (status[i][i] != 'O' && status[i][i] != 'T')
                break;
                
        if (i == 4)
        {
            fout << "O won" << endl;
            flag = 1;
        }
        
        if (flag == 1)
            continue;
        
        for (i = 0; i < 4; i++)
            if (status[i][3-i] != 'O' && status[i][3-i] != 'T')
                break;
                
        if (i == 4)
        {
            fout << "O won" << endl;
            flag = 1;
        }
        
        if (flag == 1)
            continue;
        
        if (flag == 0)
        {
            for (i = 0; i < 4; i++)
            {
                for (j = 0; j < 4; j++)
                {
                    if (status[i][j] == '.')
                    {
                        fout << "Game has not completed" << endl;
                        flag = 2;
                        break;
                    }
                }
                
                if (flag == 2)
                    break;
            }
            
            if (flag == 0)
                fout << "Draw" << endl;
        }
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
