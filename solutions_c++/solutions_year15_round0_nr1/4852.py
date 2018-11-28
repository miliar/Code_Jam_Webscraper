#include <iostream>
#include <string>
#include <cassert>

using namespace std;

int solve(int maxS, string& hist)
{
    int nonZeroIndex = -1;
    int count = 0;
    int invite = 0;
    for (int shyness = 0; shyness <= maxS; shyness++)
    {
        int people = hist.at(shyness) - '0';
        if (count >= shyness)
        {
            count += people;
        }
        else
        {
            int shouldInvite = shyness - count;
            invite += shouldInvite;
            count += people + shouldInvite;
        }
    }
    return invite;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int maxS;
        string hist;
        cin >> maxS;
        cin >> hist;
        assert(maxS+1 == hist.length());
        cout << "Case #" << i+1 << ": " << solve(maxS, hist) << endl;
    }
    return 0;
}