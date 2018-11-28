#pragma warning (disable: 4786)
#pragma comment (linker, "/STACK:26777216")
#include <bits/stdc++.h>

using namespace std;
typedef long long lint;
typedef unsigned long long ulint;
#define NN 10010
#define MM 1000002
#define CLR( a ) memset( a , 0 , sizeof ( a ) )
#define negCLR( a ) memset( a , -1 , sizeof( a ) )
#define lld I64d
#define FOR(i,s,t) for(int i = (s); i <= (t); i++)
#define ROF(i,t,s) for(int i = (t); i >= (s); i--)

const lint MOD =  100000007;
const lint LINF = 1000000097999999903LL;
lint boundz = 10000000001LL;
const int INF = (1 << 29);
int idz[ 220 ], offsetz = 107;
int mulz[ 220 ][ 220 ], divz[ 220 ][ 220 ];

char org[ ] = { '1', 'i', 'j', 'k' };
//map < int, string > revid;
int mvalz[ ] = { 49, 105, 106, 107,   105, -49, 107, -106,  106, -107, -49, 105,   107, 106, -105, -49  };
struct node{
    int val, sig; node(){} node( int a, char b ){ val = a; sig = b; }
};

node retMul[ NN ];
node  retDiv[ NN ];
struct vert{
    int id; char ch; vert(){} vert( int a, char b ){ id = a; ch = b; }
};

bool cmp( const vert &a, const vert &b ) {
    if( a.id == b.id ){ return a.ch < b.ch; }
    return a.id < b.id;
}

vert posz[ NN + NN ];

int N, X, L, caseno;
char arr[ NN ], brr[ NN ];
int crr[ NN ];
int aind, bind, posind;

void reset() {
    CLR( arr ); CLR(brr); aind = bind = 0; posind = 0;
    CLR( retMul ); CLR( retDiv ); CLR( posz );

}

void noZ(){  printf("Case #%d: NO\n",++caseno); }
void yesZ(){  printf("Case #%d: YES\n",++caseno); }

void pre_precal() {
    CLR( mulz ); CLR( divz );
    CLR( idz );   //printf("%d %d %d %d\n",'1','i','j','k');    //-k = -107  //49 105 106 107 1 i j k
    FOR( i , 0, 3 ) {  idz[ org[ i ] ] = (int)org[ i ] + offsetz;  }

    // if z - offsetz < 0 then pos = -1*z + offset;
   /*
    revid.clear();
    revid[ 49 + offsetz ] = "1";
    revid[ -49 + offsetz ] = "-1";
    revid[ 105 + offsetz ] = "i";
    revid[ -105 + offsetz ] = "-i";
    revid[ 106 + offsetz ] = "j";
    revid[ -106 + offsetz ] = "-j";
    revid[ 107 + offsetz ] = "k";
    revid[ -107 + offsetz ] = "-k";
    */
}
void precal() {
    int k = 0;
    FOR( i , 0, 3 ) {
        FOR( j, 0, 3 ) {
             int ith = idz[ org[ i ] ]; int jth = idz[ org[ j ] ];
             int x = mvalz[ k ] + offsetz; k++;
             mulz[ ith ][ jth ] =  x;

             divz[ x ][ ith ] = jth; // x/ith = jth
             divz[ x ][ jth ] = ith;

        }
        //cout<<endl;
    }
}

void process() {
    int Z = L * X;
    FOR( i, 1, Z + 1 ){ brr[ i ] = '\0'; }
    FOR( i, 1, L){ brr[ i ] = arr[ i ]; }
    bind = Z; // :p L + 1 to Z
    aind = 1;
    FOR( i, L + 1, Z ) {
      brr[ i ] = arr[ aind++ ];  if( aind > L ){ aind = 1;}
      //printf(" %c", brr[ i ]);
    }
    CLR( crr );
    FOR( i, 1, Z ) {
        crr[ i ] = idz[ brr[ i ] ];
    }

    //cout<<endl;
    //puts(brr + 1 );
}

int main() {
  //freopen("dd.in","r",stdin);
  //freopen("out3.txt","w",stdout);
  pre_precal(); precal();
  int cases; scanf("%d",&cases);
  while( cases-- ) {
      reset();
      scanf("%d %d",&L, &X); int Z = L * X;
      scanf("%s",arr + 1 );
      //puts( arr + 1 );
      process();
      int iPos = 1, kPos = 1;

      if( X * L <= 2 ){ noZ(); }
      else if( X*L == 3 ) {
           if(brr[ 1 ] == 'i' && brr[ 2 ] == 'j' && brr[ 3 ] == 'k' ){ yesZ(); }
           else{ noZ(); }
      } else {
          retMul[ 1 ] = node( crr[ 1 ], 1 ); int sig = 1;

          int ifl = 0, kfl = 0;

          FOR( i, 2, Z  ) {
               node ith = retMul[ i - 1 ];  int jth = crr[ i ];
               // if ith == neg convert it to positive
               int mulX =  mulz[ ith.val ][ jth ];
               sig = 1;

               if( mulX - offsetz < 0 ) {
                   sig = -1;
                   mulX = mulX - offsetz;    // conver val to pos  -49+offset = -49-offsetz,   -49, *-1, 49 + offsetz
                   mulX *= -1; mulX += offsetz;
               }
               if( ith.sig < 0 ){ // prev -1
                   sig =  sig == -1 ? 1 :  -1  ;
                } // -1 * -1 = 1

                retMul[ i ] = node( mulX, sig);

                if(  mulX == ('i' + offsetz) && sig == 1  ) {
                     ifl = 1;  //posz[ posind++ ] = vert( i , 'i');
                     iPos = min( iPos, i );

                }

          }



          node totMul = retMul[ Z ]; int lastVal = retMul[ Z ].val;
          if( totMul.sig == -1 ) {
              lastVal -= offsetz;   //convert to neg  49-offset as div array built for neg as well
              lastVal *= -1;
              lastVal += offsetz;
          }

          FOR( i, 1, Z-1 ) {
                 sig = totMul.sig;
                 node jth = retMul[ i ];
                 int divX = divz[ lastVal ][ jth.val ];  // jth val always pos for divz arr
                 if( divX - offsetz < 0  ) {  sig == -1 ? 1 : -1;
                    divX -= offsetz; divX *= -1; divX += offsetz; //convert to pos
                  } else {
                      sig = 1;
                  } // -1/-1 = 1
                  if( divX == ('k' + offsetz ) && sig == 1 ) {
                       kfl = 1; //posz[ posind++ ] = vert( i + 1, 'k'  );
                       kPos = max( kPos, i );
                  }


          }
          // if( tot / ik  == j  ) ret = true    i*k = -j
          int jfl = 0;
          int diff = kPos - iPos;
          if( ifl && kfl && (diff > 1 ) ) {
             sig = totMul.sig;   //-j convert it to j as div array is build for positive only
             int jth = 106 + offsetz;
             int divJ = divz[ lastVal ][ jth ];
             if( ( ( divJ == 106 + offsetz ) && sig == -1 ) || ( ( divJ == -106 + offsetz ) && sig == 1 ) ) { // j & -neg || -j && pos cause ik = neg
                 jfl = 1;
             }

          }



          if( ifl && jfl && kfl ) {
              yesZ();
          } else {
              noZ();
          }

      }

  }
  return 0;
}
