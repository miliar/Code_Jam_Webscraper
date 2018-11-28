#include <iostream>
#include <vector>

using namespace std;

int printResult(vector<int> & diners)
{
    int stops = 0;
    
    int max = 0;
    int maxIndex;
    for(int i = 0; i < diners.size(); i++)
    {
        if(diners[i] > max)
        {
            max = diners[i];
            maxIndex = i;
        }
    }
    int result = max + stops;
    int bestResult = result;
    if( max > 3 )
    {
        max = (max - 2)/2; //tyle moze byc podzialow
        for(int i = 1; i <= max; i++)
        {
            vector<int> newDiners = vector<int>(diners);
            newDiners.push_back( i+1 );
            newDiners[maxIndex] = newDiners[maxIndex] - i - 1;
            result = printResult(newDiners) + 1;
            if(result < bestResult)
                 bestResult = result;
        }
    }
    return bestResult;
}

int main()
{
    int T, pancakes;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        int nonEmpty;
        cin >> nonEmpty;
        vector<int> diners = vector<int>();
        for(int j = 0; j < nonEmpty; j++)
        {
            cin >> pancakes;
            diners.push_back(pancakes);
        }        
        cout << "Case #" << i+1 << ": " << printResult(diners) << endl;
    }
}


