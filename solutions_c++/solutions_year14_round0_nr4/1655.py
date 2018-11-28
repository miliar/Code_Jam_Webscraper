#include<iostream>
#include <cstring>
#include <stdio.h>
#include <cmath>
#include <iomanip>
using namespace std;

int T;
double a[1000],b[1000];
int n;
void init()
{
    cin >> n;
    for (int i = 0; i < n; i++) cin>>a[i];
    for (int i = 0; i < n; i++) cin>>b[i];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < i; j++)
            if (a[i] < a[j])
            {
                double tmp = a[i];
                a[i] = a[j];
                a[j] = tmp;
            }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < i; j++)
            if (b[i] < b[j])
            {
                double tmp = b[i];
                b[i] = b[j];
                b[j] = tmp;
            }
}

void solve()
{
    int ans = 0;
    int k = 0,h;
    int c[1000], check;
    for (int i = 0; i < n; i++) c[i] = 0;
    for (int i = 0; i < n; i++)
    {
        check = 0;
        for (int j = 0; j < n; j ++)
            if (b[j] < a[i] && c[j] == 0)
            {
                check = 1;
                c[j] = 1;
                break;
            }
        if (check == 1)
        {
            ans++;
        }
        else
            for (int j = n-1; j >= 0; j--)
            if (c[j] == 0)
            {
                c[j] == 1;
                break;
            }
    }
    cout << ans << ' ';
    for (int i = 0; i < n; i++) c[i] = 0;
    h = 0;
    ans = 0;
    for (int i = 0; i < n; i++)
    {
        check = 0;
        for (int j = 0; j < n; j++)
            if (b[j] > a[i] && c[j] == 0)
            {
                ans++;
                c[j] = 1;
                check = 1;
                break;
            }
        if (not check)
        for (int j = 0; j < n; j++)
            if (c[j] == 0)
            {
                c[j] = 1;
                break;
            }
    }
    cout << n-ans;

}

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        init();
        solve();
        cout << endl;
    }
    return 0;
}
