#include<iostream>
#include<string.h>
using namespace std;

pair<int,int> a[1000000];
int b[1000000], c[1000000], yo[1000000];
int f ( int x[], int n )
{
    if ( n <= 2 )
    return 0;
    int g = 1000000,i, y = -1;
    for ( i = 0; i < n; i++ )
    {
        if ( g > x[i] )
        g=x[i],y = i;
    }
    int jo=0;
    for ( i = 0; i < n; i++ )
    {
        if ( x[i] != g )
        yo[jo++]=x[i];
    }
    return min(n-y-1,y)+f(yo,n-1);
}
int main()
{
    freopen ("output.txt","w",stdout);
    freopen ("o.txt","r",stdin);
    int t, o = 0;  
    cin >> t;
     while ( t-- )
     {
           int n,m;
           cin >> n;
           for ( int i = 0; i < n; i++ )
           {
           cin >> a[i].first;
           a[i].second = i;
           }
           sort(a,a+n);
           int k;
           for ( int i = 0; i < n; i++ )
           {
               b[a[i].second] = i;
           }
           cout << "Case" << " #"<< ++o<<": "<< f(b,n) << endl;
      }
      cin>>t;                                    
  //string s;
 // cin >> s;
  //cout << "pogo"<<endl;
//    cout << "Hello World"<<endl;
}
