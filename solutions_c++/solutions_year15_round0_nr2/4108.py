#include <iostream>
#include <vector>

using namespace std;

void printPlates(vector<int> const & platesPerNumber)
{
    for(int i = platesPerNumber.size() - 1; i >= 0; i--)
        cout << "n° pancakes = " << i << " for " << platesPerNumber[i] << " diners" << endl; 
}

int possibleGainDividingMaxNumber(vector<int> & platesPerNumber, int n) 
{
    int biggest = 0;
    int quantityBiggest = 0;
    
    for(int i = platesPerNumber.size() - 1; i >= 0; i--)
    {
        if(platesPerNumber[i] != 0)
        {
            biggest = i;
            quantityBiggest = platesPerNumber[i];
            break;
        }
    }
    
    if( (n-1)*quantityBiggest < biggest - (biggest + n - 1)/n )
    {
        platesPerNumber[biggest] = 0;
        
        vector<int> nums(n,0);
        for(int i = 0; i < biggest; i++)
        {
            nums[i%n]++;
        }
        for(int n : nums)
            platesPerNumber[n] += quantityBiggest;
        
        return (n-1)*quantityBiggest;
    }
    return 0;
}

int getBiggest(vector<int> const & platesPerNumber)
{
    for(int i = platesPerNumber.size() - 1; i >= 0; i--)
    {
        if(platesPerNumber[i] != 0)
            return i;
    }
    return 0;
}

int minEatingTime(vector<int> platesPerNumber)
{
    int biggest = getBiggest(platesPerNumber);
    int min = biggest;
    for(int i = 2; i <= biggest; i++)
    {
        vector<int> copy = platesPerNumber;
        int timeForGain = possibleGainDividingMaxNumber(copy, i);
        if(timeForGain > 0) 
        {
            int val = timeForGain + minEatingTime(copy);
            if(min > val)
            {
                min = val;
            }
        }
    }
    return min;
}

int eatingTime(vector<int> pancakes, int maxNumber)
{
    vector<int> platesPerNumber(maxNumber+1, 0);
    for(int p : pancakes)
        platesPerNumber[p]++;
    
    //printPlates(platesPerNumber);
    
    /*int res = getBiggest(platesPerNumber);
    int specialMinutes = 0;
    
    int timeForGain = possibleGainDividingMaxNumber(platesPerNumber);
    
    while(timeForGain != 0)
    {
        //printPlates(platesPerNumber);
        
        specialMinutes += timeForGain;
        if(res > getBiggest(platesPerNumber) + specialMinutes)
            res = getBiggest(platesPerNumber) + specialMinutes;
        
        timeForGain = possibleGainDividingMaxNumber(platesPerNumber);
    }*/
    
    return minEatingTime(platesPerNumber);
}

int main()
{
    int tests;
    cin >> tests;
    //cout << tests << endl;
    
    for(int i = 0; i < tests; i++)
    {
        //cout << i << endl;
        int filled;
        cin >> filled;
        vector<int> pancakes;
        int maxPj = 0;
        for(int j = 0; j < filled; j++)
        {
            int pj;
            cin >> pj;
            pancakes.push_back(pj);
            if(maxPj < pj)
                maxPj = pj;
        }
        
        cout << "Case #" << i+1 << ": " << eatingTime(pancakes, maxPj) << endl;
    }
    
    return 0;
}