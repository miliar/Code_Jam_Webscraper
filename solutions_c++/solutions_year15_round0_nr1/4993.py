#include <iostream>
#include <string>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        int maxShynessLvl, shynessLvl = 0, friendsRequired = 0;
        string audience;
        cin >> maxShynessLvl >> audience;
        for(int i = 0; i < audience.size(); i++)
        {
            if(shynessLvl < i)
            {
                friendsRequired += i - shynessLvl;
                shynessLvl = i;
            }
            shynessLvl += audience[i] - '0';
        }
        cout << "Case #" << t << ": " << friendsRequired << endl;
    }
    return 0;
}
