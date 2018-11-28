    using namespace std;
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cstring>
#include <string>

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)

#define SET(a,x) memset((a),(x),sizeof(a))
#define COPY(a,b) memcpy((a),(b),sizeof(a))
// set = 0
#define PB push_back
#define TR(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();it++)

#define EXIST(c,x) (c.find(x)!=c.end())

typedef double LL;
typedef pair<int,int>II;
typedef pair<int,II>III;

#define ST first
#define ND second

typedef vector<int>VI;
typedef vector<VI>VVI;
typedef vector<II>VII;
typedef vector<VII>VVII;

int ntest;
int n,a,b,k;

int fa[64],fb[64],fk[64],flag,d[100][2][2][2];
int base = 10000;
struct bignum{
   int a[20];       
   
   void creat(){
      SET(a,0);
   }
   
   void load(int x){
      creat();
      a[0]=1;a[1]=x;     
   }
   
   bool operator<(const bignum& op){
      if(a[0]!=op.a[0]) return(a[0]<op.a[0]);
      
      FORD(i,a[0],1) if(a[i]!=op.a[i]) return(a[i]<op.a[i]);
   }
   
   bignum operator+(const bignum& op){
      bignum z;
      z.creat();
      z.a[0]=max(a[0],op.a[0]);
      
      FOR(i,1,z.a[0]){
         int p=z.a[i]+a[i]+op.a[i];
         z.a[i]=p%base;
         z.a[i+1]+=p/base;
      }
      
      if(z.a[z.a[0]+1]>0) z.a[0]++;
      return z;
   }
   
   bignum operator-(const bignum& op){
      // trustly that a>b -> a-b;
      
      bignum z;
      z.creat();
      
      int carry=0;
      
      z.a[0]=a[0];
      
      FOR(i,1,a[0]){
        int p= a[i] - op.a[i]-carry;
        if(p < 0){
           z.a[i]=p+base;carry=1;     
        }else {
           z.a[i]=p;carry=0;      
        }
      }
      

      while(z.a[0]>1 && z.a[z.a[0]]==0) z.a[0]--;
      return z;
   }
   
   bignum operator*(const bignum& op){
       bignum z;
       z.creat();
       
       z.a[0]=a[0]+op.a[0]-1;
       
       FOR(i,1,a[0]){
           FOR(j,1,op.a[0]){
              int p=z.a[i+j-1]+a[i] * op.a[j];
              z.a[i+j-1]=p%base;
              z.a[i+j]+=p/base;
           }           
       }
       if(z.a[z.a[0]+1]>0) z.a[0]++;
       return z;
   }
   
   void print(){
      printf("%d",a[a[0]]);
      FORD(i,a[0]-1,1) printf("%04d",a[i]);
   }
};


bignum f[100][2][2][2],res;
bignum cal(int pos,int ok1,int ok2,int ok3){
    if(pos > 63){
        f[pos][ok1][ok2][ok3].load(1);
        return f[pos][ok1][ok2][ok3];
    }
    if(d[pos][ok1][ok2][ok3] == flag) return f[pos][ok1][ok2][ok3];

    d[pos][ok1][ok2][ok3] = flag;

    int la,lb;

    if(ok1){
        la = 1;
    } else la = fa[pos];

    if(ok2){
        lb = 1;
    } else lb = fb[pos];

    bignum tmp;
    tmp.load(0);

    FOR(ia,0,la) FOR(ib,0,lb) {
        int ok1_ = ok1 | (ia < fa[pos]);
        int ok2_ = ok2 | (ib < fb[pos]);
        int ok3_ = ok3 | ((ia & ib) < fk[pos]);
        if(ok3 || !(ia & ib > fk[pos]) )
        tmp = tmp + cal(pos+1,ok1_,ok2_,ok3_);
    }
    f[pos][ok1][ok2][ok3] = tmp;
    return tmp;
}

int main(){

    freopen("B-large.in","r",stdin);
    freopen("out","w",stdout);

    cin >> ntest;
    
    flag =  0;

    FOR(test,1,ntest){
    
        cin >> a >> b >> k;
        
        a--;
        b--;
        k--;

        flag++;

        FORD(i,63,0) {
            fa[i] = a % 2; a/=2;
            fb[i] = b % 2; b/=2;
            fk[i] = k % 2; k/=2;
        }
        
        res = cal(0,0,0,0);
    
        cout <<"Case #"<<test<<": ";
        res.print();;cout<<endl;
    }
    return 0;
}
