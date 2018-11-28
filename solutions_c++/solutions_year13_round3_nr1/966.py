
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

#define clr(name,val) memset(name,(val),sizeof(name));
#define Assign(name,val) name.assign(val+1,vector<int>())
#define EPS .000000001
#define ll long long
#define psb(b) push_back((b))
#define ppb() pop_back()
#define oo 10000000
#define mp make_pair
#define fs first
#define sc second
#define rep(var,s,n) for(var=(s);var<(n);(var)++)
#define rvp(var,s,n) for(var=(n-1);var>(s-1);(var)--)
#define read_ freopen("input.txt","r",stdin)
#define write_ freopen("output.txt","w",stdout)

using namespace std;

ll cal[1100000];
int val[300];
int main()
{
    read_;
    write_;
    for(int i='b';i<='z';i++)
    {
        if(i!='e'&&i!='i'&&i!='o'&&i!='u') val[i]=1;
    }
    ll test,len,n,cas=0L;
    string s;
    cin>>test;
    while(test--)
    {
        clr(cal,0L);
        cin>>s>>n;
        len=s.size();
        for(int i=1;i<=len;i++)
        {
            if(val[s[i-1]]) cal[i]=cal[i-1]+1;
            else cal[i]=cal[i-1];
        }
        ll res=0L,up=0L;
        bool flag=false;
        for(int i=1;i<=len;i++)
        {
//            cout<<cal[i]<<" ";
            if(i>=n&&(cal[i]-cal[i-n]==n)&&val[s[i-n]])
            {
                res+=(i-n)+1;
                up=i-n;
                flag=true;
            }
            else if(flag) res+=up+1;
        }
        printf("Case #%lld: %lld\n",++cas,res);
    }
    return 0;
}



















