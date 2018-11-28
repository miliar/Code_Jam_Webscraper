#include <iostream>
#include <vector>
#include <string>

int main()
{
    using namespace std;

    unsigned int caseCount = 0;
    cin >> caseCount;

    for(unsigned int c = 0; c < caseCount; ++c)
    {
        vector<unsigned int> shynessCounts;

        unsigned int maxShyness = 0;
        cin >> maxShyness;
        shynessCounts.resize(maxShyness + 1);

        for(unsigned int& i : shynessCounts)
        {
            char c = '0';
            cin >> c;
            i = c - '0';
        }

        unsigned int currentCount = 0;
        unsigned int minFriends = 0;

        for(unsigned int i = 0; i < shynessCounts.size(); ++i)
        {
            unsigned int temp = i > currentCount ? i - currentCount : 0;
            minFriends = temp > minFriends ? temp : minFriends;
            currentCount += shynessCounts[i];
        }

        cout << "Case #" << c+1 << ": " << minFriends << '\n';
    }
}
