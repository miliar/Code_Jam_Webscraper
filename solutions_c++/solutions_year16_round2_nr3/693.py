#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

const int N = 20;

string a[N], b[N];
int n;
bool fake[N];

bool ok(int mx, int x = 0){
    if (!mx || x == n){
        if (mx) return 0;
        for (int i = 0; i < n; i++){
            bool f = 0, s = 0;
            if (fake[i]){
                for (int j = 0; j < n; j++)
                    if (!fake[j]){
                        if (i != j && a[i] == a[j]) f = 1;
                        else if (i != j && b[i] == b[j]) s = 1;
                    }
                if (!f || !s) return 0;
            }
        }
        return 1;
    }
    bool ret = 0;
    fake[x] = 1; ret |= ok(mx-1,x+1); fake[x] = 0;
    ret |= ok(mx,x+1);
    return ret;
}

void solve()
{
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i] >> b[i];
    
    for (int i = n-2; i >= 0; i--)
        if (ok(i)) {
            cout << i << endl;
            return;
        }
}

int main()
{
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        cout << "Case #" << tt << ": ";
        solve();
    }

    return 0;
}
