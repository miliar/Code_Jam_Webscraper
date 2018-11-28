#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>
#include "math.h"

using namespace std;






int main()
{
    ifstream fin("A-small-attempt3.in");
    ofstream fout("A-small-attempt3.out");
    
    int T;
    char ch;
    char grid[4][4];
    bool solX=false,solO=false,Draw=true;
    int counter=0;
    fin >> T;
    
    for(int j=0;j <T; j++)
    {
            solX=false;solO=false;Draw = true;
            
            for(int i=0;i<4;i++)
            {
                    for(int j=0;j<4;j++){
                            fin >> grid[i][j];
                            if(grid[i][j] == '.')Draw = false;
                    }
            }
            
            for(int i=0;i<4;i++)
            {
                    for(int j=0;j<4;j++)
                    {
                            if(j==0)
                            {
                                    if(grid[i][j] != 'T')ch = grid[i][j];
                                    else ch = grid [i][1]; 
                                    continue;
                            }
                            if(ch == grid[i][j] || 'T' == grid[i][j])counter++;
                    }
                    if(counter == 3&& ch != '.')
                    {
                               if(ch == 'X') solX = true;
                               else if(ch == 'O')solO = true;
                    }
                    counter=0;
            }
            
            for(int i=0;i<4;i++)
            {
                    for(int j=0;j<4;j++)
                    {
                            if(j==0)
                            {
                                    if(grid[j][i] != 'T')ch = grid[j][i];
                                    else ch = grid [1][i]; 
                                    continue;
                            }
                            if(ch == grid[j][i] || 'T' == grid[j][i])counter++;
                    }
                    if(counter == 3&& ch != '.')
                    {
                               if(ch == 'X') solX = true;
                               else if(ch == 'O')solO = true;
                    }
                    counter=0;
            }
            
            for(int i=0;i<4;i++)
            {
                    if(i==0)
                            {
                                    if(grid[i][i] != 'T')ch = grid[i][i];
                                    else ch = grid [1][1]; 
                                    continue;
                            }
                    if(ch == grid[i][i] || 'T' == grid[i][i])counter++;
            }
            
            if(counter == 3&& ch != '.')
                    {
                               if(ch == 'X') solX = true;
                               else if(ch == 'O')solO = true;
                    }
            counter=0;
            
            for(int i=0;i<4;i++)
            {
                    if(i==0)
                            {
                                    if(grid[i][j] != 'T')ch = grid[i][3-i];
                                    else ch = grid [1][2]; 
                                    continue;
                            }
                    if(ch == grid[i][3-i] || 'T' == grid[i][3-i])counter++;
            }
            if(counter == 3&& ch != '.')
                    {
                               if(ch == 'X') solX = true;
                               else if(ch == 'O')solO = true;
                    }
            counter=0;
            
            
            
            if(solX)fout << "Case #" << j+1 << ": " << "X won" << endl;
            else if(solO)fout << "Case #" << j+1 << ": " << "O won" << endl;
            else if(Draw)fout << "Case #" << j+1 << ": " << "Draw" << endl;
            else fout << "Case #" << j+1 << ": " << "Game has not completed" << endl;
    }
    return 0;
}
