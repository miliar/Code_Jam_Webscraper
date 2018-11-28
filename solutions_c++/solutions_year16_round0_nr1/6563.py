#include <bits/stdc++.h>

using namespace std;

inline bool fill_digits(unsigned long long n, bool *h)
{
    bool full = true;
    while(n)
    {
        h[n%10] = true;
        n /= 10;
    }
    for(int i=0;i<10;++i)
    {
        if(h[i] == false)
        {
            full = false;
            break;
        }
    }
    return full;
}

int main()
{
    int T;
    unsigned long long n;
    cin >> T;
    for(int t=1;t<=T;++t)
    {
        cin >> n;
        if(n == 0)
            cout << "Case #" << t << ": INSOMNIA" << endl;
        else
        {
            bool *h = new bool[10];
            fill_n(h,10,false);
            for(unsigned long long i=1;;++i)
            {
                if(fill_digits(n*i, h))
                {
                    cout << "Case #" << t << ": " << (n*i) << endl;
                    break;
                }
            }
            free(h);
        }
    }
    return 0;
}

