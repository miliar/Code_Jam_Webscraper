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

    int t, ca = 1;

    cin >> t;

    while( t-- )
    {
        long long i, j, x = 0, y, n, m, cnt = 0, a;

    cin >> n ;


    int arr[100] = { 0 };

    x = n;
    y = 100000000;
    while( y-- )
    {
        m = x;

        while( m > 0 )
        {
            a = m % 10;

            if( arr[a] == 0 )
            {
                arr[a]++;
                cnt++;

            }
            m /= 10;
        }

        if( cnt >= 10 || n == 0 )
            break;
         x += n;
    }

    if( cnt < 10 )
        cout << "Case #" << ca << ": INSOMNIA" << endl;
    else
        cout << "Case #" << ca << ": " << x << endl;
    ca++;

    }


    return 0;

}


