#include <iostream>
#include <cstring>
#include <queue>
#include <stdio.h>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <set>
#include <cstdlib>
#include <vector>
#include <cctype>
#include <utility>
#include <map>
#include <string>
using namespace std;

int conversion(string p){ int o; o=atoi(p.c_str()); return o; }
string toString(int h){ stringstream ss; ss<<h; return ss.str(); }
long long gcd(long long a,long long b) {return (b==0 ? a : gcd(b,a%b));}
int lcm(int a,int b) {return (a*(b/gcd(a,b))); }

int main()
{
    ios::sync_with_stdio(1);

    #ifndef ONLINE_JUDGE
    freopen("D:/input.txt","r",stdin);
    freopen("D:/output.txt","w",stdout);
    #endif

    int T,cas=1;
    cin>>T;
    while(T--)
    {
        cout<<"Case #"<<cas<<": ";
        vector<double> R;
        int a=0;
        double c,f,x,cos=2.0,res=0;
        cin>>c>>f>>x;
        R.push_back(x/cos);
        for(int i=0;i<=1000000;i++)
        {
            res+=c/cos;
            cos+=f;
            //if(x<=cos) break;
            double pon=res+x/cos;
            R.push_back(pon);
        }
        sort(R.begin(),R.end());
        if(cas==100) printf("%.7f",R[0]);
        else printf("%.7f\n",R[0]);
        cas++;
    }
}
