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
    int T;
    cin>>T;
    vector<int> ans;
    

    for(int i=0;i<T;i++)
    {
        ans.push_back(0);
        int S[2000];
        int Smax;
        cin>>Smax;
        
        for(int j=0;j<=Smax;j++)
        {
            char dummy;
            cin>>dummy;
            S[j]=dummy-'0';
        }
        int sum=0;
        ans[i]=0;
        for(int k=1;k<=Smax;k++)
        {
            sum+=S[k-1];
            S[k-1]+=max(0,k-sum);
            ans[i]+=max(0,k-sum);
            sum+=max(0,k-sum);
        }

    }
    for(int i=0;i<T;i++)
    {
        cout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
    }
    return 0;
}