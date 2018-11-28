#define ll __int64
#define vi vector <int>
#define pii pair <int,int>
#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((int)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("in.txt","r",stdin)
#define filew() freopen("out.txt","w",stdout)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <cassert>


using namespace std;



#define nn 10002

int D[nn],N[nn],E[nn],W[nn],S[nn],dd[nn],dp[nn],ds[nn];



struct Event
{
    ll d,w,e,s;
};

bool cmp( Event e1, Event e2  )
{
    return e1.d<e2.d;
}



#define MM 10000000

struct Tree
{
    int l,r;
    ll m;
    bool lz;
};

Tree T[ MM ];

void build( int n,int l,int r )
{



	T[n].m=0;
    T[n].l=l;
    T[n].r=r;

    if( T[n].l==T[n].r )return;

    int mid=(l+r)>>1;


    build(  2*n ,l,mid );
    build(  2*n+1 ,mid+1,r );

}




ll query( int n,int l,int r )
{


    if( T[n].lz )
    {
        if( T[n].l!=T[n].r )
        {

            T[2*n].m=MAX( T[n].m,T[2*n].m );
            T[2*n+1].m=MAX( T[n].m,T[2*n+1].m );

            T[ 2*n ].lz=1;
            T[ 2*n +1 ].lz=1;


            T[n].lz=0;
        }
    }

    if( T[n].l>r || T[n].r<l )return 1000000000LL*1000000000;
    if( T[ n ].l>=l && T[n].r<=r )return T[n].m;




    ll q1,q2;

    q1=query( 2*n,l,r );
    q2=query( 2*n+1,l,r );



    return MIN( q1,q2 );


}

void update( int n,int l,int r,int v )
{


    if( T[n].lz )
    {
        if( T[n].l!=T[n].r )
        {

            T[2*n].m=MAX( T[n].m,T[2*n].m );
            T[2*n+1].m=MAX( T[n].m,T[2*n+1].m );

            T[ 2*n ].lz=1;
            T[ 2*n +1 ].lz=1;


            T[n].lz=0;
        }
    }



    if( T[n].l>r || T[n].r<l )return;
    if( T[ n ].l>=l && T[n].r<=r )
    {

        T[n].m=MAX( v,T[n].m );
        T[n].lz=1;

        return;
    }



    update( 2*n,l,r,v );
    update( 2*n+1,l,r,v );



    T[n].m=MIN( T[2*n].m , T[2*n+1].m );


    return;
}







int main()
{
    int i,j,k,ks,t,x,n;


   // filer();


   freopen("C-large.in","r",stdin);
    freopen("C-large.txt","w",stdout);


    scanf("%d",&t);


    FOR(ks,1,t)
    {

        scanf("%d",&n);

        int tot=0;

        Event e,le;

        vector<Event>v;


      //  cout<<n<<endl;

        REP(i,n)
        {



            scanf("%d",&D[i]);
            scanf("%d",&N[i]);

            scanf("%d",&W[i]);
            scanf("%d",&E[i]);


//            W[i]*=2;
  //          E[i]*=2;

    //        W[i]+=off;
      //      E[i]+=off;

            scanf("%d",&S[i]);
            scanf("%d",&dd[i]);
            scanf("%d",&dp[i]);

//            dp[i]*=2;

            scanf("%d",&ds[i]);




            e.d=D[i];
            e.w=W[i];
            e.e=E[i];
            e.s=S[i];


            v.pb( e );

            le=e;


            FOR(j,1,N[i]-1)
            {


                e.d=le.d+dd[i];
                e.w=le.w+dp[i];
                e.e=le.e+dp[i];
                e.s=le.s+ds[i];


                v.pb(e);

                le=e;


            }


        }


        sort(ALL(v),cmp);


        set< ll >Set;
        map< ll,int >Map;



        int sz=SZ(v);

        REP(i,sz)
        {
            Set.insert( v[i].w );
			Set.insert( v[i].e );
        }


        set< ll > :: iterator  it = Set.begin();

        int idx=0;

        for(;it!=Set.end();it++)Map[ *it ]=++idx;





        REP( i,sz )
        {

            v[i].w=Map[ v[i].w ];
            v[i].w*=2;

            v[i].e=Map[ v[i].e ];
            v[i].e*=2;

        }



        idx*=2;

        build(1,1,idx);



        REP( i,sz )
        {




//            SET(NT,0);


            vi up1,up2,val;

            for( j=i;j<sz;j++ )
            {
                if( v[i].d!=v[j].d )break;

                e=v[j];


              //  cout<<e.d<<" "<<e.w<<" "<<e.e<<" "<<e.s<<endl;



                int mv= query( 1,e.w,e.e );


                if( mv<e.s  )
                {
                 //   cout<<"asd"<<endl;

                    tot++;

                    up1.pb( e.w );
                    up2.pb( e.e );
                    val.pb( e.s );

                }


            }





            i=j-1;





            REP(j,SZ( val ))
            {
                update( 1,up1[j],up2[j],val[j] );
            }


        }


        printf("Case #%d: %d\n",ks,tot);
    }


    return 0;

}
