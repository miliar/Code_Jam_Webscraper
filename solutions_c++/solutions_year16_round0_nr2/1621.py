#include <bits/stdc++.h>

using namespace std;

string is;
int st[109];
int test , T , top , i;

int main()
{
ifstream fin("test.in");
ofstream fout("test.out");

fin >> T;
for (test = 1 ; test <= T ; ++test)
{
    fin >> is;

    if (is[0] == '+')
    st[top = 1] = 1;
    else st[top = 1] = 0;

    for (i = 1 ; i < is.size() ; ++i)
    {
        if (is[i] == '+')
        {
            if (st[top] == 0) st[++top] = 1;
        }
        else
        {
            if (st[top] == 1) st[++top] = 0;
        }
    }

    fout << "Case #" << test << ": ";
    if (st[top] == 1) fout << top - 1 << '\n';
    else fout << top << '\n';
}

return 0;
}
