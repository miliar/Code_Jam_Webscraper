#include<iomanip>
#include<fstream>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("output.txt");
    int T,k;
    double C,F,X,cnt,t0,t1,ans,i;
    fin>>T;
    for(k=1;k<=T;k++)
    {
        fin>>C>>F>>X;
        cnt=0.0;
        i=1.0;
        t1=X/2.0;
        do
        {
            t0=t1;
            cnt=cnt+C/(2.0+(i-1.0)*F);
            t1=cnt+(X/(2.0+(i*F)));
            i=i+1.0;
        }while(t1<=t0);
        fout<<"Case #"<<k<<": ";
        fout<<setprecision(7)<<fixed<<t0<<endl;
    }
    return 0;
}
