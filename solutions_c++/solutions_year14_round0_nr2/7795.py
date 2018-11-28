#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;

ifstream fin ("B-large.in");
ofstream fout ("B-large.out");

int test;
long double speed1,speed2,c,f,x,minv;

int main()
{
    fin>>test;

    for (int k=1; k<=test; ++k)
    {
        fin>>c>>f>>x;

        long double minv = x/2;

        speed1 = 0;

        for (int i=1; i<=x; ++i)
        {
            speed1 = speed1 + c/(2+(i-1)*f);
            speed2 = x/(2+i*f);

            minv = min (minv,speed1+speed2);
        }

        fout<<"Case #"<<k<<": ";

        fout<<fixed<<setprecision(7)<<minv<<"\n";
    }
}
