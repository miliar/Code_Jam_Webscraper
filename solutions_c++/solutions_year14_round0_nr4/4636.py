#include <iostream>
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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
double m[1000],k[1000];
int t;
int pw,pdw;
int mh,kh;
int n;
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        pw=0;pdw=0;
        cin>>n;
        for(int j=0;j<n;j++)
        {
            cin>>m[j];
        }
        for(int j=0;j<n;j++)
        {
            cin>>k[j];
        }
        sort(m,m+n);
        sort(k,k+n);
        mh=0;kh=0;
        while(mh<n&&kh<n)
        {

                if(k[kh]>m[mh])
                {
                    pw=pw+1;
                    mh=mh+1;
                    kh=kh+1;
                }
                else kh=kh+1;
            //}
        }
        kh=0;mh=0;
        while(kh<n&&mh<n)
        {
            //while(mh<n)
            //{
                if(m[mh]>k[kh])
                {
                    pdw=pdw+1;
                    kh=kh+1;
                    mh=mh+1;
                }
                else mh=mh+1;
                //cout<<m[mh]<<" "<<k[kh]<<endl;
            //}
        }
        cout<<"Case #"<<i+1<<": "<<pdw<<" "<<n-pw<<endl;
    }

    return 0;
}
