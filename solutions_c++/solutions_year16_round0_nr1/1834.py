#include<iostream>
#include<cstring>
using namespace std;

int main()
{
    int t, kaseno = 0;
    cin >> t;
    while(t--)
    {
        bool hash[10];
        memset(hash, false, sizeof(hash));
        int n;
        cin >> n;
        int orig = n;
        cout << "Case #" << ++kaseno << ": ";
        if (n == 0)
        {
            cout << "INSOMNIA" << endl;
            continue;
        }
        else
        {
            while (true)
            {
                int tmp = n;
                while (tmp)
                {
                    hash[tmp % 10] = true;
                    tmp /= 10;
                }
                bool flag = true;
                for (int i = 0; i <= 9; i++)
                    if (!hash[i])
                        flag = false;
                if (flag)
                {
                    cout << n << endl;
                    break;
                }
                n += orig;
            }
        }
    }
    return 0;
}