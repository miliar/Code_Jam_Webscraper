#include <iostream>

#define MAX 18446744073709551615

using namespace std;

void result()
{
    int num, y = 0;
    unsigned long long m, n;
    int i, inc = 1, sum = 0;
    int arr[10] = {0};

    cin >> num;

    if(num == 0)
        cout << "INSOMNIA";
    else
    {
        while(m <= MAX)
        {
            m = num * inc++;

            n = m;

            while(m)
            {
                y = m % 10;
                arr[y] = 1;

                m = m/10;
            }

            sum = 0;
            for(i = 0; i< 10; i++)
                sum += arr[i];

            if(sum == 10) break;

        }
        if(sum == 10)
        {
            //cout << "sleep at:" << n << endl;
            cout << n;
        }
        else
            cout << "INSOMNIA";

        /*
        for(i = 0; i < 10; i++)
            cout << arr[i] << " ";

        cout << endl;
        */
    }

}


int main()
{
    int test, i = 1;

    //cout << "Test Cases:";
    cin >> test;

    while(test--)
    {
        cout << "case #"<< i++ <<": ";

        result();

        cout << endl;
    }

return 0;
}
