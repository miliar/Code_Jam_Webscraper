// if last line is not empty, it will stuck
#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

void digitToArray(int num, int* digitArray)
{
    char numberHolder[25];
    itoa(num, numberHolder, 10);
    for(int k=0; k<25; k++)
    {
        if(numberHolder[k] == '\0')
        {
            break;
        }
        digitArray[numberHolder[k] - '0'] += 1;
    }
    delete numberHolder;
}

bool fulfilled(int* digitArray)
{
    for(int l=0; l<10; l++)
    {
        if(digitArray[l] == 0)
            return false;
    }
    return true;
}

int main()
{
    int numCases;
    int multiplier;
    int number;
    int digitArray[10] = {};
    int n;

    ifstream inData;
    ofstream outData;

    inData.open("A-large.in");
    outData.open("A-large-answer.txt");

    inData >> numCases;

    for(int i=0; i<numCases; i++)
    {
        inData >> number;

        multiplier = 1;

        for(int j=0; j<10; j++)
        {
            digitArray[j] = 0;
        }

        while(true && number != 0)
        {
            n = multiplier * number;
            digitToArray(n, digitArray);
            if(fulfilled(digitArray))
                break;
            multiplier += 1;
        }

        if(number == 0)
        {
            outData << "Case #" << i+1 << ": INSOMNIA" << endl;
        }
        else
        {
            outData << "Case #" << i+1 << ": " << n << endl;
        }
    }

    inData.close();
    outData.close();

    return 0;
}
