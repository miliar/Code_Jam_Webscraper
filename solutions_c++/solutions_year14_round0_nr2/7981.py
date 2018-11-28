#include <stdio.h>
#include <math.h>

void solve_next();

/**
 * Reads the input from stdin and prints the result
 */
int main(int argc, char** argv)
{
    int num_tests;
    if (fscanf(stdin, "%d", &num_tests) != 1) {
        printf("error\n");
        return 1;
    }

    for (int i = 0; i < num_tests; ++i) {
        printf("Case #%d: ", i+1);
        solve_next();
    }

    return 0;
}

void solve_next()
{
    double C, F, X;
    if (fscanf(stdin, "%lf %lf %lf", &C, &F, &X) != 3) {
        printf("error\n");
        return;
    }

    int n = floor(X/C - 2/F);     // the number of cookie farms needed
    if (n < 0) n = 0;             // can't buy less than 0

    double total_time = 0.0;
    for (int i = 0; i < n; ++i)
        total_time += C/(2+i*F);  // time needed to buy the farms

    total_time += X/(2+n*F);      // time to gather the X cookies
    printf("%.7f\n", total_time);
}

