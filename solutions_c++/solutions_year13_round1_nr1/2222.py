#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
const double pi=acos(-1);
int main()
{
    int T;
    while(cin>>T)
    {
  //      freopen("A-small-attempt2.in","r",stdin);
        freopen("A-small-attempt2.txt","w",stdout);
        for(int x=1;x<=T;x++)
        {
            long long r,t;
            cin>>r>>t;
            long long i;
            long long sum=0;
            for(i=1;;i++)
            {
                sum+=4*i+2*r-3;
                if(sum>t)
                {
                    break;
                }
            }
            cout<<"Case #"<<x<<": "<<i-1<<endl;
        }
    }
    return 0;
}
