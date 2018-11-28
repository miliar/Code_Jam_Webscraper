#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("quala.txt", "r", stdin);
    freopen("qualao.txt", "w", stdout);
    long long n;
    n = 0;
    long long t;
    cin >> t;
    for (long long kkk = 0; kkk < t; kkk++)
    {
        cin >> n;
        if (n == 0)
        {
            cout << "Case #"<< kkk + 1 << ": INSOMNIA" << endl;
            continue;
        }
        vector<long long> was(10);
        for (long long i = 1; i < 100000; i++)
        {
            long long tt = n * i;
            //cout << tt << " ";
            while (tt)
            {
                was[tt % 10] = 1;
                tt /= 10;
            }
            long long br = 0;
            for (long long i = 0; i < 10; i++)
            {
                if (was[i] == 0)
                {
                    br = 1;
                }
            }
            if (br == 0)
            {
               //for (long long i = 0; i < 10; i++)
                //{
                //    cout << was[i] << " ";
                //}
                //cout << endl;
                cout << "Case #"<< kkk + 1<< ": " << i * n << endl;
                break;
            }
        }
        for (long long i = 0; i < 10; i++)
        {
           if (was[i] == 0)
            {
                cout << "Case #" << kkk + 1<< ": " << "INSOMNIA" << endl;
            }
        }
    }
}
