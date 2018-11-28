#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>

using namespace std;

ifstream lire("input.in", ios::in);
ofstream ecrire("output.txt", ios::out);

bool isPal (int n)
{
    int k = 0, m = n;
    while (m > 0)
    {
        k = 10 * k + m % 10;
        m /= 10;
    }
    return k == n;
}

int main()
{
    int N;
    lire >> N;
    for (int i = 1; i <= N; i++)
    {
        int A, B, s = 0;
        lire >> A >> B;
        int a = (int)sqrt(A);
        int b = (int)sqrt(B);
        if (a * a < A) a++;
        for (int j = a; j <= b; j++)
            if (isPal(j) && isPal(j * j))
                s++;
        ecrire << "Case #" << i << ": " << s << endl;
    }
    return 0;
}
