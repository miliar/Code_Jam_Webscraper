#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
string s;
int a[10];
int main()
{
    freopen("A-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for(int i = 0;i < t;i++)
    {
        int n;
        cin >> n;
        if (n == 0)
        {
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
            continue;
        }
        int k = 1;
        bool d = true;
        for(int j = 0;j < 10;j++)
            a[j] = 0;
        while(true)
        {
            char w[100];
            sprintf(w, "%d", n * k);
            s = string(w);
            for(int j = 0;j < s.length();j++)
            {
                char u = s[j];
                a[u - '0'] = 1;
            }
            d = true;
            for(int j = 0;j  < 10;j++)
            {
                if (a[j] == 0)
                {
                    d = false;
                    break;
                }
            }
            if (d == true)
                break;
            k++;
        }
        if (d == true)
            cout << "Case #" << i + 1 << ": " << n * k << endl;
        else
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
    }
    return 0;
}
