#include<fstream>
using namespace std;
int main()
{
    ifstream in("p.in");
    ofstream out("p.out");
    int t,x,r,c,i;
    in>>t;
    for(i=1;i<=t;i++)
    {
        in>>x>>r>>c;
        if(x==1) out<<"Case #"<<i<<": GABRIEL"<<"\n";
        if(x==2)
        {
                if((r*c)%2==0) out<<"Case #"<<i<<": GABRIEL"<<"\n";
                else out<<"Case #"<<i<<": RICHARD"<<"\n";
        }
        if(x==3)
        {
            if((r*c)%3==0 && r*c>3) out<<"Case #"<<i<<": GABRIEL"<<"\n";
            else out<<"Case #"<<i<<": RICHARD"<<"\n";
        }
        if(x==4)
        {
            if(r*c==12 || r*c==16) out<<"Case #"<<i<<": GABRIEL"<<"\n";
            else out<<"Case #"<<i<<": RICHARD"<<"\n";
        }
    }
    return 0;
}
