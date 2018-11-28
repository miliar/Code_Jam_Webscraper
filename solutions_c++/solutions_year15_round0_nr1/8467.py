#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
const int MAX = 10000;
int a[MAX];
ifstream fin("a.in");
ofstream fout("a.out");
int ans()
{
    int len; fin >> len;
    char ch;
    for (int i=0; i<=len; ++i)
    {
        fin >> ch;
        a[i] = (int)ch-'0';
        //cout << a[i] << endl;
    }
    int dif = 0;
    int val = 0;
    for (int i=0; i<=len; ++i)
    {
        if (dif < i && a[i]>0)
        {
            val += (i-dif);
            dif += (i-dif);
        }
        dif += a[i];
        //cout << val << "   " << dif << endl;
    }
    return val;
}

int main()
{
    int tt; fin >> tt;
    int Ans[tt];
    for (int i=0; i<tt; ++i)
    {
        Ans[i] = ans();
    }
    for (int i=0; i<tt; ++i)
    {
        fout << "Case #" << i+1 << ": " << Ans[i] << endl;
    }
}
