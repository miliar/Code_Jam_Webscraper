#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
int n;
int a[1005];
void init()
{
    n = 0;
    memset(a, 0, sizeof(a));
    cin >> n;
    for( int i = 0; i <= n; i++) {
        char x;
        cin >> x;
        a[i] = x - '0';
    }
}
void work()
{
    int tot = 0, ans = 0;
    for( int i = 0; i <= n; i++) {
        if( tot < i ) {
            ans += i - tot;
            tot += i - tot;
        }
        tot += a[i];
    }
    cout << ans << endl;
}
int main(void)
{
    int cs;
    cin >> cs;
    for( int i = 1; i <= cs; i++) {
        init();
        cout << "Case #" << i << ": ";
        work();
    }
    return 0;
}
