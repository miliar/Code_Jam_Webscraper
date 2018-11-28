#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void flip(string& str, int bound)
{
    for (int i = 0; i <= bound; i++)
        str[i] = (str[i] == '-')? '+' : '-';

    reverse(str.begin(), str.begin() + bound + 1);
}

int main()
{
    int n;
    cin >> n;

    for (int t_i = 0; t_i < n; t_i++)
    {
        string pancakes;
        cin >> pancakes;

        int bottom = pancakes.size() - 1;

        int res = 0;

        while (bottom >= 0)
        {
            while (bottom >= 0 && pancakes[bottom] == '+')
                bottom--;

            if (bottom >= 0)
            {
                if (pancakes[0] == '-')
                    flip(pancakes, bottom);
                else // flip from the top to the last +
                {
                    int bound = 0;

                    while (pancakes[bound] == '+')
                        bound++;

                    flip(pancakes, bound - 1);
                }

                res++;
            }
        }

        cout << "Case #" << t_i + 1 << ": " << res << endl;
    }
}
