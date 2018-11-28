#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool checkSolution(const vector<int>& S, int Smax, int invitedPeople)
{
    int stoodPeople = invitedPeople;
    for (int i = 0; i <= Smax; ++i)
    {
        if (stoodPeople < i && S[i] > 0)
        {
            return false;
        }
        stoodPeople += S[i];
    }

    return true;
}

int howManyToInvite(const vector<int>& S, int Smax)
{
    int stoodPeople = 0;
    int invitedPeople = 0;
    for (int shynessLevel = 0; shynessLevel <= Smax; ++shynessLevel)
    {
        int N = S[shynessLevel];
        if (stoodPeople < shynessLevel && N > 0)
        {
            invitedPeople += (shynessLevel - stoodPeople);
            stoodPeople += (shynessLevel - stoodPeople);
        }
        stoodPeople += N;
    }
    //cout << checkSolution(S, Smax, invitedPeople) << endl;
    return invitedPeople;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        int Smax;
        cin >> Smax;
        vector<int> S(Smax+1);

        for (int i = 0; i <= Smax; ++i)
        {
            char n;
            cin >> n;
            S[i] = n - '0';
        }

        cout << "Case #" << (t+1) << ": " << howManyToInvite(S, Smax) << endl;

    }
    return 0;
}
