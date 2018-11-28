#include <bits/stdc++.h>

using namespace std;

ifstream in("A.in");
ofstream out("A.out");

bool taken[10];

bool check()
{
    for (int i=0;i<10;i++)
        if (taken[i] == false)
            return false;
    return true;
}

void solve()
{
    unsigned long long N;
    in>>N;

    for (int i=0;i<10;i++)
        taken[i] = false;

    if (N == 0)
    {
        out<<"INSOMNIA"<<endl;
        return;
    }

    int i = 1;
    while (check() == false)
    {
        unsigned long long tmp = i * N;
        while (tmp>0)
        {
            taken[tmp%10] = true;
            tmp/=10;
        }
        i++;
    }
    out<<(i-1)*N<<endl;
}

int main()
{
    int t;
    in>>t;

    for (int i=0;i<t;i++)
    {
        out<<"Case #"<<i+1<<": ";
        solve();
    }


    return 0;
}
