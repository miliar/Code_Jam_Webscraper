#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

vector<string> vec;

bool compx( int x, int y, bool t )
{
    bool wx=false, cn=false;
    int c, g;
    size_t found;

    if(t)
        vec[y][x]='X';

    for( c=0; c<4 && !wx ; c++ )
    {
        found=vec[c].find("XXXX");

        if( found!=string::npos )
        {
            wx++;
        }
    }

    for( c=0; c<4 && !wx ; c++ )
    {
        cn=false;
        for( g=0; g<4 && !wx && !cn ; g++ )
        {
            if( vec[g][c]!='X' )
                cn++;
        }

        if( !cn )
            wx++;
    }

    cn=false;
    for( c=0; c<4 && !cn && !wx ; c++ )
    {
        if( vec[c][c]!='X' )
            cn++;
    }

    if( !cn )
        wx++;

    cn=false;
    for( c=0; c<4 && !cn && !wx ; c++ )
    {
        if( vec[c][3-c]!='X' )
            cn++;
    }

     if( !cn )
        wx++;

    return wx;
}

bool compy( int x, int y, bool t )
{
    bool wo=false, cn=false;
    int c, g;
    size_t found;

    if(t)
        vec[y][x]='O';

    for( c=0; c<4 && !wo ; c++ )
    {
        found=vec[c].find("OOOO");

        if( found!=string::npos )
        {
            wo++;
        }
    }

    for( c=0; c<4 && !wo ; c++ )
    {
        cn=false;
        for( g=0; g<4 && !wo && !cn; g++ )
        {
            if( vec[g][c]!='O' )
                cn++;
        }

        if( !cn )
            wo++;
    }

    cn=false;
    for( c=0; c<4 && !cn && !wo ; c++ )
    {
        if( vec[c][c]!='O' )
            cn++;
    }

    if( !cn )
        wo++;

    cn=false;
    for( c=0; c<4 && !cn && !wo ; c++ )
    {
        if( vec[c][3-c]!='O' )
            cn++;
    }

     if( !cn )
        wo++;

    return wo;
}

int main()
{
    int n, c, g, x, y, cont, z;
    bool t, wx, wo, cn;
    string str;
    size_t found;
    ifstream in("A.in");
    ofstream out("A.out");

    in>>n;

    for( z=0; z<n; z++ )
    {
        t=wx=wo=cn=false;

        for( c=0; c<4; c++ )
        {
            in>>str;
            vec.push_back(str);
            found=str.find("T");

            if( found!=string::npos )
            {
                x=found;
                y=c;
                t++;
            }
        }

        wx=compx( x, y, t);
        wo=compy( x, y, t);

        out<<"Case #"<<z+1<<": ";
        if( wx && !wo )
            out<<"X won\n";
        else if( !wx && wo )
            out<<"O won\n";
        else if( !wx && !wo )
        {

            for( c=0; c<4 && !cn; c++ )
            {
                found=vec[c].find(".");

                if( found != string::npos )
                    cn++;
            }

            if( cn )
                out<<"Game has not completed\n";
            else
                out<<"Draw\n";
        }

        vec.clear();
    }

    return 0;
}
