#include<iostream>
#include<vector>
#include<iomanip>
#include<cstring>
using namespace std;
int main()
{
    int T;
    bool used[17];
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        vector<int> sol;
        memset(used, 0, 17);
        for(int i = 0; i < 2; ++i)
        {
            int r1;
            cin >> r1;
            for(int j = 1; j <= 4; ++j)
            {
                for(int k = 0; k < 4; ++k)
                {
                    int a;
                    cin >> a;
                    if (j != r1) continue;
                    if (i == 1) {
                        if (used[a])
                            sol.push_back(a);
                    } else {
                        used[a] = true;
                    }
                }
            }
        }
        cout << "Case #" << t << ": ";
        if(sol.size() == 1)
            cout << sol[0];
        if(sol.size() == 0)
            cout << "Volunteer cheated!";
        if(sol.size() > 1)
            cout << "Bad magician!";
        cout << endl;
    }
    return 0;
}
