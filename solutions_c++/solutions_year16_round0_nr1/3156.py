#include <fstream>
#include <cstring>
#include <cstdlib>
#include <ctime>
#define MAX_TIMES 100000
using namespace std;

bool freq[10];
int completed;

void generator()
{
    srand(time(NULL));
    int tests = 200;
    ofstream g("sheep.in");
    g << tests << '\n';
    for (int i = 0; i < tests; i++)
        g << rand() % 100001 << '\n';
    g.close();
}

void extract_digits(long long number)
{
    int digit;
    while (number > 0)
    {
        digit = number % 10;
        if(!freq[digit])
        {
            freq[digit] = true;
            completed++;
        }
        number /= 10;
    }

}

void solver()
{
    int tests;
    long long n;
    long long i;
    ifstream f("sheep.in");
    ofstream g("sheep.out");
    f >> tests;
    for (int k = 1; k <= tests; k++)
    {
        f >> n;
        memset(freq, 0, sizeof(freq));
        completed = 0;
        for (i = 1; i < MAX_TIMES; i++)
        {
            extract_digits(n * i);
            if (completed >= 10)
                break;
        }
        if (completed >= 10)
            g << "Case #" << k << ": " << n * i << '\n';
        else
            g << "Case #" << k << ": INSOMNIA\n";
    }
    f.close();
    g.close();
}

int main()
{
    solver();
    //generator();
    return 0;
}
