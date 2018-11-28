#include <iostream>

using namespace std;

bool arr[10] = {};



void set_digit(int x)
{
    if(x >= 10)
        set_digit(x / 10);

    arr[x % 10] = true;
}


bool checkArr()
{
    bool found = arr[0];

    for (int i = 1; i < 10; i++) {
        found = found && arr[i];
        if(!found)
            break;
    }

    return found;
}


int main()
{
    int answer, t, n, z;
    cin >> t;

    for (int i = 1; i <= t; i++)
    {
        z = 2;
        cin >> n;

        set_digit(n);

        if (n == 0)
        {
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }
        else
        {
            while(1)
            {
                answer = z*n;

                set_digit(answer);

                z++;

                if(checkArr())
                {
                    cout << "Case #" << i << ": " << answer << endl;
                    break;
                }
                //check if all true;
            }

        }

        for (int i = 0; i < 10; i++) {
            arr[i] = 0;
        }
    }



}






