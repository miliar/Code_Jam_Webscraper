// if last line is not empty, it will stuck
#include <iostream>
#include <fstream>
#include <cctype>
using namespace std;

int findHowDeep(char* data, char symbol, int index)
{
    for(int i=0; i<=index; i++)
    {
        if(data[i] != symbol)
        {
            return i-1;
        }
    }
    return index;
}

void flip(char* data, int start, int ending, char symbol)
{
    for(int i=start; i<=ending; i++)
    {
        data[i] = symbol;
    }
}

bool notFulfilled(char* data, int index)
{
    for(int i=0; i<=index; i++)
    {
        if(data[i] != '+')
            return true;
    }
    return false;
}

int main()
{
    int numCases;
    int maxIndex;
    char dataArray[200];
    int thisDeep;
    int flipCount;

    ifstream inData;
    ofstream outData;

    inData.open("B-large.in");
    outData.open("B-large-answer.txt");

    inData >> numCases;

    for(int i=0; i<numCases; i++)
    {
        inData >> dataArray;

        // to determine max index where dataArray currently can be accessed (char with + or -)
        for(int j=0; j<200; j++)
        {
            if(dataArray[j] != '+' && dataArray[j] != '-')
            {
                maxIndex = j-1;
                break;
            }
        }
        flipCount = 0;
        while(notFulfilled(dataArray, maxIndex))
        {
            if(dataArray[0] == '+')
            {
               thisDeep = findHowDeep(dataArray, '+', maxIndex);
                // flip all + in front of -
                flip(dataArray, 0, thisDeep, '-');
            }
            else
            {
                thisDeep = findHowDeep(dataArray, '-', maxIndex);
                // flip all - in front
                flip(dataArray, 0, thisDeep, '+');
            }
            flipCount += 1;
        }
        outData << "Case #" << i+1 << ": " << flipCount << endl;
    }

    inData.close();
    outData.close();

    return 0;
}
