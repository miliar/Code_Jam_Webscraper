#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

void megold(istream& in, ostream &out)
{
    double c,f,x;
    in>>c>>f>>x;
    if(x<c) {out<<x/2;
    return;
    }

    double prevtime=x/2;//time for previous iter
    double factime=0;//time to buy factories

    int n=1;//buying this many factories
    while(1)
    {
        factime+=c/(2+(n-1)*f);
        double alltime=factime+x/(2+n*f);
        if(prevtime<alltime) {
            out<<prevtime;
            return;
        }
        prevtime=alltime;
        n++;
    }
}

int main()
{
    ifstream in("B-large.in");
    ofstream out("cookies.out");
    int n;
    in>>n;
    out<<setprecision(12);
    for(int i=1; i<=n; i++)
    {
        out<<"Case #"<<i<<": ";
        megold(in, out);
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
