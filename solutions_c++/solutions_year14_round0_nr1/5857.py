#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int T;

bool good[17];

void run(int Case)
{
    int a1, a2;
    cin >> a1;
    for (int i = 1; i <= 4; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            int x; cin >> x;
            if (i==a1)
            {
                good[x] = true;
            }
        }
    }
    cin >> a2;
    int cnt = 0;
    int X;
    for (int i = 1; i <= 4; i++)
    {
        for (int j=1; j <= 4; j++)
        {
            int x; cin >> x;
            if (i==a2)
            {
                if (good[x])
                {
                    cnt++;
                    X = x;
                }
            }
        }
    }
    if (cnt == 1)
    {
        cout << "Case #" << Case << ": " <<X << endl;
    }else if (cnt > 1)
    {
        cout << "Case #" << Case << ": Bad magician!" << endl;
    }else
    {
        cout << "Case #" << Case << ": Volunteer cheated!" << endl;
    }




}
int main()
{
    freopen("inFile.txt", "r", stdin);
    freopen("outFile.txt", "w", stdout);
    cin >> T;

    for (int Case = 1; Case <=T; Case++)
    {
        memset(good, false, sizeof(good));
        run(Case);
    }

    return 0;
}
