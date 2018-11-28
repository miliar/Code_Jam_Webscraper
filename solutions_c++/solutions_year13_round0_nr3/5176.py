#include<iostream>
#include<stdlib.h>
#include<vector>

using namespace std;

int palindrome(unsigned long long i)
{
    unsigned long long temp=i;
    int a[100],c=-1,flag=0;
    
    while( temp > 0 )
    {
           a[++c] = temp%10;
           temp = temp / 10;
    }
    for( int i = 0 ; i < (c/2+1); i++)
    {
         if( a[i]!=a[c-i])
         flag = 1;
    }
    if( flag == 0 )
    return 1;
    else
    return 0;
}
int main ()
{
    int j,t;
    vector<unsigned long long> v;
    unsigned long long ar=1,br=10000000,count=0;
    for ( unsigned long long i = ar; i <= br ; i++ )
    {
        if( palindrome(i) && palindrome(i*i))
        {
            v.push_back(i*i);
        }
    }

    cin>>t;
    for ( j = 1; j <= t ; j++ )
    {
    unsigned long long a,b;
    cin>>a>>b;
    int count=0;

    for ( int i = 0; i < v.size() ; i++ )
    {
        if(v[i]>=a && v[i]<=b)
        count++;
        if(v[i]>b)
        break;
    }
    printf("Case #%d: %u\n",j, count);
    }
    return 0;
}
