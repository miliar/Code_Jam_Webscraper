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
    int t=0,a,i=0,j=0,n=0,m=0,k=0,l,num=0,temp=0,ans=0;
    cin>>t;
    string str[102];
    int arr[10000];
    string s[102];
    vi cnt[102];
    vi v;
    for(i=0;i<t;++i)
    {
        cin>>n;
        ans=0;
        for(j=0;j<n;++j)
        {
            cin>>str[j];
            s[j].clear();
            cnt[j].clear();
            s[j].pb(str[j][0]);
            num=1;
            for(k=1;k<str[j].length();++k)
            {
                if(str[j][k]!=str[j][k-1])
                {
                    cnt[j].pb(num);
                    num=1;
                    s[j].pb(str[j][k]);
                }
                else
                    ++num;
            }
            cnt[j].pb(num);
        }
        for(j=1;j<n;++j)
        {
            if(s[j]!=s[0])
                break;
        }
        cout<<"Case #"<<i+1<<": ";
        if(j<n)
        {
            cout<<"Fegla Won";
        }
        else
        {
            m=s[0].length();
            for(a=0;a<m;++a)
            {
                v.clear();
                for(k=0;k<n;++k)
                {
                    v.pb(cnt[k][a]);
                }
                sort(all(v));
                num=v[n/2];
                for(k=0;k<n;++k)
                {
                    ans+=abs(num-v[k]);
                }
            }
            cout<<ans;
        }
        cout<<"\n";
    }
	return 0;
}
