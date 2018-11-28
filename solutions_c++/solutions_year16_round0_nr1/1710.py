#include <algorithm>
#include <iostream>

using namespace std;
typedef unsigned long long ull;

void update_digits(unsigned &digits, ull v) 
{
    for(; v; v /= 10) {
        unsigned d = v%10;
        digits |= 1 << d;
    }
}


int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cerr.tie(0);

    size_t T;
    cin >> T;

    for(size_t t=1; t<=T; ++t) {
        std::cout << "Case #" << t << ": ";
        
        ull n;
        cin >> n;
        if(0 == n) {
            cout << "INSOMNIA\n";
            continue;
        }

        unsigned v = 0;
        unsigned digits = 0;
        do {
            v += n;
            update_digits(digits, v);
        } while(digits != 0x3FF);
        cout << v << "\n";
    }
}
