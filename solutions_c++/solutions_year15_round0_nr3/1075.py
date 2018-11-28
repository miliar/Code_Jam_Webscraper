// AUTHOR : SIKANDER MAHAN
// sikander_nsit
// PLAGIARISM IS BAD

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <limits>
#include <string.h>

#define tr(type,c,it) for(type::iterator it=c.begin();it!=c.end();++it)
#define all(c) c.begin(),c.end()
#define mod 1000000007
#define itor(c) c::iterator
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
#define F first
#define S second

using namespace std;

map<char,int> mci;

int table[4][4]={{0,1,2,3},{1,4,3,6},{2,7,4,1},{3,2,5,4}};

int main()
{
    //ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t=0,i=0,j=0,n=0,m=0,k=0,num=0,temp=0,ind=0,sign;
    ll x;
    mci['1']=0;
    mci['i']=1;
    mci['j']=2;
    mci['k']=3;
    cin>>t;
    string str,s;
    for(i=0;i<t;++i)
    {
        cin>>n>>x;
        cin>>s;
        str.clear();
        cout<<"Case #"<<i+1<<": ";
        if(x>15)
        {
            x=12+(x%4);
        }
        k=x;
        for(j=0;j<k;++j)
        {
            str+=s;
        }
        n*=k;
        temp=0;
        sign=0;
        for(j=0;j<n;++j)
        {
            temp=table[temp][mci[str[j]]];
            if(temp>3)
            {
                temp-=4;
                sign=1-sign;
            }
            if(temp==1 && sign==0)
            {
                break;
            }
        }
        if(j==n)
        {
            cout<<"NO\n";
            continue;
        }
        ++j;
        temp=0;
        sign=0;
        for(;j<n;++j)
        {
            temp=table[temp][mci[str[j]]];
            if(temp>3)
            {
                temp-=4;
                sign=1-sign;
            }
            if(temp==2 && sign==0)
            {
                break;
            }
        }
        if(j==n)
        {
            cout<<"NO\n";
            continue;
        }
        ++j;
        temp=0;
        sign=0;
        for(;j<n;++j)
        {
            temp=table[temp][mci[str[j]]];
            if(temp>3)
            {
                temp-=4;
                sign=1-sign;
            }
        }
        if(temp==3 && sign==0)
        {
            cout<<"YES\n";
        }
        else
        {
            cout<<"NO\n";
        }
    }
    return 0;
}
