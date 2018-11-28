#include <cstdio>
#include <cstring>

// for large problem set
const int MAX_LETTERS = 10001;

// answer matrix
char answers[256][256];
int sign[256][256];

// countTestCases should be less or equal to 100
int countTestCases = 0;

// the amount of audience for different shyness level
char input[MAX_LETTERS];

void init() {

    memset(answers, 0, sizeof(char) * 256 * 256);

    answers['1']['1'] = '1';
    answers['1']['i'] = 'i';
    answers['1']['j'] = 'j';
    answers['1']['k'] = 'k';

    answers['i']['1'] = 'i';
    answers['i']['i'] = '1'; // '-1'
    answers['i']['j'] = 'k';
    answers['i']['k'] = 'j'; // '-j'

    answers['j']['1'] = 'j';
    answers['j']['i'] = 'k'; // '-k'
    answers['j']['j'] = '1'; // '-1'
    answers['j']['k'] = 'i';

    answers['k']['1'] = 'k';
    answers['k']['i'] = 'j';
    answers['k']['j'] = 'i'; // '-i'
    answers['k']['k'] = '1'; // '-1'

    for (int i = 0; i < 256; ++i) {
        for (int j = 0; j < 256; ++j) {
            sign[i][j] = 1;
        }
    }

    sign['i']['i'] = -1;
    sign['i']['k'] = -1;
    sign['j']['i'] = -1;
    sign['j']['j'] = -1;
    sign['k']['j'] = -1;
    sign['k']['k'] = -1;
}

bool findK(int beginIndex, int countLetters, int countRepeatTimes) {

    char currentLetter = '1';
    int currentSign = 1;

    // find 'k' until the end
    for (int i = beginIndex; i < countLetters * countRepeatTimes; ++i) {
        const char nextLetter = input[i % countLetters];

        currentSign = currentSign * sign[currentLetter][nextLetter];
        currentLetter = answers[currentLetter][nextLetter];
    }

    return currentLetter == 'k' && (currentSign > 0);
}

bool findJAndK(int beginIndex, int countLetters, int countRepeatTimes) {

    char currentLetter = '1';
    int currentSign = 1;

    // find 'j'
    for (int i = beginIndex; i < countLetters * countRepeatTimes; ++i) {
        const char nextLetter = input[i % countLetters];

        currentSign = currentSign * sign[currentLetter][nextLetter];
        currentLetter = answers[currentLetter][nextLetter];

        if (currentLetter == 'j' && (currentSign > 0)) {
            return findK(i + 1, countLetters, countRepeatTimes);
        }
    }

    return false;
}

bool solve(int caseNum, int countLetters, int countRepeatTimes) {

    char currentLetter = '1';
    int currentSign = 1;

    // find possible strings to convert to 'i'
    for (int i = 0; i < countLetters * countRepeatTimes; ++i) {
        const char nextLetter = input[i % countLetters];

        currentSign = currentSign * sign[currentLetter][nextLetter];
        currentLetter = answers[currentLetter][nextLetter];

        //printf("i = %d, currentLetter = %c, currentSign = %d\n", i, currentLetter, currentSign);

        if (currentLetter == 'i' && (currentSign > 0)) {
            if (findJAndK(i + 1, countLetters, countRepeatTimes)) {
                return true;
            }
        }
    }

    return false;
}

int main() {

    init();

    scanf("%d", &countTestCases);

    int i = 0;

    for ( ; i < countTestCases; ++i) {

        int countLetters = 0;
        int countRepeatTimes = 0;

        scanf("%d %d", &countLetters, &countRepeatTimes);
        scanf("%s", input);

        bool result = solve(i, countLetters, countRepeatTimes);

        printf("Case #%d: %s\n", i + 1, result ? "YES" : "NO");
    }

    return 0;
}
