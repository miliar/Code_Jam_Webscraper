#include<bits/stdc++.h>
using namespace std;

int main()
{
    int tt, t, x, r, c, f;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        cin>>x>>r>>c;
        if( r > c )
            r=c+r-(c=r);

        if( x == 1 )
        {
            f=1;
        }
        else if( x == 2 )
        {
            if( r % x == 0 || c % x == 0 )
            {
                f=1;
            }
            else
            {
                f=0;
            }
        }
        else if( x == 3 )
        {
            if( r == 1 )
            {
                f=0;
            }
            else if( r == 2 )
            {
                if( c == 3 )
                {
                    f=1;
                }
                else
                {
                    f=0;
                }
            }
            else if( r == 3 )
            {
                f=1;
            }
            else
            {
                f=0;
            }
        }
        else
        {
            if( r < 3 )
            {
                f=0;
            }
            else if( r == 3 )
            {
                if( c == 3 )
                {
                    f=0;
                }
                else
                {
                    f=1;
                }
            }
            else
            {
                f=1;
            }
        }
        if(f==1)cout<<"Case #"<<tt<<": GABRIEL\n";
        else cout<<"Case #"<<tt<<": RICHARD\n";
    }
    return 0;
}
