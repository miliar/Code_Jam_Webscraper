#include <iostream>
#include <vector>

using namespace std;

int printResult(vector<int> & audience)
{
    int clapping = 0;
    int result = 0;
    for(int i = 0; i < audience.size(); i++)
    {
        if(i > clapping)
        {
            result++;
            clapping++;
            i--;
            continue;
        }
        clapping += audience[i];
    }
    return result;
}

int main()
{
    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        int Smax;
        cin >> Smax;
        vector<int> audience = vector<int>();
        cin.get();
        for(int j = 0; j <= Smax; j++)
        {
            int Si = cin.get() - '0';
            audience.push_back(Si);
        }
        cin.get();
        
        cout << "Case #" << i+1 << ": " << printResult(audience) << endl;
    }
}

