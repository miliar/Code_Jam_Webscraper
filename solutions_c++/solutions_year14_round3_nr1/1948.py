#include <iostream>

using namespace std;

int T;
long long P, Q;

long long GCD(long long a, long long b)
{    
    long long temp;
    while (b != 0) {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;    
}

void Solve(int t)
{
    int n = 0;
    long long r = GCD(P, Q);
    long long p = P / r;
    long long q = Q / r;
    cout << "Case #" << t << ": ";
    
    long long qq = Q;
    while (qq > 1)
    {
        if (qq % 2 == 0)
        {
            qq /= 2;
        }
        else
        {
            cout << "impossible" << endl;
            return;
        }
    }

    while (q > 1 && p < q)
    {
        if (q % 2 == 1)
        {
            cout << "impossible" << endl;
            return;
        }
               
        if (p < q / 2)
        {
            ++n;
            q /= 2;
        }
        else
        {
            cout << n + 1 << endl;
            return;
        }        
    }

    if (p == q && p == 1)
    {
        cout << n << endl;
    }
    else
    {
        cout << "impossible" << endl;
    }
}

int main()
{
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        char c;
        cin >> P >> c >> Q;        
        Solve(t);
    }
    return 0;
}
