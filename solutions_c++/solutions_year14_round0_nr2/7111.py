#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

fstream in, out;
double solve()
{
    double C, F, X;
    in >> C >> F >> X;
    double p_res, res = 0.;
    int x = -1;

    do
    {
        ++x;
        p_res = res;
        res += C/(2 + x *F); 

    } while( (p_res + X/(2. + x*F)) > (res + X/(2. + x*F + F)));

    return p_res + X/(2. + x*F);
}

int main()
{
    in.open("a.txt"); out.open("out.txt"); 
    int T;
    in >> T;
    for(int i = 1; i <= T; ++i)
        out << "Case #" << i << ": " << fixed << setprecision(7) <<solve() << endl;

    return 0;
}
