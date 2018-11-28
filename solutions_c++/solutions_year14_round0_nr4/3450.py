#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
    int t;
    ifstream fe("D-large.in");
    ofstream fs("D-large.out");
    fe>>t;
    for (int q=1; q<=t; q++)
    {
        int n;
        fe>>n;
        vector <double> na(n),ke(n);
        for (int w=0; w<n; w++)
        {
            fe>>na[w];
        }
        for (int w=0; w<n; w++)
        {
            fe>>ke[w];
        }
        sort (na.begin(),na.end());
        sort (ke.begin(),ke.end());
        vector <double> na1=na;
        vector <double> ke1=ke;
        int cd=0,cw=0;
        bool df;
        for (int p=n-1; p>=0; p--)
        {
            df=false;
            for (int m=0; m<n; m++)
            {
                if (ke[p]<na[m])
                {
                    ke[p]=0;
                    na[m]=0;
                    cd++;
                    m=n;
                    df=true;
                }
            }
            if (df==false)
            {
                ke[p]=0;
                na[0]=0;
            }
        }
        bool fg;
        for (int p=n-1; p>=0; p--)
        {
            fg=false;
            for (int m=0; m<n; m++)
            {
                if (na1[p]<ke1[m])
                {
                    na1[p]=0;
                    ke1[m]=0;
                    cw++;
                    m=n;
                    fg=true;
                }
            }
            if (fg==false)
            {
                na1[p]=0;
                ke1[0]=0;
            }
        }
        cw=n-cw;
        fs<<"Case #"<<q<<": "<<cd<<" "<<cw<<endl;
    }
    return 0;
}
