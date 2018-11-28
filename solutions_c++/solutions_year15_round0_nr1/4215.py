#include <cstdio>
#include <cstring>

// for large problem set
const int MAX_SHY_LEVEL = 1001;

// countTestCases should be less or equal to 100
int countTestCases = 0;

// the amount of audience for different shyness level
char countAudience[MAX_SHY_LEVEL];

void solve(int caseNum, int shynessLevel) {
    int countInviteFriends = 0;
    int countAlreadyJoinedAudience = 0;

    for (int currentShyLevel = 0; currentShyLevel <= shynessLevel; ++currentShyLevel) {

        countAlreadyJoinedAudience += countAudience[currentShyLevel] - '0';

        if (countInviteFriends + countAlreadyJoinedAudience > currentShyLevel) {
            continue;
        }

        ++countInviteFriends;
    }

    printf("Case #%d: %d\n", caseNum + 1, countInviteFriends);
}


int main() {

    memset(countAudience, 0, sizeof(char) * MAX_SHY_LEVEL);

    scanf("%d", &countTestCases);

    int i = 0;

    for ( ; i < countTestCases; ++i) {
        int currentShynessLevel = 0;

        scanf("%d %s", &currentShynessLevel, countAudience);

        solve(i, currentShynessLevel);
    }

    return 0;
}
