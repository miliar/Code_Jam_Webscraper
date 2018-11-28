#include <iostream>
#include <sstream>
#include <gmpxx.h>
#include <gmp.h>
#include <algorithm>
#include <fstream>

using namespace std;

bool palindrome( mpz_class v, mpz_class b )
{
    stringstream sstr;
    string str, str1;
    bool pal=false;
    mpz_class t=v;

    sstr<<v;
    sstr>>str;
    sstr.clear();

    str1=str;
    reverse( str.begin(), str.end() );

    if( str == str1 )
        pal++;


    if( pal )
    {
        sstr<<str1;
        sstr>>v;
        sstr.clear();

        v=sqrt(v);

        if( v*v==t )
        {
            sstr<<v;
            sstr>>str;
            sstr.clear();

            str1=str;
            reverse( str.begin(), str.end());

            if( str != str1 /*|| v>b*/ )
                pal=false;
        }
        else
            pal=false;
    }

    return pal;
}

int main()
{
    mpz_class a, b, c, g, t, d;
    ifstream in("C.in");
    ofstream out("C.out");

    in>>t;
    for( d=0; d<t; d++ )
    {
        g=0;
        in>>a>>b;
        for( c=a; c<=b; c++ )
        {
            if( palindrome(c, b) )
               g++;
        }

        out<<"Case #"<<d+1<<": "<<g<<'\n';
    }
    return 0;
}
