#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

bool isGood(vector<vector<int> > &v)
{
    for(int i=0;i<v.size();i++)
    {
        for(int j=0;j<v[i].size();j++)
        {
            bool isOk = true;
            int curr = v[i][j];
            for(int k=0;k<v.size();k++)
            {
                if(v[k][j]>curr)
                    isOk = false;
            }
            if(isOk)
                continue;
            isOk = true;
            for(int k=0;k<v[i].size();k++)
            {
                if(v[i][k]>curr)
                    isOk = false;
            }
            if(!isOk)
                return false;
        }
    }
    return true;
}

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        int N, M;
        cin>>N>>M;
        vector<vector<int> >v;
        for(int i=0;i<N;i++)
        {
            vector<int> vv;
            for(int j=0;j<M;j++)
            {
                int ii;
                cin>>ii;
                vv.push_back(ii);
            }
            v.push_back(vv);
        }
        if(isGood(v))
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }

    return 0;
}
