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
        freopen("in22.in","r",stdin);
    #endif
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double tme=0,speed=2;
        while(1)
        {
            double tmp=c/speed;
            tmp+=x/(speed+f);
            if(x/speed<=tmp)
            {
                tme+=x/speed;
                break;
            }
            tme+=c/speed;
            speed+=f;
            //cout<<tme<< " "<<speed<<endl;
        }
        printf("Case #%d: %0.7lf\n",i,tme);
        //cout<<"Case #"<<i<<": "<<tme<<endl;
    }
    return 0;
}
