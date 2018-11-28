#include <fstream>

using namespace std;

int main()
{
    int T, N, i, j, counter = 0, digit;
    unsigned long long current;
    ifstream f("input.in");
    ofstream g("output.out");
    f >> T;
    for (i = 1; i <= T; i++)
    {
        f >> N;
        g << "Case #" << i << ": ";

        if (N == 0)
            g << "INSOMNIA";
        else
        {
            bool seen[10];
            fill(seen, seen + 10, false);
            current = N;
            counter = 0;
            j = 1;
            while (counter < 10)
            {
                current = 1ULL * N * j;
                while (current)
                {
                    digit = current % 10;
                    if (!seen[digit])
                        seen[digit] = true, counter++;
                    current /= 10;
                }

                if (counter == 10)
                    g << 1ULL * N * j;

                j++;
            }
        }
        g << '\n';
    }
    return 0;
}
