#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<utility>
using namespace std;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define ll long long
#define MAX_SIZE 200005
#define MOD 1000000007
#define S(x) scanf("%d",&x)
#define SL(x) cin>>x
#define SC(x) scanf("%c",&x)
#define SS(x) scanf("%s",x)
#define SZ(x) x.size()
#define IT iterator
#define PI pair<int,int>
#define PL pair<ll,ll>
#define VI vector<int>
#define VL vector<ll>
#define VVI vector< VI >
#define VVL vector< VL >
#define VVP vector< PI >
#define READ() freopen("/Users/home/Desktop/input.txt","r",stdin)
#define WRITE() freopen("/Users/home/Desktop/output.txt","w",stdout)
#define dump() SC(dump_char)
int dump_char;

int main()
{
    READ();
    WRITE();
    
    int t;
    double c,f,x;
    S(t);
    
    for(int k=1;k<=t;k++)
    {
        SL(c);
        SL(f);
        SL(x);
        
        double ans=0,rate=2,t1,t2;
        while(1)
        {
            t1=x/rate;
            t2=c/rate+x/(rate+f);
            if(t2<t1)
            {
                ans+=c/rate;
                rate+=f;
            }
            else
            {
                ans+=x/rate;
                break;
            }
        }
        
        printf("Case #%d: %.7lf\n",k,ans);
    }
    return 0;
}