#include <iostream>

using namespace std;

void compareNumbers(int number, int * wantedNumbers, int & numbersToEnd)
{
    for(int i = 0; i < numbersToEnd; i++)
    {
        if(number == wantedNumbers[i])
        {
            wantedNumbers[i] = wantedNumbers[numbersToEnd-1];
            wantedNumbers[numbersToEnd-1] = number;
            numbersToEnd--;
            i = 10;
        }
    }
}

void checkNumbers(int n, int * wantedNumbers, int & numbersToEnd)
{
    while(n > 0)
    {
        compareNumbers(n%10,wantedNumbers,numbersToEnd);
        n /= 10;
    }
}

void reset(int * wantedNumbers, int & numbersToEnd)
{
    for(int i = 0; i < 0; i++)
        wantedNumbers[i] = i;

    numbersToEnd = 10;
}

int main()
{
    int wantedNumbers[10];
    int numbersToEnd = 10;

    for(int i = 0; i < 10; i++)
        wantedNumbers[i] = i;

    int t, n;
    cin >> t;
    for(int i = 0; i < t; i++)
    {
        cin >> n;
        if(n == 0)
        {
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
            continue;
        }
        int tmp = n;

        int j = 1;
        while(true)
        {
            checkNumbers(n,wantedNumbers,numbersToEnd);

            if(numbersToEnd == 0) break;
                else {
                    j++;
                    n = tmp * j;
                }
        }
        cout << "Case #" << i+1 << ": " << n << endl;
        reset(wantedNumbers,numbersToEnd);
    }
    return 0;
}
