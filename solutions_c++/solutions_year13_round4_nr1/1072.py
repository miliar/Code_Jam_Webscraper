#include "cstdio"
#include "cstring"
#include "iostream"
#include "algorithm"
#include "cmath"
#include "utility"
#include "cstdlib"
#include "vector"
#include "string"
#include "queue"
#include "stack"
#include "set"
#include "map"

using namespace std;

long long n;
map<long long,long long> sums;
set<long long> nodess;
vector<long long> nodes;

long long solve(int,int,long long);
long long cost(long long, long long);

int main(void)
{
    long long realcost;
    long long lowcost;
    int t;
    
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        int m;
        sums.clear();
        nodess.clear();
        nodes.clear();
        
        realcost=0LL;
        
        scanf("%lld%d",&n,&m);
        while(m--)
        {
            long long a,b,c;
            
            scanf("%lld%lld%lld",&a,&b,&c);
            if(nodess.find(a)==nodess.end())
            {
                nodess.insert(a);
                sums[a]=0LL;
            }
            
            if(nodess.find(b)==nodess.end())
            {
                nodess.insert(b);
                sums[b]=0LL;
            }
            
            sums[a]+=c;
            sums[b]-=c;
            
            realcost+=c*cost(a,b);
        }
        
        int i=0;
        for (std::set<long long>::iterator it=nodess.begin(); it!=nodess.end(); ++it)
        {
            nodes.push_back(*it);
            if(i>0)sums[nodes[i]]+=sums[nodes[i-1]];
            i++;
            
            //printf("- %d %lld %lld\n",i,nodes[i],sums[nodes[i]]);
        }
        
        lowcost=solve(0,nodes.size()-1,0);
        
        //printf("%lld %lld\n",realcost,lowcost);
        printf("Case #%d: %lld\n",test,realcost-lowcost);
    }
    
    return 0;
}

long long solve(int a,int b,long long buffs)
{
    if(a==b)return 0LL;
    long long ans=0;
    
    int start=a;
    long long minimum=1000000000000000LL;
    
    for(int i=a;i<b;i++)
    {
        minimum=min(sums[nodes[i]],minimum);
    }
    
    //printf(">> %d %d %lld\n",nodes[a],nodes[b],minimum-buffs);
    ans=(minimum-buffs)*cost(nodes[a],nodes[b]);
    buffs=minimum;
    
    for(int i=a;i<b;i++)
    {
        if(sums[nodes[i]]==buffs)
        {
            //printf(">>> %d %d\n",start,i);
            ans+=solve(start,i,buffs);
            start=i+1;
        }
    }
    
    ans+=solve(start,b,buffs);
    
    return ans;
}

long long cost(long long a, long long b)
{
    long long ans=1LL;
    b-=a;
    
    ans*=n+(n-b+1);
    ans*=b;
    ans/=2LL;
    
    return ans;
}