#include <assert.h>
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


#define NUM_LETTERS ('Z' - 'A' + 1)
int numLetters[NUM_LETTERS];
int numDigits[10];
int N;

bool backFinished = false;




int indexVec[NUM_LETTERS];

int SortCmp(const void *a, const void *b) {
    //return (int *)a - (int *)b;
    //return numLetters[*((int *)a)] - numLetters[*((int *)b)];
    return numLetters[*((int *)b)] - numLetters[*((int *)a)];
}

void DoIt() {
    int i, j;

    //memset(numLetters, 0, sizeof(int) * NUM_LETTERS);

    for (i = 0; i < N; i++) {
        indexVec[i] = i;
    }
    qsort(indexVec, N, sizeof(int), SortCmp);
  #ifdef MY_DEBUG
    printf("indexVec = ");
    for (i = 0; i < N; i++) {
        printf("%d (%d), ", indexVec[i], numLetters[indexVec[i]]);
    }
    printf("\n");
  #endif

    int sum = 0;
    for (i = 0; i < N; i++)
        sum += numLetters[i];



    for (;;) {
        //dprintf("sum = %d\n", sum);
        // "It is guaranteed that at least one valid evacuation plan will exist."
        printf("%c", indexVec[0] + 'A');
        numLetters[indexVec[0]] --;
        sum--;
        if (sum == 0)
            break;


        if (numLetters[indexVec[1]] > 0.5 * sum) {
            printf("%c", indexVec[1] + 'A');
            numLetters[indexVec[1]] --;
            sum--;
        }
        if (sum == 0)
            break;
        printf(" ");

        for (i = 0; i < N; i++)
            if (numLetters[i] > 0.5 * sum) {
                printf("!!!!\n\n\n");
                assert(0);
            }

        //assert(numLetters[indexVec[i]] < 0.5 * sum); // "absolute majority"

        qsort(indexVec, N, sizeof(int), SortCmp);
    }
    printf("\n");
}

void Read() {
    int T;
    int val;
    int idTest;
    int i;

    //printf("Entered Read()\n");

    scanf("%d", &T);
    dprintf("T = %d\n", T);

    for (idTest = 0; idTest < T; idTest++) {
        scanf("%d\n", &N);
        dprintf("N = %d\n", N);

        for (i = 0; i < N; i++) {
            scanf("%d\n", &numLetters[i]);
            dprintf("numLetters[i] = %d\n", numLetters[i]);
        }

        printf("Case #%d: ", idTest + 1);
        DoIt();
        //break;
    }
}



int main() {
    //dprintf("%ld\n", sizeof(long long));

    /*
    Compute(1021);
    for (int i = 0; i < 10; i++)
        printf("numDigitsEncountered[%d] = %d\n", i, numDigitsEncountered[i]);
    */

    //freopen("A_small.in", "rt", stdin);
    //freopen("A-small-attempt1.in", "rt", stdin);
    freopen("A-large.in", "rt", stdin);

    //freopen("A-small-attempt0.in", "rt", stdin);
    //freopen("A-large.in", "rt", stdin);

    Read();

    return 0;
}

