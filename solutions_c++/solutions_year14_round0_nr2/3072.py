#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
    fstream f,g;
    f.open("cookie.in",ios::in);
    g.open("cookie.out",ios::out);
    double C,F,X,minim,time;
    int T,i,n,j,k;
    f>>T;
    for(i=1; i<=T; i++)
    {
        g<<"Case #"<<i<<": ";
        f>>C>>F>>X;
        minim=X/2;
        n=X/C;
        if(n==0)
        {
            g<<setiosflags(ios::fixed)<<setprecision(7)<<X/2;
            g<<'\n';
        }
        else
        {
            for(j=1; j<=n; j++)
            {
                time=C/2;
                for(k=1; k<=j-1; k++)
                    time=time+(C/(2+k*F));
                time=time+(X/(2+j*F));
                if(time<minim)
                    minim=time;


            }
            g<<setiosflags(ios::fixed)<<setprecision(7)<<minim;
            g<<'\n';
        }
    }
}
