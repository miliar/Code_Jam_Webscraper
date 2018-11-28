#include <iostream>

using namespace std;

int main()
{
    int testCaseCount = 0;
    cin >> testCaseCount;

    for (int i = 0; i < testCaseCount; ++i)
    {
        int sMax = 0;
        string sStr;
        cin >> sMax >> sStr;

        int inviteCount = 0;
        int peopleStandingCount = 0;
        for (int k = 0; k <= sMax; ++k)
        {
            int s = sStr[k] - '0';
            if (s != 0 && peopleStandingCount < k) {
                inviteCount += k - peopleStandingCount;
                peopleStandingCount += inviteCount;
            }
            peopleStandingCount += s;
        }

        cout << "Case #" << i + 1 << ": " << inviteCount << endl;
    }
    return 0;
}
