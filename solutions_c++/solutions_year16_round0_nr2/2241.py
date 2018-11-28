#include <iostream>
#include <string>

using namespace std;

typedef unsigned int uint;

char str[101];

int main()
{
    uint num_cases = 0;
    cin >> num_cases;

    for (int i = 0; i < num_cases; ++i)
    {
        uint num_flips = 0; 
        cin >> str;
        
        uint length = strlen(str);

        char cur = str[0];

        // walk through whole string
        for (int i = 1; i < length; i++)
        {
            if (cur != str[i])
            {
                num_flips++;
                cur = str[i];
            }
        }

        // if we end up with all bottom faces, flip
        if (cur == '-')
        {
            num_flips++;
        }

        cout << "Case #" << i + 1 << ": " << num_flips << endl;
    }

    return 0;
}