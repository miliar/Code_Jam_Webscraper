/*
Try Try & Try until you solve the problem...
Nothing is impossible for the problem solvers... :)
*/
/*

*/
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <numeric>

#include <cmath>
#include <cstdio>

#define IP(n) for(i=0;i<n;i++)
#define JP(n) for(j=0;j<n;j++)
#define KP(n) for(k=0;k<n;k++)

#define vi vector<int>
#define vi2 vector<vector<int>>
#define vs vector<string>

#define pb push_back
#define TC int t,check=1;cin>>t;while(check<=t)
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)
#define ms(x,a) memset(x,a,sizeof(x))
#define read(a) freopen(a,"r",stdin)
#define write(a) freopen(a,"w",stdout)

using namespace std;

long long A[50];

long long x[]={0,1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000001};

int isPal(long long x)
{
    if(!x) return 1;

    string s="",s1="";

    while(x>0)
    {
        s+=(x%10+'0');
        x/=10;
    }

    s1=s;
    reverse(s.begin(),s.end());

    return s==s1;
}

void gen()
{
    int ct=0;
    for(int i=0;i<10000005;i++)
    {
        long long x=i;
        x*=x;
        if(isPal(i) && isPal(x))
        {
            A[ct++]=x;
            cout<<i<<",";
        }
    }

    cout<<ct<<endl;
}

void gen2()
{
    for(int i=0;i<41;i++)
    A[i]=x[i]*x[i];
}

int main()
{
    read("Cl.in");
    write("Cl.txt");
    gen2();
    int t,check=1;
    scanf("%d",&t);
    long long a,b;
    while(t--)
    {
        cin>>a>>b;
        int ans=upper_bound(A,A+41,b)-lower_bound(A,A+41,a);
        printf("Case #%d: %d\n",check++,ans);
    }

    return 0;
}
