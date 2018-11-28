#include <cstdio>

using namespace std;
int t;
int s;
int numberOfPersons;
int numberOfFriends;
int caseNumber;
char fr[1005];

int main() {
    freopen("ovation.in","r",stdin);
    freopen("ovation.out","w",stdout);
    scanf("%d",&t);
    caseNumber = 0;
    for (; t; --t)
    {
        ++caseNumber;
        numberOfPersons = 0;
        numberOfFriends = 0;
        scanf("%d %s",&s,fr);
        numberOfPersons = fr[0] - 48;
        for (int i = 1; fr[i] != 0; ++i)
        {
            if (numberOfPersons >=i)
            {
                numberOfPersons += fr[i] - 48;
            }
            else
            {
                ++numberOfFriends;
                ++numberOfPersons;
                numberOfPersons += fr[i] - 48;
            }
        }
        printf("Case #%d: %d\n",caseNumber,numberOfFriends);
    }
    return 0;
}
