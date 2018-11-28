#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int main()
{
    int i,ans,j,t,tt,a,b,k;
    fin>>tt;
    for(t=1; t<=tt; ++t)
    {
        fin>>a>>b>>k;
        ans = 0;
        for(i=0; i<a; ++i)
            for(j=0; j<b; ++j)
                if((i&j)<k)
                    ans++;
        fout << "Case #"<<t<<": "<<ans<<endl;

    }
    return 0;
}
