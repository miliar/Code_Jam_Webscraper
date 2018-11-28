#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <math.h>
#include <queue>
#include <string.h>
#include <sstream>
#define fo(i,n) for(i=0;i<n;i++)
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back
#define mp make_pair
using namespace std;

typedef long long ll;

int a[120][120];
int n, m;

bool check() {
    int i, j, ii, jj;
    fo(i,n) {
        fo(j,m) {
            bool lar = false;
            fo(ii, n)
                if (a[ii][j] > a[i][j])
                    lar = true;
            if (!lar) continue;
            fo(jj, m)
                if (a[i][jj] > a[i][j])
                    return false; 
        }
    }
    return true;
}

int main(void) {
    int t, tt;
    cin >> t;
    
    fo(tt, t) {
        cin >> n >> m;
        int i, j;
        fo(i, n) {
            fo(j, m) {
                scanf("%d", &a[i][j]);
                // cout << a[i][j] << endl;
            }
        }
        cout << "Case #" << tt + 1 << ": " << (check() ? "YES" : "NO") << endl;
    }
}
