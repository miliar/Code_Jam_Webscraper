#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("input.txt");
    if(!in)
    {
        cout << endl << "failed to load data file" << endl;
        return -1;
    }
    int T;
    unsigned long long t, r, temp_t, count;
    in >> T;

    for (int ex = 1; ex <= T; ex++)
    {
        in >> r;
        in >> t;
        temp_t = 0;
        count = 0;
        while (temp_t <= t)
        {
            temp_t += 2 * r + 1 + 4 * count;
            count++;
        }
        count--;
        if (count == 0)
            count = 1;
        cout << "Case #" << ex << ": " << count << endl;
    }
    return 1;
}

