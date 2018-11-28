#include<iostream>
#include <algorithm>
#include <vector>
#include<string>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<set>
#include <utility>

using namespace std;

#define inf         freopen("in.txt", "r", stdin);
#define outf        freopen("out.txt", "w", stdout);
#define pf          printf
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define mn          (long long)-9223372036854775807
#define mx          (long long) 9223372036854775807
#define mod          1000000009


//set<int>::iterator ii;



int main()
{
    ios::sync_with_stdio(false);

    inf;
    outf;

    long long  t, ca = 1;

    cin >> t;

    while( t-- )
    {
        long long  i, j, x, y, n, m, a = 0;

    string str, chk;

    cin >> str;
    chk = str;
    n = str.size();

    while( true )
    {
       x = -1;
       for( i=0; i<n; i++ )
       {
         if( str[i] == '-' )
            x = i;
       }



       if( x != -1)
       {
            if( str[0] == '+' && x != 0 )
            {
                i = 0;

                while( str[i] == '+' )
                {
                    str[i] = '-';
                    i++;
                }
                a++;
            }
            y = 0;
            for( i = x; i >= 0; i--,y++ )
            {
                if( str[i] == '+' )
                    chk[y] = '-';
                else
                    chk[y] = '+';
            }
            str = chk;
            //cout << str << endl;
            a++;
       }

       else
        break;
    }

        cout << "Case #" << ca << ": " << a << endl;
    //cout << a << endl;

    ca++;

    }



    return 0;

}


