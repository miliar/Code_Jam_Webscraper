#include <iostream>
#include <string>

using namespace std;

int extraFriends(string levels)
{
    int runningTotal = 0;
    int res = 0;
    for(int i = 0; i < levels.size(); i++) 
    {
        int numPeople = levels[i] - '0';
        //cout << "shyness level " << i << " num people " << numPeople << endl; 
        if(numPeople > 0)
        {
            if(runningTotal < i) 
            {
                res += i - runningTotal;
                runningTotal = i;
            }
            
            runningTotal += numPeople;
        }
    }
    return res;
}

int main()
{
    int tests;
    cin >> tests;
    //cout << tests << endl;
    
    for(int i = 0; i < tests; i++)
    {
        int smax;
        cin >> smax;
        string levels;
        cin >> std::ws;
        getline(cin, levels);
        
        cout << "Case #" << i+1 << ": " << extraFriends(levels) << endl;
    }
    
    return 0;
}