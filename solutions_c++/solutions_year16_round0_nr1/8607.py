/* Tariq ahmed khan - Daffodil */

#include <bits/stdc++.h>


#define pi 2*acos(0.0)
#define scan(x) scanf("%d",&x)
#define sf scanf
#define pf printf
#define pb push_back
#define memoclr(n,x) memset(n,x,sizeof(n) )
#define INF 1 << 30
#define foo(i,j,k) for(int (x)=(i);(x)<(j);(x)+=(k))
#define ffoo(i,j,k) for(int (x)=(i);(x)<=(j);(x)+=(k))


typedef long long LLI;
typedef unsigned long long LLU;

template<class T> T gcd(T x, T y){if (y==0) return x; return gcd(y,x%y);}
template<class T> T lcm(T x, T y){return ((x/gcd(x,y))*y);}
template<class T> T maxt(T x, T y){if (x > y) return x; else return y;}
template<class T> T mint(T x, T y){if (x < y) return x; else return y;}
template<class T> T power(T x, T y){T res=1,a = x; while(y){if(y&1){res*=a;}a*=a;y>>=1;}return res;}
template<class T> T bigmod(T x,T y,T mod){T res=1,a=x; while(y){if(y&1){res=(res*a)%mod;}a=((a%mod)*(a%mod))%mod;y>>=1;}return res;}


int dir[8][2]={{-1,0}
              ,{1,0}
              ,{0,-1}
              ,{0,1}
              ,{-1,-1}
              ,{-1,1}
              ,{1,-1}
              ,{1,1}};


using namespace std;

bool digChk[10];
int res;

void digitFound( int n ){
    int tmp = n;
    while( tmp > 0 ){
        int x = tmp%10;
        if( !digChk[x] ){
            digChk[x] = true;
            res++;
            //cout << x << " ";
        }
        tmp /= 10;
    }
}

int main() {
    //ios_base::sync_with_stdio(0);cin.tie(0);    // I/O optimization
    #ifdef partho222
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    int n, kase=0;
    scan(n);
    while(n--){
        res = 0;
        memoclr(digChk, false);

        int stDig;
        scan(stDig);
        if( stDig == 0 ){
            pf("Case #%d: INSOMNIA\n", ++kase);
        }
        else{
            for( int i=1; ;i++ ){
                digitFound( i*stDig );
                if( res == 10 ){
                    pf("Case #%d: %d\n", ++kase, i*stDig);
                    break;
                }
            }
        }
    }

    return 0;
}
