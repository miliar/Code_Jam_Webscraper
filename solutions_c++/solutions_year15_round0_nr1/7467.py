#include <iostream>
#include <string>

using namespace std;

int main()
{
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++)
    {
        int sMax;
        string audience;
        cin >> sMax >> audience;
        int total = audience[0] - '0', numNeeded = 0;
        for (int j = 1; j < sMax + 1; j++)
        {
            if (audience[j] > 0 && total < j)
            {
                numNeeded += (j - total);
                total += (audience[j] - '0') + j - total;
            }
            else
                total += (audience[j] - '0');
        }
        cout << "Case #" << i << ": " << numNeeded << endl;
    }
    return 0;
}
