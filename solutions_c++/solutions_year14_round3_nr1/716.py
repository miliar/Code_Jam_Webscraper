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

ll gcd(ll a,ll b)
{
    if(b==0)
        return a;
    return gcd(b,a%b);
}

int main()
{
    //ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t=0,i=0,j=0,a,b,n=0,m,k=0,num=0,temp=0,ans;
    ll p,q;
    vector<ll> v;
    char ch;
    temp=1;
    v.pb(temp);
    cin>>t;
    for(i=1;i<=40;++i)
    {
        temp*=2;
        v.pb(temp);
    }
    for(i=0;i<t;++i)
    {
        cin>>p>>ch>>q;
        cout<<"Case #"<<i+1<<": ";
        num=gcd(p,q);
        p/=num;
        q/=num;
        temp=q;
        while(temp%2==0)
        {
            temp/=2;
        }
        if(temp!=1)
        {
            cout<<"impossible";
        }
        else
        {
            j=upper_bound(all(v),p)-v.begin()-1;
            q/=v[j];
            j=lower_bound(all(v),q)-v.begin();
            cout<<j;
        }
        cout<<"\n";
    }
    return 0;
}
