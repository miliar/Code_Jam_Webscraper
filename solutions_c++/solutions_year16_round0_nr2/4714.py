#include<string>
#include<iostream>
using namespace std;

string s;

int flip( int from, char side )
{
    while( s[from] == side && from>=0 )
        from--;
    if( from == -1 ) return 0;
    while( s[from] != side && from>=0 )
        from--;
    if( side == '+' ) side = '-';
        else side = '+';

    if( from == -1 ) return 1;
        else return 1 + flip( from, side );
}

int main()
{
    int i, j, k, t, c;
    cin>>t;
    for(c=1; c<=t; c++)
    {
        cin>>s;
        cout<<"Case #"<<c<<": "<<flip( s.length()-1, '+' )<<endl;
    }
}
