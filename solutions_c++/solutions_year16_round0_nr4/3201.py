#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string.h>
#include<climits>
#include<vector>
#include<stack>
#include<set>
#include<math.h>
using namespace std;
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define sint(i) scanf("%d",&i)
#define ss(s) scanf("%s",s)
#define pii pair<int,int>
#define mp(i,j) make_pair(i,j)
#define ll long long
#define MAX 1000000000
#define MOD 1000000007
#define vi vector<int>
#define vvi vector < vi >
#define pb(i) push_back(i);
#define tr(v,it) for(it=v.begin();it!=v.end();it++)
int main()
{
    freopen("test.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int i;
    int t;
    cin>>t;
    int test;
    FOR(test,1,t)
    {
        int s,c,k;
        cin>>k>>c>>s;
        cout<<"Case #"<<test<<": ";
        FOR(i,1,s)
        {
            cout<<i<<" ";
        }
        cout<<"\n";
    }
    return 0;
}
