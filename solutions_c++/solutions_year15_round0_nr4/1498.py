#include<fstream>
#include<string>
#include<algorithm>

using namespace std;

ifstream f("D-small-attempt0.in");
ofstream g("D.out");

int t,x,r,c,w;
string G,R;

int main()
{
    G="GABRIEL";
    R="RICHARD";
    f>>t;
    for(int i=1;i<=t;++i)
    {
        g<<"Case #"<<i<<": ";
        f>>x>>r>>c;
        if(r<c)
            swap(r,c);
        if(x==1) g<<G<<'\n';
        if(x==2)
        {
            if((r*c)%x==0) g<<G;
            else g<<R;
            g<<'\n';
        }
        if(x==3)
        {
            if(r>=3&&c>=2&&(r*c)%x==0) g<<G;
            else g<<R;
            g<<'\n';
        }
        if(x==4)
        {
            if(r>=4&&c>=3&&(r*c)%x==0) g<<G;
            else g<<R;
            g<<'\n';
        }
        if(x>=7) g<<R<<'\n';
    }
}
