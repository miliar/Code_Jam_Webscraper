#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <queue>
using namespace std;

typedef long long LL;


int main()
{
    std::ios_base::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
        freopen("22.in","r",stdin);
    #endif
    int t;
    cin>>t;
    for(int x=1;x<=t;x++)
    {
        long long int a,b,k;
        cin>>a>>b>>k;
        long long int res=0;
        for(long long int i=0;i<a;i++)
        {
            for(long long int j=0;j<b;j++)
            {
                long long int tmp=i&j;
                if(tmp<k)
                    res++;
            }
        }
        cout<<"Case #"<<x<<": "<<res;
        if(x!=t)
            cout<<endl;
    }
    return 0;
}
