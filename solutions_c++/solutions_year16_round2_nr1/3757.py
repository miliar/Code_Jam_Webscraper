#include<bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define pb push_back
using namespace std;
int arr[1000], arr1[1000];
vector < int > V;
int main()
{

   freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout );
   int t;
   cin >> t;
   cin.get();
   for( int k = 1; k <= t; k++ )
   {
       V.clear();
       memset( arr, 0, sizeof( arr ) );
       memset( arr1, 0, sizeof( arr1 ) );
       string s;
       getline( cin , s ) ;
       for( int i = 0; i < s.size(); i++ )
       {
           int cc = s[i] -'A';
           arr[cc]++;
           arr1[cc]++;
       }

       bool ok = true;

       int a, b , c, d, e;
          a = 'Z' - 'A';
       b = 'E' - 'A';
       c = 'R' - 'A';
       d = 'O' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  || arr[d] <= 0 ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           V.pb( 0 );
       }

       a = 'O' - 'A';
       b = 'N' - 'A';
       c = 'E' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           V.pb( 1 );
       }

       a = 'T' - 'A';
       b = 'W' - 'A';
       c = 'O' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           V.pb( 2 );
       }

        a = 'T' - 'A';
        b = 'H' - 'A';
        c = 'R' - 'A';
        d = 'E' - 'A';
        while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  || arr[d] < 2 ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           arr[d]--;
           V.pb( 3 );
       }
       a = 'F' - 'A';
        b = 'O' - 'A';
        c = 'U' - 'A';
        d = 'R' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  || arr[d] <= 0 ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           V.pb( 4 );
       }
       a = 'F' - 'A';
        b = 'I' - 'A';
        c = 'V' - 'A';
        d = 'E' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0 || arr[d] <= 0 ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           V.pb( 5 );
       }
       a = 'S' - 'A';
        b = 'I' - 'A';
        c = 'X' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           V.pb( 6 );
       }
        a = 'S' - 'A';
        b = 'E' - 'A';
        c = 'V' - 'A';
        d = 'N' - 'A';

       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] < 2  || arr[c] <= 0 || arr[d] <= 0 ) break;
           arr[a]--;
           arr[b]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           V.pb( 7 );
       }
        a = 'E' - 'A';
        b = 'I' - 'A';
        c = 'G' - 'A';
        d = 'H' - 'A';
        e = 'T' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0 || arr[d] <= 0 || arr[e] <= 0 ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           arr[e]--;
           V.pb( 8 );
       }
        a = 'N' - 'A';
        b = 'I' - 'A';
        c = 'E' - 'A';
       while( 1 )
       {
           if( arr[a] < 2 || arr[b] <= 0  || arr[c] <= 0 ) break;
           arr[a]--;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           V.pb( 9 );
       }
       bool pp = true;
       for( int i = 0; i < 30; i++ )
        {
            if( arr[i] > 0 )
            {
                pp = false;
                break;
            }

        }
        int ad = 0;
        if( pp ) ad = 1;


       string ps = "abcdefghij";
      while(std::next_permutation(ps.begin(), ps.end()))
       {

           if( ad == 1 ) break;
           V.clear();



           for( int i = 0; i < 26; i++ ) arr[i] = arr1[i];
           for( int i = 0; i < ps.size(); i++ )
           {

           int cnt = ps[i] - 'a';


           if( cnt == 0 ){

        a = 'Z' - 'A';
       b = 'E' - 'A';
       c = 'R' - 'A';
       d = 'O' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  || arr[d] <= 0 ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           V.pb( 0 );
       }
           }

        if( cnt == 1 ){

       a = 'O' - 'A';
       b = 'N' - 'A';
       c = 'E' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           V.pb( 1 );
       }
        }
        if( cnt == 2 ){
       a = 'T' - 'A';
       b = 'W' - 'A';
       c = 'O' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           V.pb( 2 );
       }
        }
        if( cnt == 3 )
        {


        a = 'T' - 'A';
        b = 'H' - 'A';
        c = 'R' - 'A';
        d = 'E' - 'A';
        while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  || arr[d] < 2 ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           arr[d]--;
           V.pb( 3 );
       }
        }
        if( cnt == 4 )
        {


       a = 'F' - 'A';
        b = 'O' - 'A';
        c = 'U' - 'A';
        d = 'R' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  || arr[d] <= 0 ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           V.pb( 4 );
       }
        }
        if( cnt == 5 ){
       a = 'F' - 'A';
        b = 'I' - 'A';
        c = 'V' - 'A';
        d = 'E' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0 || arr[d] <= 0 ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           V.pb( 5 );
       }
        }
        if( cnt == 6 )
        {


       a = 'S' - 'A';
        b = 'I' - 'A';
        c = 'X' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0  ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           V.pb( 6 );
       }
        }
        if( cnt == 7 )
        {

        a = 'S' - 'A';
        b = 'E' - 'A';
        c = 'V' - 'A';
        d = 'N' - 'A';

       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] < 2  || arr[c] <= 0 || arr[d] <= 0 ) break;
           arr[a]--;
           arr[b]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           V.pb( 7 );
       }
        }
        if( cnt == 8 )
        {

        a = 'E' - 'A';
        b = 'I' - 'A';
        c = 'G' - 'A';
        d = 'H' - 'A';
        e = 'T' - 'A';
       while( 1 )
       {
           if( arr[a] <= 0 || arr[b] <= 0  || arr[c] <= 0 || arr[d] <= 0 || arr[e] <= 0 ) break;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           arr[d]--;
           arr[e]--;
           V.pb( 8 );
       }
        }
        if( cnt == 9 )
        {

        a = 'N' - 'A';
        b = 'I' - 'A';
        c = 'E' - 'A';
       while( 1 )
       {
           if( arr[a] < 2 || arr[b] <= 0  || arr[c] <= 0 ) break;
           arr[a]--;
           arr[a]--;
           arr[b]--;
           arr[c]--;
           V.pb( 9 );
       }
        }

        for( int i = 0; i < 30; i++ )
        {
            if( arr[i] > 0 )
            {
                ok = false;
                break;
            }

        }
        if( ok ) break;
           }
           if( ok ) break;
       }
           sort( V.begin(),V.end() );

       cout << "Case #" << k << ": ";
       for( int i = 0; i < V.size(); i++ ) cout << V[i];
       cout << "\n";

   }




}
