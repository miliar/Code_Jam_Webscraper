#include<bits/stdc++.h>

using namespace std;

int main()
{
    ofstream oyf("yes.txt");
    ifstream myf("sam.txt");
    if(myf.is_open()){
    int t,x=1;
    myf>>t;
    while(t--)
    {
        double f,c,e,r=2.0,t=0.0;
        myf>>c>>f>>e;
        if(e<=c)
            t=e/r;
        else
        {
            while(true)
            {
                double t1,t2;
                t1=e/r;
                t2= (c/r);
                r+=f;
                t2+=(e/r);
                if(t1<=t2)
                {
                    t+=t1;
                    break;
                }
                t+=(t2-(e/r));
            }
        }
        oyf<<"Case #"<<x++<<": "<<fixed<<setprecision(7)<<t<<endl;
    }}
    return 0;
}
