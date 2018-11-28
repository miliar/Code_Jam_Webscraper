#include <iostream>
#include <fstream>

using namespace std;

void check_digits(bool digits[], int n)
{
    while (n > 0)
    {
        digits[n % 10] = true;
        n /= 10;
    }
}

bool all_seen(bool digits[])
{
    for (int i = 0; i < 10; i++)
    {
        if (digits[i] == false)
            return false;
    }
    return true;
}

int main()
{
    ofstream output;
    ifstream input;
    input.open("A-large.in");
    output.open("output.txt");

    int t;
    input >> t;

    for (int i = 1; i <= t; i++)
    {
        int n;
        input >> n;

        int j = 1;
        bool digits[10] = {false};
        bool insomnia = false;

        output << "Case #" << i << ": ";
        while (!all_seen(digits))
        {
            if (n*j == n*(j-1))
            {
                output << "INSOMNIA";
                insomnia = true;
                break;
            }
            check_digits(digits, n*j);
            j++;
        }
        if (!insomnia)
            output << n*(j-1);
        output << endl;
    }

    return 0;
}
