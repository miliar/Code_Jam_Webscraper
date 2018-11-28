#include <iostream>
#include <fstream>
#include <math.h>
#include <sstream>
#include <string>

using namespace std;

bool isPali( double n );
string rev( string n );
string convert( double n );

int main ()
{
    ofstream out;
    out.open ("c.out");

    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        int c = 0;
        int a, b;
        cin >> a;
        cin >> b;
        
        for ( ; a <= b; ++a )
        {
            if ( isPali(a) && isPali(sqrt(a)))
                ++c;
        }
        
        
        out << "Case #" << t + 1 << ": " << c << endl;
    }
    
    return 0;
}

bool isPali( double n )
{
    string s = convert(n);
    int len = s.length();
    
    for (int x = 0; x < len/2; ++x)
        if (s[x] != s[len-x-1]) return false;
    
    return true;
}

string convert( double n )
{
    stringstream ss;
    ss << n;
    string s(ss.str());
    return s;
}