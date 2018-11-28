
#include <stdio.h>
using namespace std;

#define BSIZE 1<<15
char buffer[BSIZE];
long bpos = 0L, bsize = 0L;
long readLong()
{
    long d = 0L, x = 0L;
    char c;

    while (1)  {
        if (bpos >= bsize) {
            bpos = 0;
            if (feof(stdin)) return x;
            bsize = fread(buffer, 1, BSIZE, stdin);
        }
        c = buffer[bpos++];
        if (c >= '0' && c <= '9') { x = x*10 + (c-'0'); d = 1; }
        else if (d == 1) return x;
    }
    return -1;
}

void solve_next();


/**
 * Reads the input from stdin and prints the result
 */
int main(int argc, char** argv)
{
    int num_tests = readLong();
    for (int i = 0; i < num_tests; ++i) {
        printf("Case #%d: ", i+1);
        solve_next();
    }

    return 0;
}

void solve_next()
{
    int first_row = readLong();

    int numbers[16];
    for (int i = 0; i < 16; ++i)
        numbers[i] = readLong();

    int possible[4];
    for (int i = 0; i < 4; ++i)
        possible[i] = numbers[(first_row-1)*4+i];

    int second_row = readLong();
    for (int i = 0; i < 16; ++i)
        numbers[i] = readLong();

    int result = -1, num_found = 0;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (numbers[(second_row-1)*4+i] == possible[j]) {
                result = possible[j];
                num_found++;
            }
    
    if (num_found == 0)
        printf("Volunteer cheated!\n");
    else if (num_found == 1)
        printf("%d\n", result);
    else
        printf("Bad magician!\n");
}

