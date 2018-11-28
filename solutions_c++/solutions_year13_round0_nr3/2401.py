//Author: prakash.mishra005
#include<cstdio>
#include<vector>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<queue>
#include<set>
#include<stack>
#include<map>
#include<sstream>
#include<bitset>
#include<deque>
#include<utility>
#include<cstdlib>
#include<iomanip>
#include<cctype>
#include<climits>
#include<iostream>
using namespace std;
#define ll             long long
#define ull            unsigned long long
string tostr(long long x) { stringstream ss; ss << x; return ss.str(); }
long long toint(const string &s) { stringstream ss; ss << s; long long x; ss >> x; return x; }

int main()
{
freopen("C-large-1.in","r",stdin);
freopen("output.txt","w",stdout);
ull x[]={  0,1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001};
int test;
cin>>test;
int i,j,k;
for(i=1;i<=test;i++)
{
    ull a,b;
    cin>>a>>b;
    j=0;
    int cnt=0;
    while(1)
    {
        if(x[j]>=a&&x[j]<=b)
        {
            cnt++;j++;
        }
        else if(x[j]<a)
        j++;
        else if(x[j]>b)
        break;
    }
    cout<<"Case #"<<i<<": "<<cnt<<endl;
}
return 0;
}
