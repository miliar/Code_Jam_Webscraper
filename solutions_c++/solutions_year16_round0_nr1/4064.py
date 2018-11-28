#include <iostream>
#include <fstream>

using namespace std;

bool algunFalse(bool u[10])
{
    for(int i=0; i<10; i++)
        if(!u[i])
            return true;
    return false;
}

long long solve(long long k)
{
    bool u[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    long long p = 1, t = k;
    while(algunFalse(u))
    {
        t = k*p;
        long long z = t;
        while(z)
        {
            u[z%10] = true;
            z/=10;
        }
        p++;
    }
    return t;
}

int main()
{
    ifstream in("in");
    ofstream out("out.txt");
    long long n, k;

    in >> n;
    for(int i=0; i<n; i++)
    {
        //cout << i+1 << " de " << n << endl;
        out << "Case #" << i+1 << ": ";
        in >> k;
        if(k == 0)
            out << "INSOMNIA" << endl;
        else
            out << solve(k) << endl;
    }

    in.close();
    out.close();

    return 0;
}
