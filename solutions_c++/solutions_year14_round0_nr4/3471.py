/* @author Ishita Gupta*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define vi vector<int>
#define vvi vector< vi >
#define vs vector<string>
#define rep(i,s,e) for(int i=s;i<=e;i++)
#define fori(s,e) for(int i=s;i<=e;i++)
#define forj(s,e) for(int j=s;j<=e;j++)
#define fork(s,e) for(k=s;k<=e;k++)
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define ull unsigned long long
#define ll long long
#define imax INT_MAX
#define imin INT_MIN
#define mem(x,y) memset(x,y,sizeof(x));
#define pii pair<int,int>
#define aa first
#define bb second
using namespace std;
int readint()
{
    int t=0;
    char c,ch;
    ch=getchar();
    if ( ch=='-' )
    {
        c=getchar();
    }
    else
    {
        c=ch;
    }
    while ( c<'0' || c>'9' )
    {
        c=getchar();
    }
    while ( c>='0' && c<='9' )
    {
        t= ( t<<3 )+ ( t<<1 )+c-'0';
        c=getchar();
    }
    if ( ch=='-' )
    {
        return -t;
    }
    else
    {
        return t;
    }
}
double naomi[1002],ken[1002];
int main()
{
    ios::sync_with_stdio ( false );
    int t,i,j,k,m,n,x=0,y;
    freopen ( "D-large.in","r",stdin );
    freopen ( "D-largeout.txt","w",stdout );
    cin>>t;
    rep ( T,1,t )
    {
        cin>>n;
        fori ( 0,n-1 ) cin>>naomi[i];
        fori ( 0,n-1 ) cin>>ken[i];
        sort ( naomi,naomi+n );
        sort ( ken,ken+n );
        cout<<"Case #"<<T <<": ";
//        fori ( 0,n-1 ) cout<<naomi[i]<<" ";
//        cout<<endl;
//        fori ( 0,n-1 ) cout<<ken[i]<<" ";
//        cout<<endl;
        int war=0,decwar=0;
        i=0,j=0;
        while ( j<n )
        {
            if ( naomi[i]<ken[j] )
            {
                i++;
            }
            j++;
        }
        war=n-i;
        i=n-1;
        j=n-1;
        while ( j>=0 )
        {
            if ( naomi[i]>ken[j] )
            {
                decwar++;
                i--;
            }
            j--;
        }
        cout<<decwar<<" "<<war<<endl;
    }
    return 0;
}

