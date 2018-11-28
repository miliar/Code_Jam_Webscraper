#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

set<int> x;

void solve(long long n)
{
    while(n > 0){
        x.insert(n % 10);
        n /= 10;
    }
}


int main()
{
    freopen("a.txt", "r", stdin);
    freopen("b.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;

    for(int i=1;i<=t;i++){
        int n;
        cin >> n;
        if(n==0){
            cout << "Case #" << i << ": " << "INSOMNIA" << endl;
            continue;
        }
        x.clear();
        solve(n);
        long long  a = n;
        while(x.size() < 10){
            a += n;
            solve(a);
        }
        cout << "Case #" << i << ": " << a << endl;
    }
    return 0;
}
