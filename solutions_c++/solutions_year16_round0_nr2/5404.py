#include <bits/stdc++.h>

using namespace std;


int main()
{

    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);

    int T , z = 0 ;
    cin >> T;
    while( T--)
    {
        string s ;
        cin >> s ;
        long long steps = 0 , ch = 0 ;

        reverse( s.begin() , s.end() );

        for(int i=0 ; i<s.size() ; i++)
        {
            if( s[i] == '-' && !ch )
            {
                ch++;
                steps++;
            }
            else if ( s[i] == '+' && ch )
            {
                ch--;
                steps++;
            }

        }

        cout << "Case #" << ++z << ": " << steps << "\n";
    }
}

