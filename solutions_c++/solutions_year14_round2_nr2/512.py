#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int A, B, k;

void solve(){
    int res = 0;
    cin >> A >> B >> k;
    for (int i = 0; i < A; i++)
        for (int j = 0; j < B; j++)
            if ((i&j) < k) res++;
    cout << res << endl;

}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}
