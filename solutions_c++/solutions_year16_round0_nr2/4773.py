#include <iostream>

using namespace std;

int main( )
{

    string curr;
    int N, flips; cin >> N;
    char last;

    for(int _case = 1; _case <= N; ++_case)
    {

        flips = 0;
        cin >> curr;

        last = curr[0];

        for(int j = 1; curr[j] != '\0'; ++j)
        {

            if(curr[j] != last)
            {
                ++flips;
                last = curr[j];
            }

        }
        if(last == '-')
            ++flips;

        cout << "Case #" << _case <<": " << flips << endl;

    }

    return 0;

}
