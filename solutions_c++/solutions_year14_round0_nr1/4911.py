#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    //freopen("1.txt", "r", stdin);
    //freopen("2.txt", "w", stdout);
    int cases, k, fir, sec;
    int a[5];
    int b[5];
    cin >> cases;
    for (int t = 1; t <= cases; t++)
    {
        cin >> fir;
        for (int i = 1; i <= 4; i++)
        {
            for (int j = 1; j <= 4; j++)
            {
                cin >> k;
                if (i == fir)
                    a[j] = k;
            }
        }
        cin >> sec;
        for (int i = 1; i <= 4; i++)
        {
            for (int j = 1; j <= 4; j++)
            {
                cin >> k;
                if (i == sec)
                    b[j] = k;
            }
        }
        int count = 0;
        int ret;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
                if (a[i] == b[j])
                {
                    ret = a[i];
                    count++;
                }
        cout << "Case #" << t << ": "; 
        if (count == 1)
            cout << ret << endl;
        else if (count > 1)
            cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
    }
    return 0;
}
