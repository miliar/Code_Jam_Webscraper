#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    int N = 0;
    int T = 0;

    int checkDigit[10];
    int sum = 0;

    cin >> T;
    for (int i = 1; i <= T; i++)
    {
        cin >> N;

        if(N == 0)
        {
            cout << "Case #" << i << ": " << "INSOMNIA";
            cout << endl;
        }
        else
        {
            memset(checkDigit, 0, sizeof(checkDigit));

            for(int j = 0; j < 1000; j++)
            {
                int countN = (j + 1) * N;
                while (1)
                {
                    if((countN / 10) != 0)
                    {
                        checkDigit[countN % 10] = 1;
                        countN /= 10;
                    }
                    else
                    {
                        checkDigit[countN] = 1;
                        break;
                    }
                }

                sum = 0;
                for (int k = 0; k < 10; k++)
                {
                    sum += checkDigit[k];
                }

                if (sum == 10)
                {
                    cout << "Case #" << i << ": " << ((j + 1) * N);
                    cout << endl;
                    break;
                }

            }

            if(sum != 10)
            {
                cout << "Case #" << i << ": " << "INSOMNIA";
                cout << endl;
                
            }
        }
    }
}


