#pragma comment(linker, "/STACK:16777216")

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
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

#define MAX 107
#define MOD 1000002013

typedef long long Long;

Long N,M;
Long Entry[MAX+7];
Long Exit[MAX+7];


Long SUM( Long s )
{
    if( s<=1 ) return 0;
    else return (s*(s-1))/2;
}


void Update( map<Long,Long> &s )
{
    map<Long,Long> Tmp;
    map<Long,Long>::iterator p = s.begin();
    while( p!=s.end()){
        Tmp[p->first+1] = p->second;
        p++;
    }
    s = Tmp;
}

Long FindMin( map<Long,Long> &s )
{
    Long v = s.begin()->first;
    s[v]--;
    if( !s.begin()->second ){
        s.erase( v );
    }
    return v;
}


void Print( map<Long,Long> &s )
{
    map<Long,Long>::iterator p = s.begin();
    while( p!=s.end()){
        printf("%I64d %I64d\n",p->first,p->second );
        p++;
    }
    printf("\n");
}

int main( void )
{
    Long i,j,u,v,p,Icase,k=0;

    //freopen("text1.txt","r",stdin );
    freopen("A.in","r",stdin );
    freopen("A.out","w",stdout );

    cin>>Icase;
    while( Icase-- ){
        cin>>N>>M;
        Long Min = 0,Max = 0;
        MS( Entry );
        MS( Exit );
        for( i=1;i<=M;i++ ){
            scanf("%I64d%I64d%I64d",&u,&v,&p );
            Entry[u] += p;
            Exit[v] += p;
            Long l = v-u;
            Min += l*N*p;
            Min %= MOD;
            Max += p*(l*N - SUM( l ));
        }
        //cout<<Max<<" "<<Min<<endl;
        map<Long,Long> s;
        for( i=1;i<=N;i++ ){
            Update( s );
            //Print( s );
            for( j=1;j<=Entry[i];j++ ){
                s[0]++;
            }
            for( j=1;j<=Exit[i];j++ ){
                Long v = FindMin( s );
                //cout<<"here "<<v<<endl;
                Min -= SUM( v );
                //cout<<Min<<endl;
                Min %= MOD;
                Min = (Min+MOD)%MOD;
            }
        }
        //cout<<Min<<endl;
        Min = ( Min+MOD )%MOD;
        Long Ans = ( Max - Min + MOD )%MOD;
        Ans = ( Ans + MOD)%MOD;
        cout<<"Case #"<<++k<<": "<<Ans<<endl;
    }

    return 0;
}
