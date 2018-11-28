#include <iostream>
#include <fstream>

using namespace std;

int main()
{

    fstream input("input.txt"), out("output.txt");
    int T, n, Z = 0;
    double c, F, Y, res, res1, rem;
    input >> T;
    while(Z<T)
    {

    input >> c >> F >> Y;
    n=0;
    res = Y/2;
    while(1) {
/*
    for(int i = 0; i < n; i++)
        rem+=c/(2+i*F);
    res1=rem+Y/(2+n*F);
    */
if(n>0)
        rem+=c/(2+(n-1)*F);
    res1=rem+Y/(2+n*F);


    if(res1 > res)
        break;
    else
        res = res1;
    n++;
    //rem=0;
    }
    rem=0;
    out.setf( ios::fixed );
    out.precision( 7 );
    out << "Case #" << Z+1 << ": " << res << endl;

    Z++;
    }
    /// res is result

    return 0;
}
