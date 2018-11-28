#include <iostream>

using namespace std;

bool pancakes[100];

void setStack(bool * pancakes, string pancakeInput)
{
    for(int i = 0; i < pancakeInput.size(); i++)
        if(pancakeInput[i] == '+') pancakes[i] = true;
            else pancakes[i] = false;
}

void reduceRange(bool * pancakes, int & searchRange)
{
    for(int i = searchRange-1; i >= 0; i--)
    {
        if(pancakes[i] == false)
        {
            searchRange = i+1;
            break;
        }
    }
}

void flipStack(bool * pancakes, int searchRange)
{
    if(searchRange == 1)
    {
        if(pancakes[0] == true) pancakes[0] = false;
            else pancakes[0] = true;
        return;
    }

    //if(searchRange % 2 == 1) searchRange+1;

    for(int i = 0; i < searchRange / 2; i++)
    {
        int tmp;
        tmp = pancakes[i];
        pancakes[i] = pancakes[searchRange-1-i];
        pancakes[searchRange-1-i] = tmp;

        if(pancakes[i] == true) pancakes[i] = false;
            else pancakes[i] = true;

        if(pancakes[searchRange-1-i] == true) pancakes[searchRange-1-i] = false;
            else pancakes[searchRange-1-i] = true;
    }

    if(searchRange % 2 == 1)
    {
        if(pancakes[searchRange/2] == true) pancakes[searchRange/2] = false;
            else pancakes[searchRange/2] = true;
    }
}

int minusDistance(bool * pancakes, int searchRange)
{
    for(int i = searchRange-1; i >= 0; i--)
    {
        if(pancakes[i] == true)
            return i+1;
    }
}

bool finish(bool * pancakes, int pancakesStackLength)
{
    for(int i = 0; i < pancakesStackLength; i++)
    {
        if(pancakes[i] == false) return false;
    }
    return true;
}

int main()
{
    int t;
    cin >> t;

    string pancakeInput;

    for(int i = 0; i < t; i++)
    {
        int moveCount = 0;
        cin >> pancakeInput;

        int searchRange = pancakeInput.size();
        int pancakesStackLength = searchRange;

        setStack(pancakes, pancakeInput);
        if(finish(pancakes,pancakesStackLength))
        {
            cout << "Case #" << i+1 << ": " << moveCount << endl;
            continue;
        }

        while(true)
        {
            reduceRange(pancakes, searchRange);

            if(pancakes[0] == false)
            {
                flipStack(pancakes,searchRange);
                moveCount++;
            } else {
                    flipStack(pancakes,minusDistance(pancakes,searchRange));
                    flipStack(pancakes,searchRange);
                    moveCount+=2;
                }
            if(finish(pancakes,pancakesStackLength)) break;
        }
        cout << "Case #" << i+1 << ": " <<  moveCount << endl;
    }
    return 0;
}
