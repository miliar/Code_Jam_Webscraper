#include<iostream>
using namespace std;

long long pow( long long a, long long b )
{
    for( int i = 0; i < b; i++ )
        a*=a;
    return a;
}

int main()
{
    long long i, j, k, t, c, s, tt, ii;
    cin>>t;
    for(tt=1; tt<=t; tt++)
    {
        cin>>k>>c>>s;

        if( s < k && c == 1 )
            { cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<endl; continue; }
        if( s >= k )
        {
            cout<<"Case #"<<tt<<":";
            for( i=1; i<=k; i++ )
                cout<<" "<<i;
            cout<<endl;
            continue;
        }

        if( s < k )
        {
            ii = pow( k, c-1 );
            cout<<"Case #"<<tt<<":";
            for( i=2, j=0; j < k/2; j++, i+= ii + 2 )
                cout<<" "<<i;
            if( k%2 == 1 ) cout<<" "<< i - ii - 1;
            cout<<endl;
        }

     ///   cout<<"Case #"<<tt<<": "<</**/<<endl;
    }
}
