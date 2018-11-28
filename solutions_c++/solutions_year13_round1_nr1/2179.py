/*
unsolved
prob 378
algo line intersection
*/
#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include <cstdlib>
#include<climits>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <list>
#include <map>
#include <set>

using namespace std;

#define IOR(x) freopen(x,"r",stdin);
#define IOW(x) freopen(x,"w",stdout);
#define DEBUG if(1)

#define i64 long long
#define u64 unsigned long long
#define eps 1e-10

#define REPI(i,a,b) for(i=a;i<=b;++i)
#define REPD(i,a,b) for(i=a;i>=b;--i)

#define pb(p) push_back(p)
#define ms(p,v) memset(p,v,sizeof(p))
#define pii pair< int, int >
#define mp(a,b) make_pair(a,b)
#define clr(a) a.clear();
#define ff first
#define sd second

int main()
{
    DEBUG IOR("i.txt");
    DEBUG IOW("o.txt");
    long long int r,t,cases,k,n,t1,t2;
    //double pi=3.1415926535897932384626433832795;
    while(cin>>cases)
    {
        k=0;
        while(cases--)
        {
            scanf("%lld%lld",&r,&t);
            t1=(4*r*(r-1))+1+8*t;
            n=((-1*(2*r+3))+sqrt(t1))/4;
            //cout<<t1<<" "<<n<<endl;
            printf("Case #%lld: %lld\n",++k,(n+1));
        }
    }
    return 0;
}
        
