#include <stdio.h>
#include <iostream>

using namespace std;

int n, k;
int a[10001];

void Enter()
{
    scanf("%d", &n);
    for(int i = 0; i <= n; i++)
    {
        char ch;
        cin >> ch;
        a[i] = int(ch) - int('0');
    }
}

void Solve()
{
    long long dem = a[0];
    long long kq  = 0;
    for(int i = 1; i <= n; i++)
    {
        if (dem >= i) dem += a[i];
        else
        {
            kq += i - dem;
            dem = i + a[i];
        }
    }
    cout << "Case #" << k<<":"<<" "<<kq<<endl;
}

int main()
{
    int t;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &t);
    for(k = 1; k <= t; k++)
    {
        Enter();
        Solve();
    }
    fclose(stdin);
    fclose(stdout);
}
