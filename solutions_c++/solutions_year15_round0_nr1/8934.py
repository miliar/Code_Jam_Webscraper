//Deresu Roberto - FMI
//Re :)
#include<iostream>
using namespace std;

int main()
{
    int t;

    cin >> t;
    for (int test = 1; test <= t; test++)
    {
        int n = 0, up = 0, friends = 0;
        char sir[1007] = {0};

        cin >> n >> sir;

        up = sir[0]-'0';
        for (int i = 1; i <= n+1; i++)
        {
            if (sir[i] != '0')
            {
                if(i > up)
                {
                    int need = i-up;

                    friends = friends+need;
                    up = up+need;
                }
            }

            up = up+sir[i]-'0';
        }

        cout << "Case #" << test << ": " << friends << "\n";
    }

    return 0;
}
