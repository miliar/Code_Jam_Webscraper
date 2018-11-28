#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int te[1000010];
int val[300];
void f()
{
    string s;
    int n,en=-1;
    long long sum=0;
    cin>>s;
    cin>>n;
    for(int i=0;i<s.length();i++)
    {
        if(val[s[i]])
        {
            te[i]=te[i-1]+1;
            if(i==0)
                te[i]=1;
        }
        else
            te[i]=0;
        if(te[i]>=n)
        {
            sum+=(s.length()-i)*(i-en-n+1);
            en=i-n+1;
        }
    }
    cout<<sum<<"\n";
}
int main()
{
    freopen("AT.in","r",stdin);
    freopen("AAAA.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=0;i<300;i++)
    {
        val[i]=1;
    }
    val['a']=0;
    val['e']=0;
    val['i']=0;
    val['o']=0;
    val['u']=0;
    for(int i=0;i<t;i++)
    {
        printf("Case #%d: ",i+1);
        f();
    }
}
