#include <iostream>

using namespace std;

int main()
{
    int cts, a, b, k;

    cin >> cts;
    for(int ct = 1; ct <= cts; ct++)
    {
        cin >> a >> b >> k;

        int hit = 0;
        for(int i = 0; i < a; i++)
        {
            for(int j = 0; j < b; j++)
            {
                if((i & j) < k)
                    hit++;
            }
        }

        cout << "Case #" << ct << ": " << hit << endl;
    }

    return 0;
}

