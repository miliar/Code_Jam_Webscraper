#include <iostream>
#include <String>
#include <sstream>

using namespace std;

int holder[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

bool checkDigits (int digit)
{
    int sum = 0;
    switch (digit)
    {
        case 0:
            holder[0] = 1;
            break;
        case 1:
            holder[1] = 1;
            break;
        case 2:
            holder[2] = 1;
            break;
        case 3:
            holder[3] = 1;
            break;
        case 4:
            holder[4] = 1;
            break;
        case 5:
            holder[5] = 1;
            break;
        case 6:
            holder[6] = 1;
            break;
        case 7:
            holder[7] = 1;
            break;
        case 8:
            holder[8] = 1;
            break;
        case 9:
            holder[9] = 1;
            break;
    }
    for(int i=0; i<10; i++)
    {
        sum = sum + holder[i];
    }
    if(sum == 10)
    {
        for(int i=0; i<10; i++)
        {
            holder[i] = 0;
        }
        return true;
    }
    else
    {
        return false;
    }
}

long long lastNumber (long long number)
{
    int i = 0;
    int multiplier = 1;
    long long base = 10;
    long long newNumber = number;
    int digit;
    long long residue = 0;
    while(1)
    {
        //cout << "newNumber: " << newNumber << endl;
        while ((newNumber/base) > 0)
        {
            digit = ((newNumber % base)- residue)/(base/10);
            //cout << "digit: " << digit << endl;
            residue = newNumber%base;
            //cout << "residue: " << residue << endl;
            if (checkDigits (digit))
            {
                return newNumber;
            }
            else
            {
                base = base*10;
            }
        }
        digit = newNumber / (base/10);
        //cout << "digit: " << digit << endl;
        if (checkDigits (digit))
        {
            return newNumber;
        }
        else
        {
            base = 10;
            residue = 0;
            multiplier++;
            newNumber = number*multiplier;
        }
    }
}

int main()
{
    int T;
    long long N;
    cin >> T;
    for(int i=1; i<=T; i++)
    {
        cin >> N;
        if (N == 0)
        {
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }
        else
        {
            if (N < 0)
            {
                N = -N;
                cout << "Case #" << i << ": " << -(lastNumber (N)) << endl;
            }
            else
            {
                cout << "Case #" << i << ": " << lastNumber (N) << endl;
            }
        }
    }
}

