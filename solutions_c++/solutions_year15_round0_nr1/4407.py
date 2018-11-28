#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for(int k=1; k<=t; k++)
    {
        int smax;
        cin >> smax;
        string s;
        cin >> s;

        int peopleStanding = 0;
        int peopleInvited = 0;

        for(int i=0; i<s.length(); i++)
        {
            if(peopleStanding < i)
                peopleInvited += (i-peopleStanding),
                peopleStanding += (i-peopleStanding);

            peopleStanding += s[i]-'0';
        }

        cout << "Case #" << k << ": " << peopleInvited << "\n";
    }

    return 0;
}
