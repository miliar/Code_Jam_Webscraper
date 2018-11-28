#include <iostream>
#include <cstdio>
using namespace std;


int get_min_times(string s)
{
    int i = 0, j = s.length() - 1;
    int k, cnt = 0;
    while (true)
    {
        //puts("hi");
        while (j >= i && s[j] == '+')
        {
            --j;
        }
        if (j < 0)
        {
            return cnt;
        }
        if (s[i] == '+' && s[j] == '-')
        {
            k = i;
            while (s[k] == '+')
            {
                s[k] = '-';
                k++;
            }
            cnt++;
        }
        for (int p = i, q =j; p <= q; ++p, --q)
        {
            char first = s[p], last = s[q];
            
            if (first == '+')
            {
                s[q] = '-';
            }
            else
            {
                s[q] = '+';
            }
            
            if (last == '+')
            {
                s[p] = '-';
            }
            else
            {
                s[p] = '+';
            }
            
        }
        cnt++;
    }    
    return 0;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        string s;
        cin >> s;
        cout << "Case #" << i << ": " << get_min_times(s)<< endl;
    }
    return 0;
}


