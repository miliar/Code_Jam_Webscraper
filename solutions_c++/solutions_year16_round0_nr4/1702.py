#include <algorithm>
#include <iostream>
#include <numeric>

using namespace std;

typedef unsigned long long ull;


ull compute_position(ull K, ull C, ull p, ull d) 
{
    if(1 >= C)
        return p;
    return compute_position(K, C-1, p*K+d, d);
}


int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cerr.tie(0);

    unsigned T;
    cin >> T;
    for(unsigned t=1; t<=T; ++t)
    {
        int K, C, S;
        cin >> K >> C >> S;
        cout << "Case #" << t << ":";

        for(unsigned p=0; p<K; ++p)
            cout << " " << (1+compute_position(K, C, p, p));
        cout << "\n";
    }
}
