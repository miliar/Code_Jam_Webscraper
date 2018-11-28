#include <iostream>
#include <fstream>
#include <string>

#define INF 9999999999

using namespace std;


void digitBreakDown(long long number, bool (&digits)[10])
{
    if(number == 0)
    {
        digits[0] = true;
        //putchar('0' + 0);
    }
    while(number > 0)
    {
        int digit = number % 10;
        digits[digit] = true;
        //putchar('0' + digit);
        number /= 10;
    }
}

void initArray(bool (&digits)[10])
{
    for(int i = 0; i < 10 ; i++)
    {
        digits[i] = false;
    }
}

bool areAllDigitsMet(bool digits[10]){

    bool res = true;
    for(int i = 0; i < 10 ; i++)
    {
        res &= digits[i];
    }
    return res;
}

void process()
{
    int N, i = 1;
    long long next = 0, prev = 0;
    bool digits[10];
    initArray(digits);

    cin >> N;

    while(next < INF)
    {
        next = (long long)(i * N);
        if(next == prev)
        {
            cout << "INSOMNIA" << endl;
            return;
        }
        digitBreakDown(next, digits);
        if(areAllDigitsMet(digits))
        {
            cout << next << endl;
            return;
        }
        prev = next;
        i++;
    }
}

int main(int argc, char* argv[])
{
    int numberOfTestCases = 0;

    scanf("%d", &numberOfTestCases);

    for(int i = 0 ; i< numberOfTestCases ; i++)
    {
        printf("Case #%d: ", i + 1);
        process();
    }
}
