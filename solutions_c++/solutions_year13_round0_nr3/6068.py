#include<iostream>
#include<sstream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<queue>
#include<cstdio>
#include<map>

using namespace std;

bool check(string x,long long y)
{
    int n=x.size(),i;
    for(i=0;i<n;i++)
    if(x[i]!=x[n-i-1]){return 0;}

    if(sqrt(y)*sqrt(y)!=y){return 0;}

    long long ans=sqrt(y),p=sqrt(y),br=0,k=1;string s="";
    while(p)
    {
        p/=10;
        k*=10;
        br++;
    }
    while(ans)
    {
        s+=char(ans%10)+'0';
        ans/=10;
    }
    reverse(s.begin(),s.end());
    for(i=0;i<br;i++)
    if(s[i]!=s[br-i-1]){return 0;}

    return 1;
}

int main ()
{
    long long a,b,t,i,j,br=0;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>a>>b;
        for(j=a;j<=b;j++)
        {
            long long ans=j;string s="";
            while(ans)
            {
                s+=char(ans%10)+'0';
                ans/=10;
            }
            reverse(s.begin(),s.end());
            if(check(s,j))br++;
        }
        cout<<"Case #"<<i<<": "<<br<<endl;br=0;
    }
    return 0;
}
