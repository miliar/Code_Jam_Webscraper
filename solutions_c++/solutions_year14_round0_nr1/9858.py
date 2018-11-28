#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
    int n = 0;
    int ra = 0;
    int rb = 0;
    int countnum = 0;
    int a[5][5] = {0};
    int b[5][5] = {0};
    int answer[5] = {0};
    int ani = 0;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    cin >> n;
    for (int i = 0;i != n;i++)
    {
        countnum = 0;
        ani = 0;
        cin >> ra;
        for (int j = 0;j != 4;j++)
            for (int m = 0;m != 4;m++)
                cin >> a[j][m];
        cin >> rb;
        for (int j = 0;j != 4;j++)
            for (int m = 0;m != 4;m++)
                cin >> b[j][m];
        for (int ai = 0;ai != 4;ai++)
        {
            for (int bi = 0;bi != 4;bi++)
                if (a[ra-1][ai] == b[rb-1][bi])
                {
                    countnum++;
                    answer[ani++] = a[ra-1][ai];
                }
            if (countnum > 1)
                break;
        }
        cout << "Case #" << i+1 << ": ";
        if (countnum == 0)
            cout << "Volunteer cheated!" << endl;
        if (countnum == 1)
            cout << answer[0] << endl;
        if (countnum == 2)
            cout << "Bad magician!" << endl;
        //for (int j = 0;j != 16;j++)
        //    cout << a[j];
    }
    return 0;
}
