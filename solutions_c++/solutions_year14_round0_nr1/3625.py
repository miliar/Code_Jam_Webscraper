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
int main()
{
    ios::sync_with_stdio ( false );
    int t,i,j,k,m,n,x,y;
      freopen("A-small-attempt0.in","r",stdin);

    freopen("A-small.txt","w",stdout);
    cin>>t;
    rep(T,1,t)
    {
        int a1[4][4],a2[4][4],ans1,ans2,r1=-1,r2=-1;
        vi p1,p2;
        cin>>r1;
        fori ( 0,3 )
        {
            forj ( 0,3 )
            {
                cin>>a1[i][j];
                if ( i==r1 -1)
                {
                    p1.pb ( a1[i][j] );
                }
            }
        }
        cin>>r2;
        fori ( 0,3 )
        {
            forj ( 0,3 )
            {
                cin>>a2[i][j];
                if ( i==r2 -1)
                {
                    p2.pb ( a2[i][j] );
                }
            }
        }
        int match=0,card=-1;
        fori(0,3)
        {
            forj(0,3)
            if(p1[i]==p2[j]) {card=p1[i]; match++;}
        }
         cout<<"Case #"<<T <<": ";
        if (match==0)
        {
            cout<<"Volunteer cheated!\n";
        }
        else if (match==1)
        {
            cout<<card<<endl;
        }
        else
        {
            cout<<"Bad magician!\n";
        }
    }
    return 0;
}

