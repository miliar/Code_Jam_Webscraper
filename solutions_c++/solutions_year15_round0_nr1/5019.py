#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int max;
        cin >> max;

        char temp;
        int missing = 0;
        int present = 0;
        for (int j = 0; j < max + 1; ++j)
        {
            cin >> temp;
            int temp2 = temp - '0';
            if (present + missing < j)
            {
                missing += j - present - missing;
            }
            present += temp2;
        }
        cout << "Case #" << i + 1 << ": " << missing << endl;
    }

    return 0;
}
