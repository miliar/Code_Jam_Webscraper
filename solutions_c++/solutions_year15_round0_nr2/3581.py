#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cctype>
#include <math.h>
#include <cstdlib>

using namespace std;


int main()
{
    ifstream file;
    file.open("B-large.in");
    int T;
    file>>T;
    vector<int>ans;

    for(int i=0;i<T;i++)
    {
        int D;
        vector<int> P;

        file>>D;
        for(int j=0;j<D;j++) 
        {
            int dummy;
            file>>dummy;
            P.push_back(dummy);
        }
        
        int maxim=0;
        for(int k=0;k<P.size();k++) if (maxim<P[k]) maxim=P[k];
        
        int candid=maxim;

        for(int g=1;g<=maxim;g++)
        {
            int dummy=g;
            for(int k=0;k<P.size();k++)
            {
                dummy+=max(0,(P[k]-1)/g);
            }
            candid=min(candid,dummy);
        }
        ans.push_back(0);
        ans[i]=candid;
    }
    for(int i=0;i<T;i++)
    {
        cout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
    }
    return 0;
}