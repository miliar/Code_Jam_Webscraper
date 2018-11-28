#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	ifstream in("in.in");
	ofstream out("out.out");

	int T;
	in >> T;
	
	for(int i = 0; i < T; ++i) 
	{
	    char board [4][4];
        for(int j = 0; j < 4; ++j)
            in >> board[j][0] >> board[j][1] >> board[j][2] >> board[j][3] >> ws;
        
        bool foundAnyDot = false;
        bool foundX = false, foundO = false, foundDot = false;
        bool wonAlready = false;
        //rows and columns win
        for(int j = 0; j < 4; ++j)
        {
            //Check win in row j
            foundX = false, foundO = false, foundDot = false;
                
            for(int k = 0; k < 4; ++k) {
                if(board[j][k] == 'X')
                    foundX = true;
                if(board[j][k] == 'O')
                    foundO = true;
                if(board[j][k] == '.')
                    foundAnyDot = foundDot = true;
            }
            
            if(!foundDot)
            {
                if(foundX && !foundO) {
                    out << "Case #" << i+1 << ": X won" << endl;
                    wonAlready = true;
                    break;
                }
                if(!foundX && foundO) {
                    out << "Case #" << i+1 << ": O won" << endl;
                    wonAlready = true;
                    break;
                }  
            }
            
            //Check win in column j
            foundX = false, foundO = false, foundDot = false;
                
            for(int k = 0; k < 4; ++k) {
                if(board[k][j] == 'X')
                    foundX = true;
                if(board[k][j] == 'O')
                    foundO = true;
                if(board[k][j] == '.')
                    foundAnyDot = foundDot = true;
            }
            
            if(!foundDot)
            {
                if(foundX && !foundO) {
                    out << "Case #" << i+1 << ": X won" << endl;
                    wonAlready = true;
                    break;
                }
                if(!foundX && foundO) {
                    out << "Case #" << i+1 << ": O won" << endl;
                    wonAlready = true;
                    break;
                }
            }
        }
        
        if(wonAlready)
            continue;
        
        foundX = false, foundO = false, foundDot = false;
        //Main diag win
        for(int j = 0; j < 4; ++j)
        {
            if(board[j][j] == 'X')
                foundX = true;
            if(board[j][j] == 'O')
                foundO = true;
            if(board[j][j] == '.')
                foundAnyDot = foundDot = true;
        }
        
        if(!foundDot)
        {
            if(foundX && !foundO){
                out << "Case #" << i+1 << ": X won" << endl;
                continue;
            }
            if(!foundX && foundO) {
                out << "Case #" << i+1 << ": O won" << endl;
                continue;
            }
        }
        
        foundX = false, foundO = false, foundDot = false;
        //Other diag win
        for(int j = 0; j < 4; ++j)
        {
            if(board[j][3-j] == 'X')
                foundX = true;
            if(board[j][3-j] == 'O')
                foundO = true;
            if(board[j][3-j] == '.')
                foundAnyDot = foundDot = true;
        }
        
        if(!foundDot)
        {
            if(foundX && !foundO){
                out << "Case #" << i+1 << ": X won" << endl;
                continue;
            }
            if(!foundX && foundO) {
                out << "Case #" << i+1 << ": O won" << endl;
                continue;
            }
        }
        
        //no wins by here. Either draw or not finished yet
        if(!foundAnyDot)
            out << "Case #" << i+1 << ": Draw" << endl;
        else
            out << "Case #" << i+1 << ": Game has not completed" << endl;
	}
	
	
	out.close();
}
