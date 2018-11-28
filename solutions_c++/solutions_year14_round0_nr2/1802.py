#include<fstream>
#include<iostream>
#include<vector>
using namespace std;
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("out.txt");
    int t;
    fin>>t;
    fout.setf(ios::fixed, ios::floatfield );
    fout.precision(7);
    for(int i=1;i<=t;i++)
    {
        double c,f,x;
        double rate = 2.0;
        fin>>c>>f>>x;
        double ans = 0.0;
        if(x<=c)
            ans = x/rate;
        else
        {
            double t1 = (c/rate) + (x/(rate+f));
            double t2 = (x/rate);
            while(t2>t1)
            {
                ans+=c/rate;
                rate += f; // I just got a farm faggots.
                t1 = (c/rate) + (x/(rate+f));
                t2 = (x/rate);
            }
            ans += t2;
        }
        fout<<"Case #"<<i<<": "<<ans<<endl;
    }

    fin.close();
    fout.close();
    return 0;
}
