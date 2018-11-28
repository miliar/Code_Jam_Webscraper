#include <iostream>

using namespace std;

typedef unsigned int uint;

char arr[10];

int main()
{
    uint num_cases = 0;
    cin >> num_cases;

    for (int i = 0; i < num_cases; ++i)
    {
        uint input = 0;
        uint count = 0;
        uint num = 1;
        uint sum = 0;
        uint cur_val = 0;

        memset(arr, 0, sizeof(char) * 10);

        cin >> input;

        if (input == 0)
        {
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
            continue;
        }

        while (sum < 10)
        {
            cur_val = input * num;
            while (cur_val)
            {
                uint ones = cur_val % 10;
                arr[ones] = 1;
                cur_val /= 10;
            }

            sum = [] {uint total = 0; for (int i = 0; i < 10; i++) total += arr[i]; return total; }();
            num++;
            count++;
        }

        cout << "Case #" << i + 1 << ": " << input * (num - 1) << endl;
    }

    return 0;
}