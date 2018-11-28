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
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        long long d,x,cnt=0,Min=1e9;
        cin>>d;
        vector <int> v;
        for(int j=0;j<d;j++)
        {
            cin>>x;
            v.push_back(x);
        }
        x=*max_element(v.begin(),v.end());
        for(int j=1;j<=x;j++)
        {
            cnt=0;
            for(int k=0;k<v.size();k++)
            {
                if(v[k]>j)
                {
                    if((v[k]-j)%j){cnt+=(v[k]-j)/j; cnt++;}
                    else{cnt+=(v[k]-j)/j;}
                }
            }
            cnt+=j;
            if(cnt<Min){Min=cnt;}
        }
        cout<<"Case #"<<i+1<<": "<<Min<<endl;

    }
    return 0;
}
