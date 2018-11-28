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


bool AllEncountered() {
    for (int i = 0; i < 10; i++)
        if (numDigitsEncountered[i] == 0)
            return false;
    
    return true;
}


void Compute(long long val) {
    while (val != 0) {
        //if (val == )
        //break;
        int tmp = val % 10;
        val /= 10;
        numDigitsEncountered[tmp]++;
        dprintf("tmp = %d\n", tmp);
    }
}

void DoIt(int N) {
    long long i;
    long long res;

    memset(numDigitsEncountered, 0, sizeof(int) * 10);

    if (N == 0) {
        printf("INSOMNIA\n");
        return;
    }

    for (i = 1; ; i++) {
        res = i * N;
        printf("%d\n", res);

        Compute(res);
        if (AllEncountered()) {
            //dprintf("i = %d\n", i);

            //printf("Last number named = %d\n", res);
            printf("%d\n", res);
            break;
        }

        /*
        if (i > 1000) {
            printf("INSOMNIA\n");
            return;
        }
        */
    }
}

void Read() {
    int T;
    int val;

    //printf("Entered Read()\n");

    scanf("%d", &T);
    dprintf("T = %d\n", T);

    for (int idTest = 0; idTest < T; idTest++) {
        scanf("%d\n", &val);
        dprintf("val = %d\n", val);

        printf("Case #%d: ", idTest + 1);
        DoIt(val);
    }
}

int main() {
    dprintf("%d\n", sizeof(long long)); 

    /*
    Compute(1021);
    for (int i = 0; i < 10; i++)
        printf("numDigitsEncountered[%d] = %d\n", i, numDigitsEncountered[i]);
    */

    freopen("A_small.in", "rt", stdin);
    //freopen("A-small-attempt0.in", "rt", stdin);
    //freopen("A-large.in", "rt", stdin);

    //DoIt(1692);
    Read();

    return 0;
}
