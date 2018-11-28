#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int T,correct,ntest=1;
    ll n,i,aux;
    cin >> T;
    while(T--)
    {
        cout << "Case #" << ntest++ << ": ";
        cin >> n;
        if(n == 0)
            cout << "INSOMNIA" << '\n';
        else
        {
            correct = (1 << 10) - 1;
            i = 1;
            while(correct)
            {
                aux = n * i;
                i++;
                while(aux > 0)
                {
                    int dig = aux % 10;
                    aux /= 10;
                    if(correct & (1 << dig))
                        correct = correct & ~(1 << dig);
                }
            }
            cout << n * (i-1) << '\n';
        }
    }
    return 0;
}