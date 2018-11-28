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
    int t=0,a,b,i=0,j=0,n=0,m=0,k=0,l,num=0,temp=0,ans=0;
    cin>>t;
    string str;
    int arr[10000];
    vi v;
    for(i=0;i<t;++i)
    {
        cin>>a>>b>>m;
        ans=0;
        for(j=0;j<a;++j)
        {
            for(k=0;k<b;++k)
            {
                if((j&k)<m)
                    ans++;
            }
        }
        cout<<"Case #"<<i+1<<": ";
        cout<<ans;
        cout<<"\n";
    }
	return 0;
}
