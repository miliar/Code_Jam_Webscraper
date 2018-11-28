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

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        int E, R, N;
        cin>>E>>R>>N;
        vector<int> v;
        v.push_back(0);
        for(int i=0;i<N;i++)
        {
            int x;
            cin>>x;
            v.push_back(x);
        }
        
        vector<vector<int> > ve(N+1, vector<int>());
        ve[0].push_back(E);
        vector<vector<int> > mG(N+1, vector<int>());
        mG[0].push_back(0);
        for(int i=1;i<=N;i++)
        {
            for(int j=0;j<i;j++)
            {
                for(int k=0;k<ve[j].size();k++)
                {
                    for(int e=0;e<=ve[j][k];e++)
                    {
                        mG[i].push_back((e*v[i])+mG[j][k]);
                        ve[i].push_back(min(E, ve[j][k]-e+R));
                    }
                }
        }
        }
        /*
        for(int i=0;i<=N;i++)
        {
            for(int j=0;j<mG[i].size();j++)
            {
                cout<<ve[i][j]<<", "<<mG[i][j]<<" : ";
            }
            cout<<endl;
        }
        */

    cout<<*max_element(mG[N].begin(), mG[N].end())<<endl;
    }

    return 0;
}
