#include<iostream>
#include<iomanip>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int a[10000 + 10];
int n;
bool check()
{
     int i , k;
     k = 0;
     for (i = 0; i < n - 1; i++)
         if (a[i] > a[i + 1]) break;
     k = 1;
     for (; i < n - 1; i++)
         if (a[i] < a[i + 1]) break;
     if (i >= n) return true;
     return false;
}

int main()
{
    int ts, ks, i, fl, fr, k, l, r, ans;
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    cin >> ts;
    for (ks = 0; ks < ts; ks++){
        cin >> n;
        for (i = 0; i < n; i++) cin >> a[i];
        l = 0; r = n - 1;
        ans = 0;
        for (int t = 0; t < n; t++){
            k = l;
            for (i = l + 1; i <= r; i++)
                if (a[i] < a[k]) k = i;
            fl = k - l;
            fr = r - k;
            if (fl <= fr){
               ans += fl;
               for (i = k; i > l; i--)
                   a[i] = a[i - 1];
               l++;
            }
            if (fl > fr){
               ans += fr;
               for (i = k; i < r; i++)
                   a[i] = a[i + 1];
               r--;
            }
        }
        printf("Case #%d: %d\n", ks + 1, ans);
    }
}
