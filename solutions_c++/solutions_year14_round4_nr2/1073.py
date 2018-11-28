#include<iostream>
#include <cstring>
#include <stdio.h>
#include <cmath>
#include <iomanip>
using namespace std;

int T;
int a[1000];
int b[1000];
int N;
int ans;


void init()
{
    cin >> N;
    for (int i = 0; i < N; i++) { cin >> a[i]; b[i] = 0;}

}



void solve()
{
    ans = 0;
    int l = 0;
    int r = N-1;
    for (int i = 0; i < N; i++)
    {
        int xxx = -1;
        int h = 0;
        for (int j = l; j <= r; j++)
            if (xxx == -1 || xxx > a[j])
            {
                xxx = a[j];
                h = j;
            }
        if ((r-h) > (h-l))
        {
            for (int j = h; j > l; j--)
            {
                int tmp = a[j];
                a[j] = a[j-1];
                a[j-1] = tmp;
                ans++;
            }
            l++;
        }
        else
        {
            for (int j = h; j < r; j++)
            {
                int tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
                ans++;
            }
            r--;
        }
    }
    cout << ans;
}

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        init();
        solve();
        cout << endl;
    }
    return 0;
}
