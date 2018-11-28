#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <map>

using namespace std;

int main() {
    int zc;
    cin>>zc;
    for(int tc=1;tc<=zc;tc++)
    {
        int result = 0;
        int maxS;
        cin>>maxS;
        int cur, totalStanding;
        totalStanding = 0;
        getchar();
        for(int s=0; s<=maxS; s++)
        {
            cur=getchar()-48;
            if(totalStanding<s)
            {
                result+=s-totalStanding;
                totalStanding+=s-totalStanding;
            }
            totalStanding+=cur;

        }       
        cout<<"Case #"<<tc<<": "<<result<<endl;
    }
    return 0;
}


