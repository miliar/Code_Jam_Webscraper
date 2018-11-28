#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int index = 1; index <= t; ++index)
    {
        int ans, x;
        int mark[ 16 ] = { 0 };

        cin >> ans;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
            {
                cin >> x;
                if(ans ==  i + 1)
                {
                    mark[ x - 1 ] = 1;
                }
            }

        int cnt = 0, res;
        cin >> ans;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
            {
                cin >> x;
                if(ans == i + 1 and mark[ x - 1 ])
                {
                    ++cnt;
                    res = x;
                }
            }

        cout << "Case #" << index << ": ";
        if(cnt == 1)
        {
            cout << res << endl;
        }
        else if(cnt > 1)
        {
            cout << "Bad magician!" << endl;
        }
        else
        {
            cout << "Volunteer cheated!" << endl;
        }
    }
}
