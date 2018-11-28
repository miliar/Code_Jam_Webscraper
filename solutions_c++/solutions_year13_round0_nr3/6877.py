#include<iostream>
#include<cmath>
#include<stdlib.h>

using namespace std;

int palindrome(unsigned long long i)
{
    unsigned long long temp=i;
    int a[100],c=-1,flag=0;
    while( temp > 0 )
    {
           a[++c]=temp%10;
           temp/=10;
    }
    for( int i=0 ; i < (c/2+1); i++)
    {
         if( a[i]!=a[c-i])
         flag=1;
    }
    if( flag== 0 )
    return 1;
    else
    return 0;
}
int main ()
{
    int j,t;
    cin>>t;
    for ( j = 1; j <= t ; j++ )
    {
    unsigned long long a,b;
    cin>>a>>b;
    unsigned long long ar=ceil(sqrt(a)),br=floor(sqrt(b)),count=0;
    //cout<<ar<<br;
    for ( unsigned long long i = ar; i <= br ; i++ )
    {
        if( palindrome(i) && palindrome(i*i))
        {
            count++;
        }
    }
    printf("Case #%d: %u\n",j, count);
    }
    //system("pause");
    return 0;
}
