#include <iostream>
#include <cstdio>

using namespace std;

int n;
int hz[10];
int nr;

void reset()
{
    for(int i = 0; i < 10; i++)
        hz[i] = 0;
    nr = 0;
}

void solve()
{
    if(n == 0)
    {
        cout << "INSOMNIA" << endl;
        return;
    }
    int x, aux;
    x = 0;
    while(nr < 10)
    {
        x += n;
        aux = x;
        while(aux)
        {
            if(hz[aux%10] == 0) nr++;
            hz[aux % 10]++;
            aux /= 10;
        }
    }
    cout << x << "\n";
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

    int T;
    cin >> T;
    for(int q = 0; q < T; q++)
    {
        cout << "Case #" << q+1 <<": ";
        cin >> n;
        reset();
        solve();
    }
    return 0;
}
