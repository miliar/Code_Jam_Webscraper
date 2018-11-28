//“Every strike brings me closer to the next home run.” -Babe Ruth
#include<bits/stdc++.h>
#define ROW 309
#define COL 309
#define MOD 1000000007
#define ll long long
#define endl "\n"

using namespace std;

bool mycomptwo(pair<int,int> a, pair<int,int> b)
{
    return a.first < b.first;
}

bool mycompthree(pair < int , pair<int,int> > a, pair < int , pair<int,int> > b)
{
    return a.first < b.first;
}

bool mycompfour(pair < pair<int,int>,pair<int,int> > a, pair < pair <int,int>,pair<int,int> > b)
{
    return a.first.first < b.first.first;
}

ll arr[15];

int main()
{
//   freopen( "currInput.txt" , "r" , stdin );
//   freopen( "currOutput2.txt" , "w" , stdout );

   freopen( "A-large.in" , "r" , stdin );
   freopen( "Output.txt" , "w" , stdout );

    ll cases;
    cin >> cases;

    ll ii;
    for ( ii = 1 ; ii <= cases ; ii++ )
    {
        ll n;
        cin >> n;

        cout << "Case #" << ii << ": ";
        ll i;

        for ( i = 0 ; i <= 14 ; i++ )
        {
            arr[i] = 0;
        }

        ll p = 0;

        if ( n == 0 )
        {
            cout << "INSOMNIA" << endl;
            continue;
        }

        while (1)
        {
            p += n;
            ll t = p;
            while ( t )
            {
                arr[t%10] = 1;
                t /= 10;
            }
            ll j;
            for ( j = 0 ; j <= 9 ; j++ )
            {
                if ( arr[j] == 0 )
                {
                    break;
                }
            }
            if ( j == 10 )
            {
                cout << p << endl;
                break;
            }
        }

    }




    return 0;
}

