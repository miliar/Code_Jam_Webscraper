#include<algorithm>
#include<string>
#include<iostream>
#include<vector>

using namespace std;

int main(void)
{
    int test;
    cin >> test;

    string g = "GABRIEL";
    string r = "RICHARD";

    for(int i = 1; i <= test; i++)
    {
        cout << "Case #" << i << ": ";
        int X, R, C;
        cin >> X;
        cin >> R;
        cin >> C;

        if((R*C) % X != 0)
        {
            cout << r << endl;
            continue;
        }
        else if(X == 3)
        {
            if(R == 1 || C == 1)
            {
                cout << r << endl;
                continue;
            }
        }
        else if(X == 4)
        {
            if(R < 3 || C < 3)
            {
                cout << r << endl;
                continue;
            }
        }
        cout << g << endl;
        
    }

    return 0;
}
