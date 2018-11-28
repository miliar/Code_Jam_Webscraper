#include <iostream>
#include <algorithm>
#include <fstream>
#include <assert.h>

using namespace std;

#define MAX_INPUTS 10001

int main()
{
    int num_cases = 0;
    int num_inputs = 0;
    int first_result = 0;
    int second_result = 0;
    int second_max = 0;

    int *inputs = new int[MAX_INPUTS];

    cin >> num_cases;

    assert(num_cases > 0);

    for(int i = 0; i < num_cases; i++)
    {
        cin >> num_inputs;

        assert(num_inputs > 0);

        for(int j = 0; j < num_inputs; j++)
        {
            cin >> inputs[j];
            if(j > 0 && 
                inputs[j] < inputs[j-1])
            {
                // calculate first ez result
                int t = inputs[j - 1] - inputs[j];
                first_result += t < 0 ? 0 : t;

                // track second max at the same time
                if(second_max < t)
                {
                    second_max = t;
                }
            }
        }

        for(int j = 0; j < num_inputs - 1; j++)
        {
            if(inputs[j] < second_max)
            {
                second_result += inputs[j];
            }
            else
            {
                second_result += second_max;
            }
        }

        cout << "Case #" << i + 1 << ": " << first_result << " " << second_result << endl;

        first_result = 0;
        second_result = 0;
        num_inputs = 0;
        second_max = 0;
        memset(inputs, 0, sizeof(int) * MAX_INPUTS);
    }
    return 0;
}
