/*

Solution - 
    1. Keep a counter of how many people have stood up so far,
       if the count falls below the requirement invite those many
       shy-less friends.
*/

#include <iostream>
#include <string>

using namespace std;

int FindMinNumberOfInvites(int, string&);

int main(void)
{
    int T, c = 1;
    cin >> T;
    while (T--) {
        int Smax;
        string distribution;
        cin >> Smax >> distribution;
        cout << "Case #" << c++ << ": " << FindMinNumberOfInvites(Smax, distribution) << endl;
    }
    return 0;
}

int FindMinNumberOfInvites(int Smax, string& distribution)
{
    int people_stood_up_so_far = 0, invites = 0;
    for (int i = 0; i <= Smax; ++i) {
        if (people_stood_up_so_far < i) {
            invites += i - people_stood_up_so_far;
            people_stood_up_so_far = i + static_cast<int>(distribution.at(i) - '0');
        } else
            people_stood_up_so_far += static_cast<int>(distribution.at(i) - '0');
    }
    return invites;
}

