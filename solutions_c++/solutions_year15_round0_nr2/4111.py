#include<bits/stdc++.h>
using namespace std;
int solve(map<int,int> &mp,int sp)
{
    int i,n,cnt,m1;
    if(mp.size()==1 && mp.find(1)!=mp.end())
        return sp+1;
    map<int,int>::iterator it;
    it=mp.end();
    it--;
    n=it->first;
    m1=sp+n;
    cnt=it->second;
    for(i=2;i<=n;i++)
    {
        map<int,int> x;
        map<int,int>::iterator x1,x2;
        x1=mp.begin();
        x2=mp.end();
        x2--;
        while(x1!=x2)
        {
            x[x1->first]=x1->second;
            x1++;
        }
        if(i>n/2)
        {
            if(n-i)
                x[2]+=n-i;
            x[1]+=2*i-n;
        }
        else
        {
            if(n%i==0)
                x[n/i]+=cnt*i;
            else
            {
                x[n/i]+=cnt*(i-(n%i));
                x[n/i+1]+=cnt*(n%i);
            }
        }
        m1=min(m1,solve(x,sp+((i-1)*cnt)) );
    }
    return m1;
}
int main()
{
    int i,j,t,n,k;
    freopen("B-small-attempt3.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>t;
    int cases=1;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        map<int,int> mp;
        for(j=0;j<n;j++)
        {
            cin>>k;
            mp[k]++;
        }
        cout<<"Case #"<<i<<": "<<solve(mp,0)<<endl;
    }
}
