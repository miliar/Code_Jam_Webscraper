#include <fstream>
#include <iomanip>
using namespace std;
ifstream in("date.in");
ofstream out("date.out");
int main()
{
    long double c,f,x,q,nr,x1;
    short t,t1;
    in>>t;
    out<<fixed;
    for(t1=1;t1<=t;++t1)
    {

        in>>c>>f>>x;
        if(x<=c) out<<"Case #"<<t1<<": "<<setprecision(7)<<x/2<<'\n';
        else
        {
            q=2;
            nr=0;
            x1=x-c;
            while((x1/q)>(x/(q+f)))
            {
                nr=nr+c/q;
                q+=f;
            }
            nr=nr+x/q;
            out<<"Case #"<<t1<<": "<<setprecision(7)<<nr<<'\n';
        }

    }
    return 0;
}
