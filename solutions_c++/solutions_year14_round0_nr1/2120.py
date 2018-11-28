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

LL gcd(LL a, LL b) { return b?gcd(b,a%b):a; }

int main()
{
    std::ios_base::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
        freopen("in1.in","r",stdin);
    #endif
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        int r1,r2,arr[4][4],brr[4][4];
        cin>>r1;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin>>arr[j][k];
            }
        }
        cin>>r2;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin>>brr[j][k];
            }
        }
        r1--;r2--;
        int cnt=0,res;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(arr[r1][j]==brr[r2][k])
                {
                    cnt++;res=brr[r2][k];
                }
            }
        }
        //cout<<r1<<" "<<r2<<endl;
        if(cnt==1)
            cout<<"Case #"<<i<<": "<<res<<endl;
        else if(cnt==0)
            cout<<"Case #"<<i<<": Volunteer cheated!\n";
        else
            cout<<"Case #"<<i<<": Bad magician!\n";
    }
    return 0;
}
