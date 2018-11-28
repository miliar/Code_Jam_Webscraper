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
    long long int t,cases=0,a,ans,n,i,f,s,temp;
    while(cin>>t)
    {
        while(t--)
        {
            f=0;
            vector <long long int> arr;
            s=0;
            cin>>a>>n;
            ans=n;
            REPI(i,0,n-1)
            {
                scanf("%lld",&temp);
                arr.pb(temp);
            }
            if(a==1)
            {
                printf("Case #%lld: %lld\n",++cases,n);
                continue;
            }
            sort(arr.begin(),arr.end());
            REPI(i,0,n-1)
            {
                //cout<<a<<endl;
                if(arr[i]<a)
                a+=arr[i];
                else
                {
                    while(arr[i]>=a)
                    {
                        f=1;
                        ++s;
                        a+=(a-1);
                    }
                }
                ans=s+n-1-i>ans?ans:(s+n-1-i);
                if(f)
                --i;
                f=0;
            }
            printf("Case #%lld: %lld\n",++cases,ans);
        }
    }
    return 0;
}
                    
                
            
            
