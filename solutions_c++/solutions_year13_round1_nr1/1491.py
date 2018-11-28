#include <iostream>
#include <cstdio>
using namespace std;

int main(void)
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
        cout << "Case #" << i << ": ";
        long long r, paint;
        cin >> r >> paint;

        long long int ring;
        for(ring = 0; paint >= (2*r+4*ring+1) ; ++ring)
        {
            paint -= (2*r+4*ring+1);
            //fprintf(stderr, "%lld ring: costs %lld, remains %lld\n", ring, 2*r+4*ring+1, paint);
        }
        cout << (ring) << endl;
        //cout << (paint - (2 * r) + 1)/2 << endl;
    }
    return 0;
}
