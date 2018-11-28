#include <iostream>
#include <fstream>

static int arraySize = 4;

using namespace std;

int main()
{

    ofstream output("output.txt");

    int T = 0;

    ifstream data("A-small-attempt1.in");
    if (!data.is_open()) cout << "Failure";
    data >> T;

    int startGame [T][arraySize][arraySize];
    int endGame [T][arraySize][arraySize];
    int startRow [T];
    int endRow [T];

    int startCard [arraySize];
    int endCard [arraySize];
    // Refers to the starting card setup
    bool matchingCard [arraySize];
    int numMatchingCards = 0;
    int correctCard;

    for (int t = 0; data.good(); t++)
    {
        data >> startRow[t];
        startRow[t]--;
        data >> startGame[t][0][0] >> startGame[t][1][0] >> startGame[t][2][0] >> startGame[t][3][0];
        data >> startGame[t][0][1] >> startGame[t][1][1] >> startGame[t][2][1] >> startGame[t][3][1];
        data >> startGame[t][0][2] >> startGame[t][1][2] >> startGame[t][2][2] >> startGame[t][3][2];
        data >> startGame[t][0][3] >> startGame[t][1][3] >> startGame[t][2][3] >> startGame[t][3][3];
        data >> endRow[t];
        endRow[t]--;
        data >> endGame[t][0][0] >> endGame[t][1][0] >> endGame[t][2][0] >> endGame[t][3][0];
        data >> endGame[t][0][1] >> endGame[t][1][1] >> endGame[t][2][1] >> endGame[t][3][1];
        data >> endGame[t][0][2] >> endGame[t][1][2] >> endGame[t][2][2] >> endGame[t][3][2];
        data >> endGame[t][0][3] >> endGame[t][1][3] >> endGame[t][2][3] >> endGame[t][3][3];
    }



    for (int t = 0; t < T; t++)
    {
        for (int i = 0; i < arraySize; i++)
        {
            startCard [i] = startGame[t][i][startRow[t]];
        }
        for (int i = 0; i < arraySize; i++)
        {
            endCard [i] = endGame[t][i][endRow[t]];
        }

        // Compare the two sets of cards. Cards in both sets are solutions
        for (int i = 0; i < arraySize; i++) matchingCard[i] = false;
        for (int i = 0; i < arraySize; i++)
        {
            for (int j = 0; j < arraySize; j++)
            {
                if (startCard[i]==endCard[j])
                {
                    correctCard = startCard[i];
                    matchingCard[i]=true;
                }
            }
        }

        // Find number of matching cards
        numMatchingCards = 0;
        for (int i = 0; i < arraySize; i++)
        {
            if (matchingCard[i])
            {
                numMatchingCards++;
            }
        }

        // Print the solution
        if (!output.is_open()) cout << "Failure Writing";
        if (numMatchingCards == 0)
        {
            output << "Case #" << t+1 << ": Volunteer cheated!";
        }
        else if (numMatchingCards == 1)
        {
            output << "Case #" << t+1 << ": " << correctCard;
        }
        else
        {
            output << "Case #" << t+1 << ": Bad magician!";
        }
        if(t!=T-1) output << endl;
    }


    return 0;
}
