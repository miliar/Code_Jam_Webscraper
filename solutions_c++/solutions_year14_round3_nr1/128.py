#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

long long gcd (long long a, long long b) {
	return b ? gcd (b, a % b) : a;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ": ";
        long long p,q;
        char c;
        cin >> p >> c >> q;
        long long g = gcd(p, q);
        p /= g;
        q /= g;
        long long x = q;
        bool f = true;
        int ans = 0;
        while (x > 1){
            if (x % 2)
                f = false;
            x /= 2;
            ans++;
        }
        if (!f){
            cout << "impossible" << endl;
        }else{
            long long x = 1;
            for (int i=0;i<=ans;i++){
                if (x*p >= q){
                    cout << i << endl;
                    break;
                }
                x *= 2;
            }
        }
    }
    return 0;
}
