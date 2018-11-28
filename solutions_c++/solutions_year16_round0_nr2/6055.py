#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define N 123456

int solve( string str, int idx,char cur )
{
    if( idx<0 )
        return 0;
    if( str[idx]==cur )
        return solve(str,idx-1,cur);
    else if( cur=='+')
        return 1+solve(str,idx-1,'-');
    return 1+solve(str,idx-1,'+');
}

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("op.txt","w",stdout);

    int t;
    scanf("%d",&t);

    for( int tt=1 ; tt<=t ; tt++ )
    {
        string str;
        cin >> str;

        int n = str.length(),ans=0;
        printf("Case #%d: %d\n",tt,solve(str,n-1,'+'));
    }

    return 0;
}

