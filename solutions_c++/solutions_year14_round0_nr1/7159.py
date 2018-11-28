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
    LL t,i,j,k,x,y,z,res,count,temp,in,f,s;
    cin>>t;
    for(in=1;in<=t;in++)
    {
        count=0;
        cin>>f;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>a[i][j];
            }
        }
        cin>>s;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>b[i][j];
                if(i==s-1)
                {
                    for(k=0;k<4;k++)
                    {
                        if(a[f-1][k]==b[i][j])
                        {
                            count++;
                            temp=a[f-1][k];
                        }
                    }
                }
            }
        }
        if(count==1)
        cout<<"Case #"<<in<<": "<<temp<<endl;
        else if(count>1)
        cout<<"Case #"<<in<<": "<<"Bad magician!"<<endl;
        else if(count==0)
        cout<<"Case #"<<in<<": "<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
