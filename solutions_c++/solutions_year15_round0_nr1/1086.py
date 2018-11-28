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

int main()
{
    //ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t=0,i=0,j=0,n=0,m=0,k=0,num=0,temp=0,ind=0;
    cin>>t;
    string str;
    for(i=0;i<t;++i)
    {
        cin>>n>>str;
        num=0;
        cout<<"Case #"<<i+1<<": ";
        k=str[0]-48;
        for(j=1;j<=n;++j)
        {
            if(j>k)
            {
                num+=j-k;
                k=j;
            }
            k+=str[j]-48;
        }
        cout<<num;
        cout<<"\n";
    }
    return 0;
}
