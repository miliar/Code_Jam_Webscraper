#include <iostream>
#include <math.h>
#include <conio.h>

using namespace std;

int arr[14];

int isPallin( long x )
{
    int i = 0 ;
    while ( x > 0 )
    {
          arr[i] = x%10;
          x /= 10;
          ++i;
    }
    --i;
    int j;
    for ( j = 0 ; j < i/2 + 1 ; ++j )
        if ( arr[j] != arr[i-j] )
           return 0;
    return 1;
}

int isSquare( float x )
{
    float sq = sqrt(x);
    if ( sq != floor(sq) )
       return 0;
    else if ( isPallin( (long) sq ) )
         return 1; 
}

int main()
{
    long i , t , j , x , a , b , count = 0;
    cin>>t; //cin>>x;
    for ( j = 0 ; j < t ; ++j )
    {
    cin>>a>>b;
    long sqb = sqrt ( b ) ;
    long sq = ceil ( (sqrt ( a ) ) ) ;
    
    for ( i  = sq ; i <= sqb ; ++i )
           if ( ( isPallin( i ) ) )
           {
                long z = i*i;
                if ( isPallin(z) )
                {
                     //cout<<isPallin(z)<<"  "<<i*i<<endl;
                         ++count;
                         }
           }
        cout<<"Case #"<<j+1<<": "<<count<<endl;
        count = 0;
        
    }/*
    cout<<isPallin(x);/*
    cout<<isSquare(101)<<endl;
    cout<<count<<endl;
    getch();*/
    getch();
}
         
