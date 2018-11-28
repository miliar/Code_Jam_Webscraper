
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

typedef long long int LLI;

using namespace std;


vector<bool> digits(LLI n)
{
    vector<bool> dig(10, 0);
    do
    {
        dig[n % 10] = true;
        n /= 10;
    } while(n != 0);

    return dig;
}

LLI solve(int n)
{
    int f = 1;
    vector<bool> dig(10,0);
    while(1)
    {
        vector<bool> tmp = digits((LLI)n * f);

        for(int i = 0; i < 10; i++)
            dig[i] = (dig[i] || tmp[i]);

        bool all = 1;
        for(bool b : dig)
            if(b == 0) all = 0;

        if(all) break;
        f++;
    }
    return n * f;
}


int main()
{
    ios_base::sync_with_stdio(0);

    int z;
    cin >> z;
    for(int i = 1; i <= z; i++)
    {
        int n;
        cin >> n;

        cout << "Case #" << i << ": ";
        n != 0 ? cout << solve(n) << endl : cout << "INSOMNIA\n";
    }

    return 0;
}
