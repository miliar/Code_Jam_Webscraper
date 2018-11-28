#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int T = 0;
    cin >> T;
    int ansFirst = 0, ansSecond = 0;
    int arr[4] = {0}, arrTemp[4] = {0};
    int compare = 0;
    int result = 0;
    for (int cases = 1; cases <= T; ++cases)
    {
        result = 0;
        // input the first arrangement
        cin >> ansFirst;
        for (int i = 1; i <= 4; ++i)
        {
            if (i == ansFirst)
            {
                cin >> arr[0] >> arr[1] >> arr[2] >> arr[3];
            }
            else
            {
                cin >> arrTemp[0] >> arrTemp[1] >> arrTemp[2] >> arrTemp[3];
            }
        }
        // input the second arrangement
        cin >> ansSecond;
        for (int i = 1; i <= 4; ++i)
        {
            if (i == ansSecond)
            {
                for (int j = 1; j <= 4; ++j)
                {
                    cin >> compare;
                    // in original row
                    if (compare == arr[0] || compare == arr[1] || compare == arr[2] || compare == arr[3])
                    {
                        if (result == 0)
                        {
                            result = compare;
                        }
                        else if (result > 0)
                        {
                            // double answer
                            result = -1;
                        }
                    }
                }
            }
            else
            {
                cin >> arrTemp[0] >> arrTemp[1] >> arrTemp[2] >> arrTemp[3];
            }
        }
        // output
        if (result > 0)
        {
            printf("Case #%d: %d\n", cases, result);
        }
        if (result == 0)
        {
            printf("Case #%d: Volunteer cheated!\n", cases);
        }
        if (result == -1)
        {
            printf("Case #%d: Bad magician!\n", cases);
        }
    }
    return 0;
}
