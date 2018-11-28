#include <iostream>

using namespace std;

int main()
{
    long int T, r, t, count;

    cin >> T;

    for(int ix = 0; ix < T; ix++)
    {
        cin >> r >> t;

        for(count = 0; t >= 0; r += 2, count++)
            t -= 2*r+1;

        cout << "Case #" << ix+1 << ": " << count-1 << endl;
    }

    return 0;
}
