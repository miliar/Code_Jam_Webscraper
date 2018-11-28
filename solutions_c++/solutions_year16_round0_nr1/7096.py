#include <iostream>
#include <cstring>
using namespace std;

int main() {
    long long t,n,i;
    bool found[10];
    cin>>t;
    for(i=1;i<=t; i++) {
        memset(found, 0, sizeof(found));
        cin >> n;
        if(n == 0) {
            cout << "Case #" << i << ": INSOMNIA\n";
            continue;
        }
        long long multiplier = 1, cnt= 0;
        while(cnt < 10) {
            long long val = n*multiplier;
            while(val > 0) {
                if(found[val%10] == 0) {
                    found[val%10] = 1;
                    cnt++;
                }
                val /= 10;
            }
            multiplier++;
        }
        cout << "Case #"<<i << ": " << n*(multiplier-1) << endl;
    }
    return 0;
}
