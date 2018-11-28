#include<bits/stdc++.h>
using namespace std ;


long long a[100000] ;

int main()
{


long long rate ;
int t , n ;
cin >> t ;
long long f1 ;
long long f2 ;
for ( int x = 1 ; x <= t ; x++)
{
cin >> n ;
f1 = f2 = 0 ;

rate = 0 ;
for ( int i = 0 ; i < n ; i++)
{
cin >> a[i] ;
}

int i1  , i2 ;

for ( int i = 0 ; i <= ( n - 2 ) ; i++)
{
    int j = i + 1 ;
if ( a[i] > a[j])
{
f1 += a[i] - a[j] ;
rate = max ( rate ,  a[i] - a[j]) ;
}
}

for ( int i = 0 ; i < n - 1 ; i++)
{
    if ( rate > a[i] )
        f2 += a[i] ;
    else
        f2 += rate ;
}
cout << "Case #"<<x<<": "<<f1 <<  " " << f2 << endl ;

}

return 0 ;
}
