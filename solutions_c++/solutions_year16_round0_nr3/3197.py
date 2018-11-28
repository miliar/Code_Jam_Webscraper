#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
using namespace std;

int t, n, j, generated = 0;

void print_bin(ull x) {
    for(int i=n-1; i>=0; i--)
        if(x&(1<<i))
            cout<<"1";
        else
            cout<<"0";

    cout<<" ";
}

ull to_base(ull x, ull base) {
    ull power=1, ret=0;
    for(int i=0; i<32; i++) {
        if(x & (1<<i))
            ret += power;
        power *= base;
    }
    return ret;
}

ull get_div(ull x) {
    for(ull i=2; i*i<=x; i++)
        if(x % i == 0)
            return i;
    return 0;
}

vector <int> divs;

int main() {
    cin>>t>>n>>j;

    cout<<"Case #1:\n";

    for(ull x=0; x < (ull)(1<<(n-1)) && generated < j; x++) {
        ull y = 1<<(n-1) | (x<<1) | 1;

        //print_bin(y);

        bool ok = true;
        divs.clear();
        for(ull base=2; base<=10 && ok; base++) {
            ull repr = to_base(y, base);

            ull div = get_div(repr);
            if(!div)
                ok = false;
            else
                divs.push_back(div);
        }

        if(ok) {
            print_bin(y);
            for(auto div:divs)
                cout<<div<<" ";
            cout<<"\n";

            generated++;
            cerr<<generated<<"\n";
        }

        //cout<<"\n\n";

    }

    return 0;
}

