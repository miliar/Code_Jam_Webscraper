#include<fstream>
#include<iomanip>

using namespace std;

int main()
{
    ifstream fr;
    ofstream fw;
    fr.open("B-large.in");
    fw.open("B-small.out");
    int t;
    double c,f,x;
    fr>>t;
    for(int l=1;l<=t;l++){
    fr>>c>>f>>x;
    double old=x/2.0,nw=(c/2.0)+(x/(2.0+f));
    double p=(x/(2.0+f));
    double f1=2.0+f;
    while(nw<=old)
    {
        old=nw;
        nw=nw-p+c/f1+x/(f1+f);
        f1=f1+f;
        p=x/f1;
    }
    fw<<"Case #"<<l<<": ";
    fw<<fixed<<setprecision(7)<<old<<endl;
    }
    return 0;
}
