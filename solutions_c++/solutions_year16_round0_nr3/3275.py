#include <cstdio>
#include <string>
#include <iostream>
#include <cstdlib>
using namespace std;

int n, num, tot;

int a[40];
int c[11];

void judge()
{
    for (int i = 2; i <= 10; ++i)
    {
        long long b = 0;
        for (int j = 1; j <= n; ++j) b = b * i + (long long)a[j];
        //cout << b[i] << endl;
        bool ok = false;
        for (long long j = 3; (long long)j * (long long)j <= b; ++j)
        {
                if (b % j == 0) {
                                ok = true;
                                c[i] = j;
                                break;
                }
        }
        if (!ok) return;
    } 
    tot ++;
    for (int i = 1; i <= n; ++i) cout << a[i];
    for (int i = 2; i <= 10; ++i) cout << " " << c[i];
    cout << endl;
}

void check(int i)
{
    if (i == n)
    {
        a[i] = 1;
        judge();
        return;
    }
    if (tot < num) {a[i] = 0; check(i + 1);}
    if (tot < num) {a[i] = 1; check(i + 1);}
}

void work()
{  
    int t;
    cin >> t;
    for (int l = 0; l < t; ++l)
    {
        cin >> n >> num;
        cout << "Case #" << l + 1 << ":" << endl;
        tot = 0;
        a[1] = 1;
        check(2);   
    }
}


int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    work();
    return 0;
}
