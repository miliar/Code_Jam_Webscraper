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
    int t=0,i=0,j=0,n=0,m=0,k=0,ans1,ans2;
    cin>>t;
    string str;
    double naomi[1002],ken[1002];
    for(i=0;i<t;++i)
    {
        cin>>n;
        for(j=0;j<n;++j)
        {
            cin>>naomi[j];
        }
        for(j=0;j<n;++j)
        {
            cin>>ken[j];
        }
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        j=0;
        k=0;
        while(true)
        {
            while(k<n && ken[k]<naomi[j])
                ++k;
            if(k>=n)
                break;
            ++j;
            ++k;
            if(k>=n)
                break;
        }
        ans2=n-j;
        j=0;
        k=0;
        while(true)
        {
            while(j<n && ken[k]>naomi[j])
                ++j;
            if(j>=n)
                break;
            ++j;
            ++k;
            if(j>=n)
                break;
        }
        ans1=k;
        cout<<"Case #"<<i+1<<": "<<ans1<<" "<<ans2;
        cout<<endl;
    }
	return 0;
}
