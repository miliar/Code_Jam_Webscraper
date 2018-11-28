#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i)
    {
        int totalFriends = 0;
        int maxShy;
        string integerString;
        cin >> maxShy >> integerString;
        
        int shynessLevel = 0;
        int totalPeopleStanding = 0;
        
        for (char c : integerString)
        {
            if (totalPeopleStanding < shynessLevel && c != '0')
            {
                totalFriends += shynessLevel - totalPeopleStanding;
                totalPeopleStanding += shynessLevel - totalPeopleStanding;
            }
            
            totalPeopleStanding += (c - '0');
            shynessLevel++;
        }
        cout << "Case #" << i+1 << ": " << totalFriends << endl;
    }
}