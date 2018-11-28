#include<iostream>
#include <cstring>
#include <stdio.h>
#include <cmath>
#include <iomanip>
using namespace std;

int T;
int N, X,ans;
int a[10000];
int b[10000];



void init()
{
    cin >> N >> X;
    for (int i = 0; i < N; i++) {cin >> a[i]; b[i] = 0;}
}

void qsort()
{
    for (int i = 0; i < N; i++)
        for (int j = 0; j < i; j++)
            if (a[j] > a[i])
    {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
}

void solve()
{
    qsort();
    ans = 0;
    for (int i = N-1; i >= 0; i--)
        if (b[i] == 0)
        {
            for (int j = i-1; j >=0; j--)
            if (a[i]+a[j] <= X && b[j] == 0)
            {
                b[j] = 1;
                break;
            }
            ans++;
        }
    cout << ans;

}

int main() {
    freopen("A-large (1).in", "r", stdin);
    freopen("A-large (1).out", "w", stdout);
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        init();
        solve();
        cout << endl;
    }
    return 0;
}

