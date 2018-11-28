#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

double a[1002];
double b[1002];
int n;

void try2()
{
     int fs1,ls1;
     int ls2;
     fs1 = 0;
     ls1 = ls2 = n-1;
     int ans = 0;
     while ( fs1 <= ls1 && ls2 >= 0 ) {
         if ( a[ls1] > b[ls2] ) {
            ans++;
            ls1--;
            ls2--;
         }
         else {
             fs1++;
             ls2--; 
         }
     }
     cout << ans;
     return;
}

void war()
{ 
     bool chk[1002];
     memset(chk, false, sizeof(chk));
     int ans = 0;
     for ( int i = 0; i < n; i++ ) {
         for ( int j = 0; j < n; j++ ) {
             if ( chk[j] ) continue;
             if ( b[j] > a[i] ) {
                  chk[j] = true;
                  ans++;
                  break;
             }
         }
     }
     cout << n-ans;
     return;
}

int main()
{
    int t,l;
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    for ( int l = 1; l <= t; l++ ) {
        cin >> n;
        for ( int i = 0; i < n; i++ ) cin >> a[i];
        for ( int i = 0; i < n; i++ ) cin >> b[i];
        sort(a,a+n);
        sort(b,b+n);
        cout << "Case #" << l << ": "; 
        try2();
        cout << " ";
        war();
        cout << endl;
    }
    return 0;
}
