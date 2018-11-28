/* 
 * File:   main.cpp
 * Author: Freeaxle
 *
 * Created 12/04/2014
 *
 */

#include <cstdlib>
#include <fstream>
#include <string>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv)
{
    const int rowLength = 4;
    const int rowLengthTwice = 8;
    const int columnlength = 4;
    const int possibleAnswers = 8;
    std::string answerAmbiguous("Bad magician!");
    std::string answerNone("Volunteer cheated!");
    std::string answerPreamble("Case #");
    
    std::ifstream input("input.txt");
    std::ofstream answers("Answers.txt");
    
    int cases = 0;
    int inputDump = 0;
    
    input >> cases;
    for(int i_cases = 0;i_cases < cases;i_cases++)
    {
        int x_cardCurrent = 0;
        int cardsInRow[possibleAnswers] = {0};
        int answerOnlyOne = 0;
        int rowChoice = 0;
        int answerQuantity = 0;   
        
        for(int i_cardArrangments = 0;i_cardArrangments < 2;i_cardArrangments++)
        {
            input >> rowChoice;
            for(int i_row = 0;i_row < rowLength;i_row++)
            {
                for(int i_columns = 0;i_columns < columnlength;i_columns++)
                {
                    if(i_row == (rowChoice - 1))
                    {
                        input >> cardsInRow[x_cardCurrent];
                        x_cardCurrent++;
                    }
                    else
                    {
                        input >> inputDump;
                    }
                }
            }
        }
        
        for(int i_firstRow = 0; i_firstRow < rowLength;i_firstRow++)
        {
            for(int i_secondRow = rowLength;i_secondRow < rowLengthTwice;i_secondRow++)
            {
                if(cardsInRow[i_firstRow] == cardsInRow[i_secondRow])
                {
                    answerOnlyOne = cardsInRow[i_firstRow];
                    answerQuantity++;
                }
            }
        }
        
        answers << answerPreamble;
        answers << (i_cases + 1);
        answers << ": ";
        if(answerQuantity == 0)
        {
            answers << answerNone;
        }
        else if(answerQuantity == 1)
        {
            answers << answerOnlyOne;
        }
        else
        {
            answers << answerAmbiguous;
        }
        
        answers << std::endl;
    }
    return 0;
}

