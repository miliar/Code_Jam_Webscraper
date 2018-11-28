#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <deque>
#include <cmath>
#include <set>
#include <map>
#define mod 1000000007LL
using namespace std;

set <long long> l;
set <long long>::iterator it;


set <long long> list;
long long unit[15];

void dfs(long long x,long long c,long long s)
{
    if(x>=11000000)
    return;
    it=l.find(x);
    if(it!=l.end())
    return;
    if(x)
    l.insert(x);
    
   
    for(int i=1;i<=9;i++)
    {
        dfs(x*10+i+unit[c+2],c+2,s);
    }
    
    if(s!=0)
        dfs(x*10+s,c+1,s);
    
}

bool gao(long long x)
{
    vector <int> L;
    while(x)
    {
        L.push_back(x%10);
        x/=10;
        
    }
    int i,j;
    i=0;
    j=L.size()-1;
    while(i<j)
    {
        if(L[i]!=L[j])
        return false;
        i++;
        j--;
    }
    return true;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i;
    unit[1]=1;
    for(i=2;i<15;i++)
        unit[i]=unit[i-1]*10;
    int re,cases=1;
    
    l.clear();
    list.clear();
    for(i=0;i<=9;i++)
    {
        dfs(i,1,i);
    }
    
    for(it=l.begin();it!=l.end();it++)
    {
        long long x=*it;
        x*=x;
        if(gao(x))
            list.insert(x);
    }
    
    cin>>re;
    while(re--)
    {
        long long L,R;
        cin>>L>>R;
        
        long long ans=0;
        for(it=list.begin();it!=list.end();it++)
        {
            long long x=*it;
            if(x>=L&&x<=R)
            {
               
                ans++;
            }
            
        }
        cout<<"Case #"<<cases++<<": "<<ans<<endl;        
        
    }
}
