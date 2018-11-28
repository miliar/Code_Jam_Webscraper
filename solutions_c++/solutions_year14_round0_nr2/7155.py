/*
written by- Dheeraj Kumar Barnwal
Algo by- Vaibhaw & Ankit
language- c++
country- India
College- N.I.T Jamshedpur
*/
#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include<cstdio>
#include<sstream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<map>
#include<set>
#include<queue>
#include<cctype>
#include<list>
using namespace std;
#define pb push_back
#define all(s) s.begin(),s.end()
#define f(i,a,b) for(i=a;i<b;i++)
#define F(i,a,b) for(i=a;i>=b;i--)
#define PI 3.1415926535897932384626433832795
#define INF 2000000000
#define BIG_INF 7000000000000000000LL
#define mp make_pair
#define eps 1e-9
#define mod 1000000007


typedef long long LL;

string inttostring(int n)
{
stringstream a;
a<<n;
return a.str();
}

int stringtoint(string A)
{
istringstream a(A);
int p;
a>>p;
return p;
}

int gcd(int a,int b)
{
return b==0?a:gcd(b,a%b);
}

LL power(LL aa, LL n, LL MOD) {
LL x = 1, y = aa;
    while(n > 0) {
        if(n%2 == 1) {
            x=(x*y);
            if(x>MOD) x%=MOD;
        }
        y = (y*y);
        if(y>MOD) y%=MOD;
        n /= 2;
    }
    return x;
}

LL a[5][5],b[5][5],dp[100005];
int main()
{
    LL t,i,j,k,in,fl;
    double c,f,x,count,res,t1,t2,y,z,d,comp1,comp2;
    cin>>t;
    for(in=1;in<=t;in++)
    {
        cin>>c>>f>>x;
        d=2.0;
        fl=1;
        comp1=0,comp2=0;res=0;
        while(fl)
        {
        t1=(c/d)+(x/(d+f));
        t2=x/d;
        comp1=res+t1;
        comp2=res+t2;
        if(comp1<comp2)
        {
            res+=c/d;
            d+=f;
            fl=1;
        }
        else
        {
            fl=0;
        }
        }
        res+=t2;
        //cout<<"Case #"<<in<<": "<<res<<endl;
        printf("Case #%lld: %0.7lf\n",in,res);
    }
    return 0;
}
