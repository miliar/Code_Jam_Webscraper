#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("op.txt");
    double c, f, x, t, r;
    int tc, v=0;
    fin>>tc;
    while(tc--)
    {
        v++;
        fin>>c>>f>>x;
        r=2, t=0;
        while((x/r)>(c/r)+(x/(r+f))){
            t=t+(c/r);
            r=r+f;
        }
        t=t+(x/r);
      fout<<fixed<<setprecision(10)<<"Case #"<<v<<": "<<t<<endl;

    }
    return 0;
}
