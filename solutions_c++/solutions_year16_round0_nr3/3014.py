typedef long long ll;
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <utility>

using namespace std;
ll maxi=10000000;
ll mark[20],fac[10000007],flag[10000007];
vector<ll> v,primes;
ll convert(string s,ll n)
{
    ll num=1,k=1,i;
    for(i=s.length()-1;i>=0;i--)
    {
        if(s[i]=='1')
        num+=pow(n,k);
        k++;
    }
    //num+=pow(n,k);
    return num;
}
ll check(ll n)
{ 
if(n<=maxi)
return (flag[n]==1?1:fac[n]);
for(ll i=0;i<primes.size();i++)
{
    if (n%primes[i]==0)
    return primes[i];
}
return 1; 
}
int main()
{
    ll t,i,j,res,w=1,n,m,g,flag1,val;
    string s1,s;
    for(i=0;i<=maxi;i++)
    {
        flag[i]=1;
        fac[i]=-1;
    }
    for(i=2;i<=maxi;i++)
    {
        if(flag[i]==1)
        {
            fac[i]=i;
            for(j=2*i;j<=maxi;j+=i)
            {
                if(fac[j]==-1)
                fac[j]=i;
                flag[j]=0;
            }
            primes.push_back(i);
        }
    }
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld %lld",&n,&m);
        cout<<"Case #"<<w++<<" :"<<endl;
        g=0;
        for(i=0;i<(1<<n-2);i++)
        {
            s="";
            if(g==m)
            break;
            for(j=0;j<n-2;j++)
            {
                if(i&(1<<j))
                {
                    s='1'+s;
                }
                else
                s='0'+s;
            }    
            flag1=0;
            v.clear();
            for(j=2;j<=10;j++)
            {
                
                res=convert(s,j)+pow(j,n-1);
                val=check(res);
                if(val==1)
                {
                    flag1=1;
                    break;
                }
               // cout<<res<<" "<<s<<endl;
               //cout<<i<<j<<" "<<res<<" "<<fac[res]<<endl;
                v.push_back(val);
            }
          
            if(flag1==1)
            v.clear();
            else
            {
            g++;
            s='1'+s+'1';
            cout<<s;
            for(j=0;j<9;j++)
            cout<<" "<<v[j];
            cout<<endl;
            }
        }
        
       
        
    }
	return 0;
}