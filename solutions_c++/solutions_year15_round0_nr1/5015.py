#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

int main()
{
        freopen("input","r",stdin);
        freopen("output","w",stdout);

        ll tt,t,ans,sum,i;
        string s;

        cin>>tt;
        for( t=1; t<=tt; t++ )
        {
                cin >> sum >> s ;

                for( ans=sum=i=0; s[i]; i++ )
                {
                        if( sum < i && s[i]!='0' )
                        {
                                ans += (i-sum) ;
                                sum += (i-sum) ;
                        }
                        sum += s[i]-48 ;
                }

                printf( "Case #%lld: %lld\n", t, ans );
        }

        return 0;
}
