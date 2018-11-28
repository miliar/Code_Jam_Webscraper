#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define deb(x) cout << #x << " = " << x << endl;

typedef unsigned long long LL;
int digit[10], cont;

LL f(LL n, LL i)
{
    LL k = i * n;

    while(k > 0)
    {
        int d = k%10; k /= 10;
        if(digit[d] == 0)
            cont++;
        digit[d]++;
    }

    if(cont == 10)
        return i*n;
    return f(n, i+1);
}

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(0);

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, n;
    cin >> T;

    for(int t = 1; t <= T; t++)
    {
        cin >> n;
        fill(digit, digit + 10, 0);
        cont = 0;

        cout << "Case #" << t << ": ";

        if(n == 0)
            cout << "INSOMNIA";
        else
            cout << f(n, 1);

        cout << endl;
    }

    return 0;
}
