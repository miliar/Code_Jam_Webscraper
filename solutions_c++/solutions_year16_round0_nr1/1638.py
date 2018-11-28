#include <vector>
#include <iostream>

using namespace std;

int main()
{
    int n_t;
    cin >> n_t;

    for (int t_i = 0; t_i < n_t; t_i++)
    {
        unsigned long n;
        cin >> n;

        if (n == 0)
            cout << "Case #" << t_i + 1 << ": INSOMNIA" << endl;
        
        else
        {
            vector<bool> digits(10, false);

            int m = n;
            int j = 1;
            
            int count = 0;

            while (count < 10)
            {
                m = n * j;

                for (char d : to_string(m))
                {
                    int digit = d - '0';

                    if (not digits[digit])
                    {
                        count++;
                        digits[digit] = true;
                    }
                }

                j++;
            }

            cout << "Case #" << t_i + 1 << ": " << m << endl;
        }
    }
}
