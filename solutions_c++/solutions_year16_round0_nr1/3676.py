#include <bits/stdc++.h>
using namespace std;


long long n, t, seen = 0;

int main() {
    cin>>t;

    for(int test=1; test<=t; test++) {
        cin>>n;

        cout<<"Case #"<<test<<": ";
        if(n == 0) {
            cout<<"INSOMNIA\n";
            continue;
        }

        seen = 0;
        for(int i=1; ; i++) {
            long long new_n = i*n;

            while(new_n) {
                seen |= 1LL << (new_n%10);
                new_n /= 10;
            }

            if(seen == (1<<10) - 1) {
                cout<<i*n<<"\n";
                break;
            }
        }
    }

    return 0;
}
