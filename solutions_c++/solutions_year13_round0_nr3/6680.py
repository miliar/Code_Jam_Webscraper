#include <iostream>
#include <cstdio>
#include <cmath>


using namespace std;

int rev(int j)
{
    int num = j;
    int revs = 0;
            while(num != 0)
            {
                int aux = num % 10;
                revs *= 10;
                revs += aux;
                num /= 10;
            }
    return revs;
}

int main()
{
    freopen("input2.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t ; cin >> t;
    for(int i = 0; i < t; i ++)
    {
        int a, b; cin >> a >> b;
        int cont = 0;
        for(int j = a; j <= b; j ++)
        {
            if(j == rev(j))
            {
                double num = sqrt(j);
                num *= 10.0;
                int w = (int) num;
                if(w % 10 == 0)
                {
                    w /= 10;
                    if(rev(w) == w) cont ++;
                }

            }
        }
        cout << "Case #" << i + 1 << ": " << cont << endl;
    }
    return 0;
}
