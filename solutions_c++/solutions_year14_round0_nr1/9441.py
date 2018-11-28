#include <cstdio>

using namespace std;

const int EDGE_SIZE = 4;
const int FREQUENCES_LENGTH = 17;

int testsCount;

int A1[EDGE_SIZE][EDGE_SIZE];
int A2[EDGE_SIZE][EDGE_SIZE];

int firstChoise;
int secondChoise;

int frequences[FREQUENCES_LENGTH];

int i,j,t;

int answersCount;
int answer;

void clearFrequences();
void readMatrix(int X[EDGE_SIZE][EDGE_SIZE]);

int main()
{
    scanf("%d\n", &testsCount);

    for (t = 0; t < testsCount; t++) {
        scanf("%d\n", &firstChoise);
        readMatrix(A1);
        scanf("%d\n", &secondChoise);
        readMatrix(A2);

        --firstChoise;
        --secondChoise;

        clearFrequences();
        for (i = 0; i < EDGE_SIZE; i++) {
            ++frequences[A1[firstChoise][i]];
            ++frequences[A2[secondChoise][i]];
        }

        answersCount = 0;
        answer = 0;
        for (i = 1; i < FREQUENCES_LENGTH; i++) {
            if (frequences[i] >= 2) {
                ++answersCount;
                answer = i;
            }
        }

        printf("Case #%d: ", t + 1);
        if (answersCount == 0) {
            printf("Volunteer cheated!\n");
        } else if (answersCount == 1) {
            printf("%d\n", answer);
        } else {
            printf("Bad magician!\n");
        }
    }

    return 0;
}

void clearFrequences()
{
    for (i = 0; i < FREQUENCES_LENGTH; i++) {
        frequences[i] = 0;
    }
}

void readMatrix(int X[EDGE_SIZE][EDGE_SIZE])
{
    for (i = 0; i < EDGE_SIZE; i++) {
        for(j = 0; j < EDGE_SIZE; j++) {
            scanf("%d", &X[i][j]);
        }
        scanf("\n");
    }
    scanf("\n");
}
