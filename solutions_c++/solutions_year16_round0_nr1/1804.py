#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int u[1000];

bool ok(long long x){
    while (x) u[x%10] = 1, x /= 10;
    for (int i = 0; i < 10; i++)
        if (!u[i]) return false;
    return true;
}

void solve(){
    int x;
    cin >> x;
    if (!x) {
        puts("INSOMNIA");
        return;
    }
    int j = 1;
    memset(u,0,sizeof(u));
    while (!ok(x*1LL*j))j++;
    cout << x*j << endl;
 
}


int main()
{
    
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++){
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
