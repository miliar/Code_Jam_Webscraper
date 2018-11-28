#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("quala.txt", "r", stdin);
    freopen("qualao.txt", "w", stdout);
    long long int n;
    n = 0;
    int t;
    cin >> t;
    for (int kkk = 0; kkk < t; kkk++)
    {
        cin >> n;
        if (n == 0)
        {
            cout << "Case #"<< kkk + 1 << ": INSOMNIA" << endl;
            continue;
        }
        vector<int> was(10);
        for (int i = 1; i < 100000; i++)
        {
            long long int tt = n * i;
            //cout << tt << " ";
            while (tt)
            {
                was[tt % 10] = 1;
                tt /= 10;
            }
            int br = 0;
            for (int i = 0; i < 10; i++)
            {
                if (was[i] == 0)
                {
                    br = 1;
                }
            }
            if (br == 0)
            {
               //for (int i = 0; i < 10; i++)
                //{
                //    cout << was[i] << " ";
                //}
                //cout << endl;
                cout << "Case #"<< kkk + 1<< ": " << i * n << endl;
                break;
            }
        }
        for (int i = 0; i < 10; i++)
        {
           if (was[i] == 0)
            {
                cout << "Case #" << kkk + 1<< ": " << "INSOMNIA" << endl;
            }
        }
    }
}
