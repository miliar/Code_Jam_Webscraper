#include <fstream>
#include<cstring>
#include<iomanip>
using namespace std;

ifstream fin("cookie.in");
ofstream g("cookie.out");

int t;
double c,f,x,r;

int main()
{
    fin>>t;
    int i,j;
    double s,s1,s2;
    g << std::fixed << std::setprecision(7);
    for(i=1;i<=t;i++){
        fin>>c>>f>>x;
        s=0.0000000;
        r=2.0000000;
        s1=x/r;
        s2=c/r;
        s2=s2+x/(r+f);
        while(s1>s2){
            s1=x/r;
            s2=c/r;
            r=r+f;
            s2=s2+x/r;
            //g<<s<<" ";
            if(s1>s2)
                s=s+c/(r-f);
        }
        s=s+s1;
    g<<"Case #"<<i<<": "<<s<<"\n";
    }
    return 0;
}
