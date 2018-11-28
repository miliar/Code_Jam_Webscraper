#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream cin("counting.in");
    ofstream cout("counting.out");
    int q; cin >> q;
    for(int a = 0;a<q;a++){
        int n; cin >> n;
        cout << "Case #" << a+1 << ": ";
        if(n == 0){
            cout << "INSOMNIA\n";
            continue;
        }
        long long num = n;
        for(int seen = 0;seen < (1<<10)-1;num += n){
            for(long long cur = num;cur;cur/=10)
                seen |= 1 << (cur%10);
        }
        cout << num-n << "\n";
    }
    return 0;
}
