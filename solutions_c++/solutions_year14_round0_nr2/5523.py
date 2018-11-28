#include <cstdio>
#include <iostream>
 
using namespace std;
 
long double p[int(2e5)], t[int(2e5)], b[int(2e5)];
 
int main()
{
        int col;
        cin >> col;
        for ( int ii = 0; ii < col; ii++)
        {
                long double x, f, c, res = int(2e9);
                cin >> c >> f >> x;
                for ( int i = 0; i < x + 2; i++)
                {
                        if ( i != 0)
                        {
                                b[i] = b[i - 1] + c / p[i - 1];
                        }
                        p[i] = i * f + 2;
                        t[i] = b[i] + x / p[i];
                        res = min(res, t[i]);
                }
                printf("Case #%d: %.20lf\n", ii + 1, (double)res);
        }
 
 
        return 0;
}
