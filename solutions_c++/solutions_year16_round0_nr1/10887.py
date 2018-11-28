#include <bits/stdc++.h>
#define        ll                              long long
#define        f(x,y,z)                        for(int x=y;x<z;x++)
#define        take1(a);                       scanf("%d",&a);
#define        take2(a,b);                     scanf("%d%d",&a,&b);
#define        take3(a,b,c);                   scanf("%d%d%d",&a,&b,&c);
#define        take4(a,b,c,d);                 scanf("%d%d%d%d",&a,&b,&c,&d);
#define        pii                             pair<int,int>
#define        mem(a,x)                        memset(a,x,sizeof(a))
#define        N                               1000010
#define        M                               1000000007
#define        pi                              acos(-1.0)
#define        ff                              first
#define        ss                              second
#define        pb                              push_back
using namespace std;
int dx[]={0,0,1,-1,-1,-1,1,1};
int dy[]={1,-1,0,0,-1,1,1,-1};
template < class T> inline T gcd(T a, T b){while(b){a%=b;swap(a,b);}return a;}
template <class T> inline T bigmod(T p,T e,T m){
    ll ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % m;
        p = (p * p) % m;
    } return (T)ret;
}
inline int nxt(){
  int aaa;
  scanf("%d",&aaa);
  return aaa;
}
string multiply( string a, long long b ) {
        int carry = 0;
        for( int i = 0; i < a.size(); i++ ) {
            carry += (a[i] - 48) * b;
            a[i] = ( carry % 10 + 48 );
            carry /= 10;
        }
        while( carry ) {
            a += ( carry % 10 + 48 );
            carry /= 10;
        }
        return a;
    }
    int main()
    {
    freopen("out.txt","w",stdout);
    ll a[1000]={0};
    int q=0,k=1;
   int test=nxt();
   while(test--){
          ll c=0,i;
          ll n=nxt();
          if(n==0){

            printf("Case #%d: INSOMNIA\n",k++);continue;
          }
        for(i=1; ;i++){
            ll p=n*i;
              while(p){
                 int x=p%10;
                 p/=10;
                 if(!a[x]){
                    a[x]=1;
                      c++;
                 }
                 if(c==10)
                      break;
              }
              if(c==10)
                  break;
        }
         printf("Case #%d: %lld\n",k++,i*n);
        mem(a,0);
  }
    }


