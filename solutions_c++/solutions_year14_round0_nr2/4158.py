#include <stdio.h>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


struct retta
{
    double m;
    double q;
    double tx;
    double tc;
};

int main()
{
    ifstream fin("B-large.in");
    int t;
    fin >> t;
    ofstream fout("output.txt");
    for(int s=1; s<=t; ++s)
    {
        double c,f,x;
        fin >> c >> f >> x;
        vector <retta> rette (1);
        rette[0].m=2.0;
        rette[0].q=0.0;
        rette[0].tx=(x-rette[0].q)/rette[0].m;
        rette[0].tc=(c-rette[0].q)/rette[0].m;
        //printf("%d %.7f %.7f\n",s,rette[0].tx, rette[0].tc);
        do
        {
            retta u;
            rette.push_back(u);
            rette[rette.size()-1].m=rette[rette.size()-2].m+f;
            rette[rette.size()-1].q=-rette[rette.size()-2].tc*rette[rette.size()-1].m;
            rette[rette.size()-1].tx=(x-rette[rette.size()-1].q)/rette[rette.size()-1].m;
            rette[rette.size()-1].tc=(c-rette[rette.size()-1].q)/rette[rette.size()-1].m;
            //printf("%d %.7f %.7f\n",rette.size()-1,rette[rette.size()-1].tx, rette[rette.size()-1].tc);
            if(rette[rette.size()-1].tx>=rette[rette.size()-2].tx)
            break;
            //system("pause");
        }
        while(true);//rette[i-1].tx<rette[i-2].tx);
        //printf("\n%d %.7f\n",i-2,rette[i-2].tx);
        /*for(int j=0; j<rette.size(); ++j)
            printf("%d %.7f\n",j,rette[j].tx);*/

        //printf("\n%d %.7f\n",rette.size()-2,rette[rette.size()-2].tx);
        fout << "Case #" << s << ": ";
        fout.precision(7);
        fout << rette[rette.size()-2].tx << fixed << endl;
    }
}
