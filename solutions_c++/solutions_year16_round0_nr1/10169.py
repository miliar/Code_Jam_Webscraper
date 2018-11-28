#include <iomanip>
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

#define TEN 10

int result(int &N, int &i);
bool finish (bool ary [TEN]);


int main()
{
    int cases,
        counter = 1,
        N = 0,
        i = 1,
        last = 0,
        calcVal = 0,
        temp1 = 0;

    bool done = false;
    bool nums[TEN];
    scanf("%d", &cases);

    do
    {
        for (int m = 0; m < 10; m++)
        {
            nums[m] = false;
        }
        done = false;
        i = 1;
        N = 0;

        scanf("%d", &N);

        if (N == 0)
        {
            cout << "Case #" << counter << ": INSOMNIA" << endl;
        }
        else
        {
            calcVal = N;
            last = calcVal;
            while (calcVal > 0)
            {
                temp1 = calcVal % TEN;
                calcVal = calcVal / TEN;

                for (int n = 0; n < TEN; n++)
                {
                    if (temp1 == n)
                    {
                        nums[n] = true;
                    }
                }
            }
            if (finish(nums))
            {
                done = true;
            }

            while (!done)
            {
                calcVal = result(N, i);
                last = calcVal;

                while (calcVal > 0)
                {
                    temp1 = calcVal % TEN;
                    calcVal = calcVal / TEN;

                    for (int n = 0; n < TEN; n++)
                    {
                        if (temp1 == n)
                        {
                            nums[n] = true;
                        }
                    }
                }
                if (finish(nums))
                {
                    done = true;
                }
                i++;
            }
            cout << "Case #" << counter << ": " << last << endl;
        }

        counter++;
    }while(counter <= cases);

    return 0;
}

int result(int &N, int &i)
{
    return (N * i);
}

bool finish (bool ary [])
{
    for (int i = 0; i < TEN; i++)
    {
        if (ary [i] != true)
        {
            return false;
        }
        else{continue;}
    }
    return true;
}
