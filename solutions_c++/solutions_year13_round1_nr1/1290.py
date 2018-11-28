#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;

typedef unsigned long long ULL;

void print(int i, ULL ans)
{
    cout << "Case #" << i << ": " << ans << endl;
}


ULL foo( ULL r, ULL I)
{
//    return ((2*(r+1)-1)+2*(r+2*I)-5)*I/2;
    return (2*(r+1)+2*I-3)*I;
}

int main()
{
    int T;
    cin >> T;
    for (int tT=0;tT<T;++tT)
    {
        ULL t, r;
        cin >> r >> t;
        ULL min_e = 0;
        ULL max_e = min(t/(2*r)+100,(ULL)sqrt(t)+100);
        while ( min_e < max_e)
        {
            ULL mid = (min_e + max_e+1) >> 1;
            ULL rmid = foo( r,mid);
//            cout << min_e << " " << max_e << ": ";
//            cout << mid << " " << rmid <<endl;
            if ( rmid <= t)
            {
                min_e = mid;
            } else
            {
                max_e = mid-1;
            }
        }

        print( tT+1, min_e);

    }
    return 0;
}

