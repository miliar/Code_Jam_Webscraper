#pragma comment(linker, "/STACK:16777216")

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<time.h>
#include<iostream>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<utility>
#include<algorithm>
#include<list>
using namespace std;

#define pb push_back
#define MS( a ) memset( a,0,sizeof(a))
#define MSV( a,v ) memset( a,v,sizeof(a))

typedef long long Long;

#define MAX 10000007

Long A,B;

bool IsPalin( Long v )
{
    vector<Long> s;
    while( v ){
        s.pb( v%10 );
        v /= 10;
    }
    vector<Long> r = s;
    reverse( r.begin(),r.end());
    return r==s;
}

int main( void )
{
    Long i,j,Icase,k = 0;;

    //freopen("text1.txt","r",stdin );
    freopen("C.in","r",stdin );
    freopen("C.out","w",stdout );

    map<Long,Long> Map;
    for( i=1;i<=MAX;i++ ){
        if( !IsPalin( i ) ) continue;
        if( !IsPalin( i*i )) continue;
        Map[i*i] = Map.size();
    }

    cin>>Icase;
    while( Icase-- ){
        cin>>A>>B;
        map<Long,Long>::iterator p1 = Map.lower_bound( A );
        map<Long,Long>::iterator p2 = Map.upper_bound( B );
        p2--;
        Long Ans = p2->second - p1->second + 1;
        printf("Case #%I64d: %I64d\n",++k,Ans );
    }

    return 0;
}
