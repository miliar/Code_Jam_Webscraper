// google code jam 2013 Qualification Round
// problem C

#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

bool check(int a)
{
    if (a < 10)
        return true;
    if (a > 9 && a < 100 && a % 10 == a / 10)
        return true;
    if (a >= 100 && a <= 999 && a / 100 == a % 10)
        return true;
    return false;
}

int main()
{
    FILE *fin = fopen("C.in", "r");
    FILE *fout = fopen("C.out", "w");
    int test_t, input_a, input_b, res, a, b;
    fscanf(fin, "%d", &test_t);
    for (int testcase = 1; testcase <= test_t; testcase++)
    {
        fscanf(fin, "%d%d", &input_a, &input_b);
        a = int(sqrt(double(input_a)));
        a = (a * a < input_a ? a + 1 : a);
        b = int(sqrt(double(input_b)));
        res = 0;
        for (int i = a; i <= b; i++)
            if (check(i) && check(i * i))
                res++;
        fprintf(fout, "Case #%d: %d\n", testcase, res);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}

