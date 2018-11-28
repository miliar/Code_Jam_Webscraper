#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <sstream>
#include <bitset>
using namespace std;


int main()
{
	
	
	FILE *fp1 = fopen ("A-small-attempt0.in", "r");
	FILE *fp2 = fopen ("output1.txt", "w");
	//FILE *fp1 = fopen ("B-large.in", "r");
	//FILE *fp2 = fopen ("output22.txt", "w");
	
	int T;
    char board[4][4];
    char line[8];
	fscanf (fp1, "%d\n", &T);
	//printf ("T is %d\n", T);
    
	for (int i = 0; i < T; ++i) {
		if (i != 0)
            //read empty line
            fgets(line, 8, fp1);
        
        string result = "";
        
        //read
        int total = 0;
        bool hasT = false;
		for (int r = 0; r < 4; ++r) {
            for (int c = 0; c < 4; ++c) {
                fscanf (fp1, "%c", &board[r][c]);
                if (board[r][c] != '.' )
                    total++;
                if (board[r][c] != 'T' )
                    hasT = true;
                //new-line
                if (c == 3)
                    fscanf (fp1, "%c", &line[0]);
                    
            }
        }
        
        /*
        for (int r = 0; r < 4; ++r) {
            for (int c = 0; c < 4; ++c) {
                printf ("%c ", board[r][c]);
            }
            printf ("\n");
        }
         */
        
        //check row
        int xTotal = 0, oTotal = 0;
        bool hasTHere = false;
        for (int r = 0; r < 4; ++r) {
            xTotal = oTotal = 0;
            hasTHere = false;
            for (int c = 0; c < 4; ++c) {
                if (board[r][c] == 'X')
                    xTotal += 1;
                if (board[r][c] == 'O')
                    oTotal += 1;
                if (board[r][c] == 'T')
                    hasTHere = true;
            }
            if (xTotal == 4 || xTotal == 3 && hasTHere)
                result = "X won";
            if (oTotal == 4 || oTotal == 3 && hasTHere)
                result = "O won";
            
        }
        

        //check column
        for (int c = 0; c < 4; ++c) {
            xTotal = oTotal = 0;
            hasTHere = false;
            for (int r = 0; r < 4; ++r) {
                if (board[r][c] == 'X')
                    xTotal += 1;
                if (board[r][c] == 'O')
                    oTotal += 1;
                if (board[r][c] == 'T')
                    hasTHere = true;
            }
            if (xTotal == 4 || xTotal == 3 && hasTHere)
                result = "X won";
            if (oTotal == 4 || oTotal == 3 && hasTHere)
                result = "O won";
        }
        
        //check diagonal
        xTotal = oTotal = 0;
        hasTHere = false;
        for (int r = 0; r < 4; ++r) {
            if (board[r][r] == 'X')
                xTotal += 1;
            if (board[r][r] == 'O')
                oTotal += 1;
            if (board[r][r] == 'T')
                hasTHere = true;
        }
        if (xTotal == 4 || xTotal == 3 && hasTHere)
            result = "X won";
        if (oTotal == 4 || oTotal == 3 && hasTHere)
            result = "O won";
        
        //check second diagonal
        xTotal = oTotal = 0;
        hasTHere = false;
        for (int r = 0; r < 4; ++r) {
            if (board[r][3 - r] == 'X')
                xTotal += 1;
            if (board[r][3 - r] == 'O')
                oTotal += 1;
            if (board[r][3 - r] == 'T')
                hasTHere = true;
        }
        if (xTotal == 4 || xTotal == 3 && hasTHere)
            result = "X won";
        if (oTotal == 4 || oTotal == 3 && hasTHere)
            result = "O won";
         
        if (result.size() == 0) {
            if (total == 16 || total == 15 && hasT)
                result = "Draw";
            else
                result = "Game has not completed";
        }
        //print out
        fprintf (fp2, "Case #%d: %s\n", i + 1, result.c_str());
        
        
    }
    
    return 0;
}


