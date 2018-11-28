#include <iostream>
#include <math.h>
#include <map>
#include <vector>
#include <stdlib.h>
#include <memory.h>
#include <time.h>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <set>

using namespace std;

long long x[ 10000 ];
long long y[ 10000 ];
int id[ 10000 ];
bool red[ 10000 ];

int M;

bool cmp( int a , int b )
{
    return (x[M]*(y[a]-y[b])-x[a]*(y[M]-y[b])+x[b]*(y[M]-y[a]))>0;
}

void func( vector< int > v )
{
    if( v.size() <= 1 ) return;
    if( v.size() == 2 )
    {
        if( red[ v[0] ] )
            swap( v[0] , v[1] );

        printf( "%d %d\n" , id[v[0]] , id[v[1]] );
        return;
    }
    int Id = 0;
    for( int i = 1 ; i < v.size() ; ++i )
        if( (x[v[Id]] == x[v[i]] && y[v[Id]] > y[v[i]]) || x[v[Id]] > x[v[i]] )
            Id = i;

    M = v[Id];
    v.erase( v.begin() + Id );

    sort( v.begin() , v.end() , cmp );


    int bl , rd;
    bl = rd = 0;
    for( int i = 0 ; i < v.size() ; ++i )
    {
        if( red[v[i]] + red[M] == 1 )
        {
            if( rd == bl )
            {
                vector< int > tmp;
                int a , b;
                a = v[i];
                b = M;

                if( red[a] ) swap( a , b );


                printf( "%d %d\n" , id[a] , id[b] );

                for( int k = 0 ; k < i ; ++k )
                    tmp.push_back( v[k] );
                func( tmp );

                tmp.clear();
                for( int k = i+1 ; k < v.size() ; ++k )
                    tmp.push_back( v[k] );

                func( tmp );
                return;
            }
        }
        rd += red[v[i]];
        bl += !red[v[i]];
    }
}

int main()
{
	freopen( "input.txt" , "r" , stdin );freopen( "output.txt" , "w" , stdout );
    int t;
    scanf( "%d" , &t ); //cin >> t;
    vector< int > v;
    while(t--)
    {
        int n;
        scanf( "%d" , &n ); //cin >> n;
        v.clear();
        int l = 0;
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] ); //cin >> a.x >> a.y;
            red[l] = 0;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] );//cin >> a.x >> a.y;
            red[l] = 1;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        func( v );
    }
    while(t--)
    {
        int n;
        scanf( "%d" , &n ); //cin >> n;
        v.clear();
        int l = 0;
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] ); //cin >> a.x >> a.y;
            red[l] = 0;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] );//cin >> a.x >> a.y;
            red[l] = 1;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        func( v );
    }
    while(t--)
    {
        int n;[l] = i+1;
            v.push_back( l );
            ++l;
        }
        func( v );
    }
    while(t--)
    {
        int n;
        scanf( "%d" , &n ); //cin >> n;
        v.clear();
        int l = 0;
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] ); //cin >> a.x >> a.y;
            red[l] = 0;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] );//cin >> a.x >> a.y;
            red[l] = 1;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        func( v );
    }
    while(t--)[l] = i+1;
            v.push_back( l );
            ++l;
        }
        func( v );
    }
    while(t--)
    {
        int n;
        scanf( "%d" , &n ); //cin >> n;
        v.clear();
        int l = 0;
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] ); //cin >> a.x >> a.y;
            red[l] = 0;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] );//cin >> a.x >> a.y;
            red[l] = 1;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        func( v );
    }
    while(t--)[l] = i+1;
            v.push_back( l );
            ++l;
        }
        func( v );
    }
    while(t--)
    {
        int n;
        scanf( "%d" , &n ); //cin >> n;
        v.clear();
        int l = 0;
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] ); //cin >> a.x >> a.y;
            red[l] = 0;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] );//cin >> a.x >> a.y;
            red[l] = 1;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        func( v );
    }
    while(t--)
        scanf( "%d" , &n ); //cin >> n;
        v.clear();
        int l = 0;
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] ); //cin >> a.x >> a.y;
            red[l] = 0;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] );//cin >> a.x >> a.y;
            red[l] = 1;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        func( v );
    }
    while(t--)
    {
        int n;
        scanf( "%d" , &n ); //cin >> n;
        v.clear();
        int l = 0;
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] ); //cin >> a.x >> a.y;
            red[l] = 0;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        for( int i = 0 ; i < n ; ++i )
        {
            scanf( "%lld %lld" , &x[l] , &y[l] );//cin >> a.x >> a.y;
            red[l] = 1;
            id[l] = i+1;
            v.push_back( l );
            ++l;
        }
        func( v );
    }
    return 0;
}
