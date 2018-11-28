#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ofstream fout;
    fout.open("a.txt",ios::out);
    int t;
    cin>>t;
    int test=1;

    while(test<=t)
    {
        double c,f,x;

        cin>>c;
        cin>>f;
        cin>>x;
        double t1,t2;
        t1=0;
        t2=0;
        double r=2.0;
        double count=0.0;
        t1=x/r;
        while(t1>=0)
        {

            t2=(c/r)+(x/(r+f));
            if(t1>t2)
            {
                t1=(x/(r+f));

                count=count+(c/r);
                r=r+f;
            }
            else
            {
                count=count+t1;
                break;
            }
        }

        fout<<"Case #"<<test<<":"<<" "<<setprecision(11)<<count<<endl;
        test++;
    }
    return 0;
}
