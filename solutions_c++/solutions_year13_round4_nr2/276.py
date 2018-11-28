#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
    int T;    
    cin >> T;
    for (int kase=1;kase<=T;++kase)
    {
        long long  n,p;
        cin >> n >> p;
        p--;
        //maxR <= p
        long long maxR = 1LL;
        maxR <<= n;
        maxR--;
        long long R1 = maxR;
        for (int i=0;;++i)
        {
            if (maxR <= p) break;
            maxR -= 1LL << i;
            if (i==0) R1--;
            else R1 -= 1LL << (n-i);
        }

        long long minR = 0, R2 = 0;
        for (int i=0;;++i)
        {
            minR += 1LL<<i;
            if (minR > p) break;
            R2 += 1LL<<(n-1-i);
        }
        
        cout << "Case #" << kase <<": " << R1 << " " << R2 << endl;
    }
    return 0;
}
