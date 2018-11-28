#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    int t;
    cin >> t;
    cin.get();
    for( int kk = 1; kk <= t; kk++ )
    {
        string s;
        getline( cin , s );
        cout << "Case #" << kk << ": ";
        /*

        int sum = 0;
        int i = s.size() - 1;
        while( i >= 0 )
        {
            if( s[i] == '+' ) i--;
            if( s[i] == '-' )
            {
                sum++;
                int ck = 0;
                for( int j = i-1; j>= 0; j-- )
                {
                    ck = j;
                    if( s[j] == '+' )break;
                }
                for( int k = 0; k <= ck; k++ )
                {

                    if( s[k] == '+' )
                    {
                        s[k] = '-';
                    }
                    else s[k] = '+';
                }
                i = ck;
            }

        }
        */

        int sum1 = 0;
        bool ok = false;
        int ii = s.size() - 1;
        while( ii >= 0 )
        {
            if( s[ii] == '-' )
            {
                ok = true;
                ii--;
            }
            if( !ok && s[ii] == '+' ) ii--;
            if( ok && s[ii] == '+' )
            {
                sum1++;
                for( int jj = 0; jj <= ii; jj++ )
                {
                    if( s[jj] == '+' ) s[jj] = '-';
                    else s[jj] = '+';
                }
            }
        }
        if( ok ) sum1++;

        cout << sum1  << "\n";

    }
}
