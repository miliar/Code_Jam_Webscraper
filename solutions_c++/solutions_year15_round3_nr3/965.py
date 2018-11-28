#include <iostream>
#include <set>
using namespace std;

int main()
{
    set<int>::iterator it, eit;
    long long c, v;
    int t, d, denom, res;
    cin >> t;

    for(int tt=1; tt<=t; ++tt) {
        set<int> den;
        cin >> c >> d >> v;

        for(int i=0; i<d; ++i) {
            cin >> denom;
            den.insert(-denom);
        }

        res = 0;
        for(long long i=1; i<=v; ++i) {
            it = den.begin();
            eit = den.end();

            long long req = i;
            while(it != eit) {
                long long cur = -(*it);
                long long num = req/cur;
                req -= cur * min(c, num);
                ++it;
            }

            if (req > 0) {
                res++;
                den.insert(-i);
            }
        }

        cout << "Case #" << tt << ": " << res << endl;
    }
    return 0;
}
