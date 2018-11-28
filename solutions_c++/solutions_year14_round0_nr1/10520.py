#include <iostream>
#include <fstream>

using namespace std;

#define BAD (0)
#define INCOMPLETE (-1)

int main()
{
    ifstream fin("A-small-attempt0.in");
    int numTestCases;
    int board[4][4];
    int possibleCards[4];
    int volunteerAnswer;
    int theActualCard = INCOMPLETE;
    bool cardFound = false;
    
    // get number of test cases
    fin >> numTestCases;
    
    for(int i=0; i < numTestCases; ++i)
    {
        // initialize variables
        theActualCard = INCOMPLETE;
        cardFound = false;
        
        // get volunteer's first answer
        fin >> volunteerAnswer;
        --volunteerAnswer;
        
        // read board state
        for(int j=0; j < 4; ++j)
        {
            for(int k=0; k < 4; ++k)
            {
                fin >> board[j][k];
            }
        }
        // board read
        
        // extract possible cards
        for(int j=0; j < 4; ++j)
        {
            possibleCards[j] = board[volunteerAnswer][j];
        }
        // possible cards noted
        
        // get volunteer's second answer
        fin >> volunteerAnswer;
        --volunteerAnswer;
        
        // read final board state
        for(int j=0; j < 4; ++j)
        {
            for(int k=0; k < 4; ++k)
            {
                fin >> board[j][k];
            }
        }
        // board read
        
        // check final board against possible answers
        for(int j=0; j < 4; ++j)
        {
            for(int k=0; k < 4; k++)
            {
                if(board[volunteerAnswer][j] == possibleCards[k])
                {
                    // if it's already been found (multiple possibilities)
                    if(cardFound)
                        theActualCard = BAD;
                    else
                    {

                        // set the flag
                        cardFound = true;
                        // note the card
                        theActualCard = possibleCards[k];
                    }
                }
            }
        }
        // done processing
        
        // print result
        cout << "Case #" << i+1 << ": ";
        if(!cardFound)
            cout << "Volunteer cheated!";
        else
        {
            if(theActualCard == BAD)
                cout << "Bad magician!";
            else
                cout << theActualCard;
        }
        
        cout << endl;
    }
    
    return 0;
}
