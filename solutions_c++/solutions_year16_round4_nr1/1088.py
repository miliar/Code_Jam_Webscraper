#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define N 100010
#define LN 17
#define mod (int)(1e9+7)


string memo ( string str , int l, int r )
{
    if( r-l==0 )
        return str.substr(l,1);
    string x = memo( str,l,(l+r)/2);
    string y= memo( str,(l+r)/2+1,r );

    //cout << x << " " << y << endl ;
    if( x+y < y+x )
        return x+y;
    return y+x;
}

string solve( int R,int P,int S,char x,int rounds )
{
    string ans ="",newans="";
    if( x=='R' )
        ans="RS";
    else if( x=='S' )
        ans="PS";
    else
        ans="PR";

    int counter=1;

    while( counter<rounds )
    {
        counter++;
        newans="";

        int n = ans.length();

        for( int i=0 ; i < n ; i++ )
        {
            if( ans[i]=='R' )
                newans = newans + "RS";
            else if( ans[i]=='S' )
                newans = newans + "PS";
            else
                newans = newans + "PR";
        }
        ans=newans;
    }

    int r,p,s;
    r=p=s=0;

    for( int i=0 ; i<ans.length() ; i++ )
    {
        if( ans[i]=='R' ) r++;
        else if( ans[i]=='S' ) s++;
        else p++;
    }

    //cout << r << " " <<s << " " <<p <<" "<<ans << endl;
    if( r!=R || s!=S || p!=P )
        return "";
    return memo( ans , 0,ans.length()-1);
}



int main()
{
    freopen("inp.txt","r",stdin);
    freopen("op.txt","w",stdout);

    int T;
    scanf("%d",&T);

    for( int cases=1; cases <= T; cases++ )
    {
        printf("Case #%d: ",cases);
        int R,P,S,n;
        scanf("%d %d %d %d",&n,&R,&P,&S);

        int x = (R+P+S);
        int numberofrounds=0;

        while( x>1 )
        {
            x/=2;
            numberofrounds++;
        }

        string x1=solve(R,P,S,'R',numberofrounds);
        string x2=solve(R,P,S,'P',numberofrounds);
        string x3=solve(R,P,S,'S',numberofrounds);

        vector < string > arr;
        if( x1.length() ) arr.push_back(x1);
        if( x2.length() ) arr.push_back(x2);
        if( x3.length() ) arr.push_back(x3);

        string ans ="";

        for( int i=0; i<arr.size() ; i++ )
        {
            if( ans=="" || ans<arr[i])
                ans=arr[i];
        }
        if( ans.length()==0 ) puts("IMPOSSIBLE");
        else cout << ans << endl;
    }
	return 0;
}


