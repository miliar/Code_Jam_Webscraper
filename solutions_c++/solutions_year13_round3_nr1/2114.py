/*
Original Author: El_Magnifico(Sudhanshu Shekhar)
*/

#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<string>
#include<cctype>
#include<sstream>
#include<cmath>
#include<list>
#include<climits>
#include<stack>
#include<map>
#include<bitset>
#include<queue>
#include<set>
#include<climits>
#include<cstring>
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
using namespace std;
typedef long long ll;
map<char,int>mp;

bool check(string s,ll x)
{
    int i,j,k,cnt;
    //cout<<"X="<<x<<endl;
    for(i=0;i<=s.length()-x;i++)
    {
        if(mp[s[i]])continue;
        for(j=i;j<i+x && j<s.length();j++)if(mp[s[j]])break;
        //cout<<"j="<<j<<endl;
        if(j-i>=x)return true;
    }
    return false;
}

int main()
{
    freopen("C:\\Users\\Psyduck\\Desktop\\A-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\Psyduck\\Desktop\\output.txt","w",stdout);
    ll i,j,k,n,m,t,cnt,saven;
    string s;
    mp['a']=1;mp['e']=1;mp['i']=1;mp['o']=1;mp['u']=1;
    //check("tra",3);
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>s>>n;
        saven=n;
        cnt=0;
        for(;n<=s.length();n++)
        {
            for(j=0;j<=s.length()-n;j++)
            {
                //cout<<s.substr(j,n)<<endl;
                if(check(s.substr(j,n),saven))
                {
                    //cout<<s.substr(j,n)<<endl;
                    cnt++;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<cnt<<endl;
    }
    return 0;
}
