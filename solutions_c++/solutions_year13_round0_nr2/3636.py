
#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
#include <queue>        //max heap implementation
#include <limits.h>




#define pub push_back
#define pob pop_back
#define puf push_front
#define pof pop_front
#define mkp make_pair
#define fi first
#define se second
#define debug(a) { for( typeof(a.begin()) it = a.begin() ; it != a.end() ; it++ ) cout << *it << " "; cout << endl; }

using namespace std;

//class comparators for queue and others
class classcomp{
    public:
        bool operator() (const int& l, const int& r)const{
            return l<r;
        }
};

#define ll long long

int main()
{
    freopen("input1.txt","r",stdin);
    freopen("output.txt","w",stdout);

        int t,n,m,maxi;
    cin>>t;
    for(int i=1;i<=t;++i)
    {   int a[105][105],maxr[105],maxc[105],f=0;
        cin>>n>>m;
        for(int j=1;j<=n;++j)
        {maxi=0;
        for(int k=1;k<=m;++k)
        {
            cin>>a[j][k];
            if(a[j][k]>maxi)maxi=a[j][k];
        }
         maxr[j]=maxi;
        }

        for(int j=1;j<=m;++j)
        {   maxi=0;
            for(int k=1;k<=n;++k)
            {
                if(a[k][j]>maxi)maxi=a[k][j];
            }
            maxc[j]=maxi;
        }

         for(int j=1;j<=n;++j)
        {   //max=0;
            for(int k=1;k<=m;++k)
            {
                if(a[j][k]<maxr[j] && a[j][k]<maxc[k])
                {f=1;break;}
            }

        }if(f==1)
        cout<<"Case #"<<i<<":"<<" "<<"NO"<<endl;
        else
        cout<<"Case #"<<i<<":"<<" "<<"YES"<<endl;

    }


}
