#include <bits/stdc++.h>
using namespace std;

string get( char s1, char c1, char s2, char c2 )
{
        string r="";

        if( c1 == '1' )  {
                if(c2=='1') { r=(s1==s2?"+":"-"); r+='1' ; }
                if(c2=='i') { r=(s1==s2?"+":"-"); r+='i' ; }
                if(c2=='j') { r=(s1==s2?"+":"-"); r+='j' ; }
                if(c2=='k') { r=(s1==s2?"+":"-"); r+='k' ; }
        }

        if( c1 == 'i' )  {
                if(c2=='1') { r=(s1==s2?"+":"-"); r+='i' ; }
                if(c2=='i') { r=(s1!=s2?"+":"-"); r+='1' ; }
                if(c2=='j') { r=(s1==s2?"+":"-"); r+='k' ; }
                if(c2=='k') { r=(s1!=s2?"+":"-"); r+='j' ; }
        }

        if( c1 == 'j' )  {
                if(c2=='1') { r=(s1==s2?"+":"-"); r+='j' ; }
                if(c2=='i') { r=(s1!=s2?"+":"-"); r+='k' ; }
                if(c2=='j') { r=(s1!=s2?"+":"-"); r+='1' ; }
                if(c2=='k') { r=(s1==s2?"+":"-"); r+='i' ; }
        }

        if( c1 == 'k' )  {
                if(c2=='1') { r=(s1==s2?"+":"-"); r+='k' ; }
                if(c2=='i') { r=(s1==s2?"+":"-"); r+='j' ; }
                if(c2=='j') { r=(s1!=s2?"+":"-"); r+='i' ; }
                if(c2=='k') { r=(s1!=s2?"+":"-"); r+='1' ; }
        }

        return r;
}

bool solve()
{
        long long L,X,i,j;
        string inp,c="";

        cin >> L >> X >> inp ;

        for( i=0; i<X; i++ )
                c += inp;

        string s(c.size(),'+');

        vector<string> res(c.size());

        res[0] = string(1,s[0])+string(1,c[0]) ;

        for( i=1; i<c.size() ; i++ )
                res[i] = get( res[i-1][0], res[i-1][1], s[i], c[i] ) ;

        if( res.back()=="-1" )
                for( i=0; i<c.size()-2; i++ )
                        for( j=i+1; j<c.size()-1; j++ )
                                if( res[i]=="+i" && res[j]=="+k" )
                                        return 1;
        return 0;
}

int main()
{
        freopen("input","r",stdin);
        freopen("output","w",stdout);

        long long t=0,tt;

        for( cin>>tt; tt--; )
                printf( "Case #%lld: %s\n", ++t, solve()?"YES":"NO" ) ;

        return 0;
}
