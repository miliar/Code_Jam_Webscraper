#include <iostream>
#include <string>

using namespace std;

long int insomnia(long int n);

int main()
{
    long int t;
    long int tCases[t];
    long int answer[t];

    cin >> t;

    for(long int i = 0; i < t; i++)
    {
        cin >> tCases[i];
        answer[i] = insomnia(tCases[i]);
    }

    for(long int i = 0; i < t; i++)
    {
        if(answer[i] == -1)
        {
            cout << "Case #" << (i + 1) << ": " << "INSOMNIA" << endl;
        }
        else
        {
            cout << "Case #" << (i + 1) << ": " << answer[i] << endl;
        }
    }
}

long int insomnia(long int n)
{
    long int integers[10];
    long int lastNumber;
    bool awake = true;
    bool negative = false;
    long int temp;
    temp = n;
    lastNumber = n;

    if(n < 0)
    {
        n = n * -1;
        temp = n;
        lastNumber = n;
        negative = true;
    }

    for(long int i = 0; i < 10; i++)
    {
        integers[i] = 0;
    }

    if(n == 0)
    {
        return -1;
    }
    else
    {
        long int i = 1;
        while(awake)
        {
            lastNumber = n * i;
            temp = n * i;
            while(temp > 0)
            {
                integers[temp % 10] = 1;
                temp = temp / 10;
            }
            awake = false;
            for(long int j = 0; j < 10; j++)
            {
                if(integers[j] == 0)
                {
                    awake = true;
                }
            }
            i++;
        }
        return (negative ? lastNumber * -1 : lastNumber);
    }
}
