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
#define pf          prlong longf
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define mn          (long long)-9223372036854775807
#define mx          (long long) 9223372036854775807
#define mod          1000000009


//set<long long>::iterator ii;

long long int  bm(long long int  base, int power) {    //bm represents bigmod
    if(power == 0)
    {
        return 1;
    }
    if(power % 2 == 0)
    {
        /*
        int ret = bm(base, power / 2, modu);
        return ret * ret;
        */
        long long int  ret = (bm(base, power / 2));
        return (ret * ret) ;
    }
    else
    {
        //return base * bm(base, power - 1, modu);
        return ( base * (bm(base, power - 1)) );
    }
}



int main()
{
    ios::sync_with_stdio(false);

    inf;
    outf;

    long long  t, ca = 1;

    cin >> t;

    while( t-- )
    {
         long long  i, j, x = 1, y, n, m, k , c, s, a = 1, z;

    cin >> k >> c >> s ;
    y = bm( k, c);



    z = y/k;
    cout << "Case #"<< ca <<": " ;

    if( c == 1 && k != s )
        cout << "IMPOSSIBLE";
    else if( k > s )
        cout << "IMPOSSIBLE";
    else
    {
        for( i=0; i<s; i++ )
    {
        cout << a << ' ';
        a += z;
    }

    }

    cout << endl;
    ca++;

    }





    return 0;

}


