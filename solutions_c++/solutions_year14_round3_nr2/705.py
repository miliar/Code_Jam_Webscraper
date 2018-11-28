// AUTHOR : SIKANDER MAHAN
// sikander_nsit
// PLAGIARISM IS BAD

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<string.h>
#define tr(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define all(c) c.begin(),c.end()
#define mod 1000000007
#define itor(c) typeof(c.begin())
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define si set<int>
#define msi multiset<int>
#define ii pair<int,int>
#define sii set<ii>
#define vii vector<ii>
#define vvi vector<vi>
#define pb push_back
#define mp make_pair

using namespace std;

int main()
{
    //ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t=0,i=0,j=0,a,b,n=0,m,k=0,num=0,temp=0,sz;
    bool flag;
    int c1,cb,cm,ce,cnt;
    int inde,indb,indm;
    ll ans=0;
    string str[101],s,newstr;
    char ch;
    vector<string> v,v1;
    ll fact[110]={0};
    fact[0]=1;
    for(i=1;i<=101;++i)
    {
        fact[i]=(fact[i-1]*i)%mod;
    }
    cin>>t;
    for(i=0;i<t;++i)
    {
        cin>>n;
        ans=1;
        v.clear();
        flag=false;
        cout<<"Case #"<<i+1<<": ";
        for(j=0;j<n;++j)
        {
            cin>>s;
            str[j].clear();
            str[j].pb(s[0]);
            for(k=1;k<s.length();++k)
            {
                if(s[k]!=s[k-1])
                    str[j].pb(s[k]);
            }
            v.pb(str[j]);
        }
        ch='a';
        while(ch<='z')
        {
            v1.clear();
            s.clear();
            s.pb(ch);
            sz=v.size();
            c1=0;cb=0;cm=0;ce=0;cnt=0;
            for(j=0;j<sz;++j)
            {
                cnt=0;
                if(v[j]==s)
                {
                    c1++;
                }
                else
                {
                    for(k=0;k<v[j].length();++k)
                    {
                        if(v[j][k]==ch)
                        {
                            cnt++;
                        }
                    }
                    if(cnt==1)
                    {
                        if(v[j][0]==ch)
                        {
                            indb=j;
                            cb++;
                        }
                        else if(v[j][k-1]==ch)
                        {
                            inde=j;
                            ce++;
                        }
                        else
                        {
                            indm=j;
                            cm++;
                        }
                    }
                    else if(cnt>1)
                    {
                        flag=true;
                        break;
                    }
                    else
                    {
                        v1.pb(v[j]);
                    }
                }
            }
            if(flag)
                break;
            newstr.clear();
            if(c1>0)
            {
                if(cm>0 || ce>1 || cb>1)
                {
                    flag=true;
                    break;
                }
                if(ce==1)
                {
                    newstr.append(v[inde]);
                }
                newstr.append(s);
                if(cb==1)
                {
                    newstr.append(v[indb]);
                }
                v1.pb(newstr);
                ans=(ans*fact[c1])%mod;
            }
            else if(ce>0 || cb>0 || cm>0)
            {
                if((ce==1 || cb==1) && cm==0)
                {
                    if(ce==1)
                    {
                        newstr.append(v[inde]);
                    }
                    if(cb==1)
                    {
                        newstr.append(v[indb]);
                    }
                }
                else if(cm==1 && ce==0 && cb==0)
                {
                    newstr.append(v[indm]);
                }
                else
                {
                    flag=true;
                    break;
                }
                v1.pb(newstr);
            }
            v=v1;
            ch++;
        }
        if(flag)
        {
            cout<<"0";
        }
        else
        {
            sz=v.size();
            ans=(ans*fact[sz])%mod;
            cout<<ans;
        }
        cout<<"\n";
    }
    return 0;
}
