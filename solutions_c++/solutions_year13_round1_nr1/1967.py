#include <iostream>
using namespace std;

inline long long sqr(unsigned long long x)
{
    return x*x;
}

int main()
{
    unsigned long long T, r, t, count, S, area;
    cin >> T;
    for(int it = 1; it <= T; it++)
    {
        cin >> r >> t;
        area = S = sqr(r+1) - sqr(r); // area of the first circle in mililitres
        count = 1;
        while(1)
        {
            area += 4;
            S += area;
            if(S > t) break;
            count++;
        }
        //
        cout << "Case #" << it << ": " << count << '\n';
    }
    cout << flush;
    return 0;
}