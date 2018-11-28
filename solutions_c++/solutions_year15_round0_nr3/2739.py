#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    int z;
    cin >> z;
    int o = 1;
    while( z -- )
    {
        int l, x;
        string a, b;
        cin >> l >> x;
        cin >> a;
        for( int i = 0; i < x; i ++ )
        {
            b += a;
        }
        string t = "1";
        bool flag = false;
        for( int i = 0; i < b.size(); i ++ )
        {
            //cout << t << " ";
            if( b[i] == 'i' )
            {
                //cout << b[i] << " " << t << "\n";
                if( t == "1" ) t = "i";
                else if( t == "-1" ) t = "-i";
                else if( t == "i" ) t = "-1";
                else if( t == "-i" ) t = "1";
                else if( t == "j" ) t = "-k";
                else if( t == "-j" ) t = "k";
                else if( t == "k" ) t = "j";
                else if( t == "-k" ) t = "-j";
                //cout << b[i] << " " << t << "\n";
            }
            if( b[i] == 'j' )
            {
                if( t == "1" ) t = "j";
                else if( t == "-1" ) t = "-j";
                else if( t == "i" ) t = "k";
                else if( t == "-i" ) t = "-k";
                else if( t == "j" ) t = "-1";
                else if( t == "-j" ) t = "1";
                else if( t == "k" ) t = "-i";
                else if( t == "-k" ) t = "i";
            }
            if( b[i] == 'k' )
            {
                if( t == "1" ) t = "k";
                else if( t == "-1" ) t = "-k";
                else if( t == "i" ) t = "-j";
                else if( t == "-i" ) t = "j";
                else if( t == "j" ) t = "i";
                else if( t == "-j" ) t = "-i";
                else if( t == "k" ) t = "-1";
                else if( t == "-k" ) t = "1";
            }
            if( t == "i" )
            {
                string s = "1";
                int j;
                for( j = i + 1; j < b.size(); j ++ )
                {
                    if( s == "j" ) break;
                    if( b[j] == 'i' )
                    {
                        if( s == "1" ) s = "i";
                        else if( s == "-1" ) s = "-i";
                        else if( s == "i" ) s = "-1";
                        else if( s == "-i" ) s = "1";
                        else if( s == "j" ) s = "-k";
                        else if( s == "-j" ) s = "k";
                        else if( s == "k" ) s = "j";
                        else if( s == "-k" ) s = "-j";
                    }
                    if( b[j] == 'j' )
                    {
                        if( s == "1" ) s = "j";
                        else if( s == "-1" ) s = "-j";
                        else if( s == "i" ) s = "k";
                        else if( s == "-i" ) s = "-k";
                        else if( s == "j" ) s = "-1";
                        else if( s == "-j" ) s = "1";
                        else if( s == "k" ) s = "-i";
                        else if( s == "-k" ) s = "i";
                    }
                    if( b[j] == 'k' )
                    {
                        if( s == "1" ) s = "k";
                        else if( s == "-1" ) s = "-k";
                        else if( s == "i" ) s = "-j";
                        else if( s == "-i" ) s = "j";
                        else if( s == "j" ) s = "i";
                        else if( s == "-j" ) s = "-i";
                        else if( s == "k" ) s = "-1";
                        else if( s == "-k" ) s = "1";
                    }
                }
                string m = "1";
                for( j; j < b.size(); j ++ )
                {
                    if( b[j] == 'i' )
                    {
                        if( m == "1" ) m = "i";
                        else if( m == "-1" ) m = "-i";
                        else if( m == "i" ) m = "-1";
                        else if( m == "-i" ) m = "1";
                        else if( m == "j" ) m = "-k";
                        else if( m == "-j" ) m = "k";
                        else if( m == "k" ) m = "j";
                        else if( m == "-k" ) m = "-j";
                    }
                    if( b[j] == 'j' )
                    {
                        if( m == "1" ) m = "j";
                        else if( m == "-1" ) m = "-j";
                        else if( m == "i" ) m = "k";
                        else if( m == "-i" ) m = "-k";
                        else if( m == "j" ) m = "-1";
                        else if( m == "-j" ) m = "1";
                        else if( m == "k" ) m = "-i";
                        else if( m == "-k" ) m = "i";
                    }
                    if( b[j] == 'k' )
                    {
                        if( m == "1" ) m = "k";
                        else if( m == "-1" ) m = "-k";
                        else if( m == "i" ) m = "-j";
                        else if( m == "-i" ) m = "j";
                        else if( m == "j" ) m = "i";
                        else if( m == "-j" ) m = "-i";
                        else if( m == "k" ) m = "-1";
                        else if( m == "-k" ) m = "1";
                    }
                }
                if( m == "k" ) flag = true;
            }
            if( flag == true ) break;
            //cout << t << "\n";
        }
        //cout << t << " ";
        if( flag == true ) cout << "Case #" << o << ": YES\n";
        else cout << "Case #" << o << ": NO\n";
        o ++;
    }
    return 0;
}
