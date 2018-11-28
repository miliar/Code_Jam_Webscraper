#include <bits/stdc++.h>


using namespace std;

bool checkDone (vector <bool> & done)
{
    bool res = true;
    for (int i = 0; i < 10; ++i)
    {
        res = res && done[i];
    }
    return res;
}

int checkNumber (int i)
{
    vector <bool> done (10);
    for (int a = 0; a < 10; ++a)
        done[a] = false;
    int p = i;
    for (int k = 0; k < 1000; ++k)
    {
        int h  = p;
        while (h > 0)
        {
            done[h%10] = true;
            h /= 10;
        }
        if (checkDone (done)) return p;
        p += i;
    }
    return -1;
}

int main()
{
    int tests;
    cin >> tests;
    for (int p = 0; p < tests; ++p )
    {
        int a;
        cin >> a;
        a = checkNumber (a);
        cout << "Case #" << p+1 << ": ";
        if (a==-1) cout << "INSOMNIA" << endl;
        else cout << a << endl;
    }
}
