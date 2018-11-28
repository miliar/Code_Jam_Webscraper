/*
G only in EIGHT
U in FOUR
W in TWO
X in SIX
Z only in ZERO
-
F in FOUR, FIVE
H only in THREE, EIGHT
S in SIX, SEVEN
V in FIVE, SEVEN
--
T in TWO, THREE, EIGHT
N in ONE, SEVEN, NINE
R in ZERO, THREE, FOUR
-
I in FIVE, SIX, EIGHT, NINE
O in ZERO, ONE, TWO, FOUR
-
E in ALL but TWO, FOUR, SIX


ALL: ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>



//#define MY_DEBUG

#ifdef MY_DEBUG
    #define dout std::cout
    // See http://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html
    #define dprintf(...) printf(__VA_ARGS__)
#else
    #define dout 0 && std::cout
    #define dprintf(...) 0 && printf(__VA_ARGS__)
#endif
//#define dprintf 0 && printf


int numDigitsEncountered[10];

#define S_LEN_MAX 2000
char S[S_LEN_MAX + 1];

#define NUM_LETTERS ('Z' - 'A' + 1)
int numLetters[NUM_LETTERS];
int numDigits[10];
int N;
char *strD[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool backFinished = false;


//bool allEncountered;
inline bool AllEncountered() {
    for (int i = 0; i < NUM_LETTERS; i++)
        if (numLetters[i] > 0)
            return false;

    return true;
}

inline bool Bad() {
    for (int i = 0; i < NUM_LETTERS; i++)
        if (numLetters[i] < 0)
            return true;

    return false;
}


void Back();

#define Compute(index) \
    { \
    lenStrD = strlen(strD[index]); \
    numDigits[index]++; \
    for (j = 0; j < lenStrD; j++) \
       numLetters[strD[index][j] - 'A']--; \
    if (!Bad()) { \
      Back(); \
      if (backFinished) \
          return; \
    } \
    numDigits[index]--; \
    for (j = 0; j < lenStrD; j++) \
       numLetters[strD[index][j] - 'A']++; \
    }




void Back() {
    int i, j;
    int lenStrD;

    if (AllEncountered()) {
        dprintf("Finished\n");
        backFinished = true;

        return;
    }

    //for (i = 0; i < N; i++) {
    {
        if (numLetters['F' - 'A'] > 0) {
            Compute(4);
            Compute(5);
        }
        if (numLetters['H' - 'A'] > 0) {
            Compute(3);
            Compute(8);
        }
        if (numLetters['S' - 'A'] > 0) {
            Compute(6);
            Compute(7);
        }
        if (numLetters['V' - 'A'] > 0) {
            Compute(5);
            Compute(7);
        }

        if (numLetters['T' - 'A'] > 0) {
            Compute(2);
            Compute(3);
            Compute(8);
        }
        if (numLetters['N' - 'A'] > 0) {
            Compute(1);
            Compute(7);
            Compute(9);
        }
        if (numLetters['R' - 'A'] > 0) {
            Compute(0);
            Compute(3);
            Compute(5);
        }

        if (numLetters['I' - 'A'] > 0) {
            Compute(5);
            Compute(6);
            Compute(8);
            Compute(9);
        }
        if (numLetters['O' - 'A'] > 0) {
            dprintf("ZERO\n");
            Compute(0);
            dprintf("Finished ZERO\n");

            dprintf("ONE\n");
            Compute(1);
            dprintf("Finished ONE\n");

            Compute(2);

            Compute(4);
        }

        if (numLetters['E' - 'A'] > 0) {
            Compute(0);
            Compute(1);
            Compute(3);
            Compute(5);
            Compute(7);
            Compute(8);
            Compute(9);
        }
        /*
        if (S[i] == 'G') {
            taken[i] = 1000 + 8;
        }
        else
        if (S[i] == 'U')
            taken[i] = 1000 + 4;
        else
        if (S[i] == 'X')
            taken[i] = 1000 + 6;
        else
        if (S[i] == 'Z')
            taken[i] = 1000 + 0;
        */

        /*
        Compute(res);
        if (AllEncountered()) {
            //dprintf("i = %d\n", i);

            //printf("Last number named = %d\n", res);
        }
        */
   }
}

void DoIt(char *S) {
    int i, j;

    memset(numDigits, 0, sizeof(int) * 10);
    memset(numLetters, 0, sizeof(int) * NUM_LETTERS);

    N = strlen(S);
    for (i = 0; i < N; i++)
        numLetters[S[i] - 'A']++;

    for (i = 0; i < N; i++) {
        //printf("%ld\n", res);

        if (numLetters['G' - 'A'] > 0) {
            numDigits[8]++;
            int lenStrD = strlen(strD[8]);
            for (j = 0; j < lenStrD; j++)
                numLetters[strD[8][j] - 'A']--;
        }
        else
        if (numLetters['U' - 'A'] > 0) {
            numDigits[4]++;
            int lenStrD = strlen(strD[4]);
            for (j = 0; j < lenStrD; j++)
                numLetters[strD[4][j] - 'A']--;
        }
        else
        if (numLetters['W' - 'A'] > 0) {
            numDigits[2]++;
            int lenStrD = strlen(strD[2]);
            for (j = 0; j < lenStrD; j++)
                numLetters[strD[2][j] - 'A']--;
        }
        else
        if (numLetters['X' - 'A'] > 0) {
            numDigits[6]++;
            int lenStrD = strlen(strD[6]);
            for (j = 0; j < lenStrD; j++)
                numLetters[strD[6][j] - 'A']--;
        }
        else
        if (numLetters['Z' - 'A'] > 0) {
            numDigits[0]++;
            int lenStrD = strlen(strD[0]);
            for (j = 0; j < lenStrD; j++)
                numLetters[strD[0][j] - 'A']--;
        }
    }

    backFinished = false;
    Back();

    /*
    printf("S = ");
    for (i = 0; i < 10; i++)
        //printf("%d ", taken[i]);
        printf("%d:%d ", i, numDigits[i]);
    printf(",    ");
    for (i = 0; i < NUM_LETTERS; i++)
        printf("%c:%d ", i + 'A', numLetters[i]);
    printf("\n");
    */
    for (i = 0; i < 10; i++)
        for (j = 0; j < numDigits[i]; j++)
            printf("%d", i);
    printf("\n");
}

void Read() {
    int T;
    int val;

    //printf("Entered Read()\n");

    scanf("%d", &T);
    dprintf("T = %d\n", T);

    int chunk = 1;
#pragma omp parallel for chunk
    for (int idTest = 0; idTest < T; idTest++) {
        scanf("%s\n", S);
        dprintf("S = %s\n", S);

        printf("Case #%d: ", idTest + 1);
        DoIt(S);
    }
}



int main() {
    dprintf("%ld\n", sizeof(long long));

    /*
    Compute(1021);
    for (int i = 0; i < 10; i++)
        printf("numDigitsEncountered[%d] = %d\n", i, numDigitsEncountered[i]);
    */

    //freopen("A_small.in", "rt", stdin);
    //freopen("A-small-attempt0.in", "rt", stdin);
    freopen("A-large.in", "rt", stdin);

    Read();

    return 0;
}

