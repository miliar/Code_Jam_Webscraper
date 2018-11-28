#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <conio.h>

using namespace std;

typedef enum
{
    Move_X = (int)'X',
    Move_O = (int)'O',
    Move_Dot = (int)'.',
    Move_T = (int)'T',
    
    Op_X_Won,
    Op_O_Won,
    Op_Draw,
    Op_Not_Over,
};

int inputBox[4][4];
bool verifiedBox[4][4];
bool fourNeigh[4];
FILE *fsIn, *fsOut;

void GetNextTestCase(void);
bool checkAllDir(int curr_i, int curr_j, int *delX, int *delY);
int FindOutput();

int main(int argc, char *argv[])
{
    cout << "Start!" << endl;
    //fsIn = fopen("sampleInput2.txt", "r");
    fsIn = fopen("A-small-attempt1.in", "r");
    
    fsOut = fopen("A-small.out", "w");

    int numCases = 10;
    
    char tempCh[100];
    
    //for(int i=0; i<16; i++)
    //    verifiedBox[i] = 0;
    
    fscanf ( fsIn, "%d\n", &numCases);
    
    for(int i=0; i<numCases; i++)
    {
        GetNextTestCase();
        fprintf(fsOut, "Case #%d: ", i+1);
        
        switch( FindOutput() )
        {
                case Op_X_Won:
                     fprintf(fsOut, "X won\n");
                     break;
                case Op_O_Won:
                     fprintf(fsOut, "O won\n");
                     break;
                case Op_Draw:
                     fprintf(fsOut, "Draw\n");
                     break;
                case Op_Not_Over:
                     fprintf(fsOut, "Game has not completed\n");
                     break;
        }
        
    }
    
    cout << "Finished " << numCases << " " << fsIn << " "  << endl;
    fclose(fsIn);
    getch();
    return EXIT_SUCCESS;
}

void GetNextTestCase()
{
     int cnt = 0;
     for(int i=0; i<4; i++)
     {
             fscanf( fsIn, "%c%c%c%c\n", &inputBox[i][0], &inputBox[i][1], &inputBox[i][2], &inputBox[i][3]);
             //cout << inputBox[cnt] << " " << inputBox[cnt+1] << " " << inputBox[cnt+2] << " " << inputBox[cnt+3] << endl;
     }
     
     //cout << endl;
     fscanf( fsIn, "\n");
     
     return;
}

// Get the direction in which similar item is present
// currItem will be changed if the base item is 'T'
bool checkAllDir(int curr_i, int curr_j, int *delX, int *delY, int *currItem)
{
     int i, j;
     bool result = false;
     
     // Dir 1 => Right
     i = curr_i;
     j = curr_j + 1;
     
     if( (i >= 0 && i <4) &&
         (j >= 0 && j <4) &&
         (fourNeigh[0] == 0) )
         {
            fourNeigh[0] = 1;
            if( (inputBox[i][j] == inputBox[curr_i][curr_j]) ||
                (inputBox[i][j] == Move_T) ||
                (inputBox[curr_i][curr_j] == Move_T) )
            {
                *delX = 0; *delY = 1;
                result = true;
                goto done;
            }
         }
     
     // Dir 2 => Right-Down
     i = curr_i + 1;
     j = curr_j + 1;
     
     if( (i >= 0 && i <4) &&
         (j >= 0 && j <4) &&
         (fourNeigh[1] == 0) )
         {
            fourNeigh[1] = 1;
            if( (inputBox[i][j] == inputBox[curr_i][curr_j]) ||
                (inputBox[i][j] == Move_T) ||
                (inputBox[curr_i][curr_j] == Move_T) )
            {
                *delX = 1; *delY = 1;
                result = true;
                goto done;
            }
         }
         
     // Dir 3 => Down
     i = curr_i + 1;
     j = curr_j;
     
     if( (i >= 0 && i <4) &&
         (j >= 0 && j <4) &&
         (fourNeigh[2] == 0) )
         {
            fourNeigh[2] = 1;
            if( (inputBox[i][j] == inputBox[curr_i][curr_j]) ||
                (inputBox[i][j] == Move_T) ||
                (inputBox[curr_i][curr_j] == Move_T) )
            {
                *delX = 1; *delY = 0;
                result = true;
                goto done;
            }
         }
         
     // Dir 4 => Left-Down
     i = curr_i + 1;
     j = curr_j - 1;
     
     if( (i >= 0 && i <4) &&
         (j >= 0 && j <4) &&
         (fourNeigh[3] == 0) )
         {
            fourNeigh[3] = 1;
            if( (inputBox[i][j] == inputBox[curr_i][curr_j]) ||
                (inputBox[i][j] == Move_T) ||
                (inputBox[curr_i][curr_j] == Move_T) )
            {
                *delX = 1; *delY = -1;
                result = true;
                goto done;
            }
         }
     
     done:
     if( (result) &&
         (inputBox[curr_i][curr_j] == Move_T) )
     {
         *currItem = inputBox[i][j];
     }
     
     // From the current point in all directions no matching object
     return result;
}

int FindOutput()
{
    int pos = 0;
    int dir = 0;
    int currSeqCount = 0, currentItem = 0, nextItem = 0;
    bool resultFound = 0, dotsPresent = 0;
    int dirX=0, dirY=0;
    int currI, currJ;
    
    memset(verifiedBox, false, sizeof(verifiedBox));
    int i, j;
    
    for(i=0; i<4; i++)
    {
            for(j=0; j<4; j++)
            {
                    if(verifiedBox[i][j])
                        continue;
                        
                    if(inputBox[i][j] == Move_Dot)
                    {
                        dotsPresent = true;
                        continue;
                    }
                        
                    currentItem = inputBox[i][j];
                    
                    memset(fourNeigh, 0, sizeof(fourNeigh));
                    
                    while( checkAllDir(i, j, &dirX, &dirY, &currentItem ) ) // dirX & dirY gives valid direction from current //!resultFound && !seqBroken)
                    {
                           currSeqCount = 0;
                           currI = i + dirX; currJ = j + dirY;
                           //nextItem = currentItem;

                           while ( (currentItem == inputBox[currI][currJ]) ||
                                   (Move_T == inputBox[currI][currJ]) )
                           {
                                 currSeqCount++;
                                 
                                 currI += dirX;
                                 currJ += dirY;
                                 
                                 if( (currI < 0 || currI >=4) ||
                                     (currJ < 0 || currJ >=4) )
                                     break;
                                 
                                 //nextItem = inputBox[currI+dirX][currJ+dirY];
                                     
                           } // loop in direction checking
                           
                           if(currSeqCount == 3)
                           {
                                 resultFound = true;
                                 break;
                           }
                           
                           currentItem = inputBox[i][j];
                           
                    } // loop for each directions
                    
                    if(resultFound)
                        break;                    
            }
            
            if(resultFound)
                break;
    }
    
    if(resultFound)
    {
        if(currentItem == Move_X)
            return Op_X_Won;
        
        else if(currentItem == Move_O)
            return Op_O_Won;
    }
    else
    {
        if(dotsPresent)
            return Op_Not_Over;
        else
            return Op_Draw;
    }
            
    
    return Op_Draw;        // This will never happen
}
     

