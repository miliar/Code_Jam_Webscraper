/*
   AUTHOR: Peeyush yadav
   Problem:
*/
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define f(a,b,c)                for(int a=b;a<c;a++)
#define s(x)                    scanf("%d",&x);
#define sl(x)                   scanf("%lld",&x);
#define p(x)                    printf("%d\n",x);
#define pl(x)                   printf("%lld\n",x);
#define p1d(a,n)                for(int ix=0;ix<n;ix++) printf("%d ",a[ix]); printf("\n");
#define p2d(a,n,m)              for(int ix=0;ix<n;ix++){ for(int jx=0;jx<m;jx++) printf("%d ",a[ix][jx]); printf("\n");}
void input(){
    #ifdef Megamind
            #define DEBUG
            #define TRACE
            #define gc getchar()
            freopen("inp.txt","r",stdin);
            freopen("out.txt","w",stdout);
    #else
            #define gc getchar()
    #endif
}
#ifdef TRACE
    #define trace(x)                       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)                    cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)                  cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
#else
    #define trace(x)
    #define trace2(x,y)
    #define trace3(x,y,z) 
#endif
template <class T>
inline void read(T &n1){
	n1=0;
    char c=gc;
    while(c<'0' || c>'9') c=gc;
    while(c>='0' && c<='9'){
       n1=(n1<<3)+(n1<<1)+c-'0';
       c=gc;
    }
}
 
inline ll power(ll a, ll b, ll m) {
    ll r = 1;
    while(b) {
        if(b & 1) r = r * a % m;
        a = (a * a)% m;
        b >>= 1;
    }
    return r;
}
inline ll power(ll a, ll b) {
     ll r = 1;
    while(b) {
        if(b & 1) r = r * a ;
        a = a * a;
        b >>= 1;
    }
    return r;
}
 
/*........................................................END OF TEMPLATES.......................................................................*/
ll k,l,s;
char a[11],b[11],c[11];	

ll mm = 0,maxi = 0;

void rec(int i){
	
	if(i == s){
		int counter = 0;
		f(i1,0,s){
			bool flag =0 ;
			f(j,0,l){
				if(i1 + j >=s) flag = 1;
				if((i1 + j <s )   && c[i1+j]!=b[j]) {
					flag = 1;
					break;
				}
			}
			
			if(!flag){
				counter++;
				mm++;
			}
		}
		if(counter>maxi) maxi = counter;
	}
	else{
		f(x,0,k){
			c[i] = a[x];
			rec(i+1);
		}
	}
}

int main(){
	input();
	int t,n;
	s(t);
	for(int x = 1;x<=t;x++){
		mm = 0;
		maxi = 0;
		sl(k);
		sl(l);
		sl(s);
		cin>>a;
		cin>>b;
		rec(0);
		
		ll d = power(k,s);
		
		double x1 = 1.0 * mm / d;
		double ans = maxi - x1;
		//trace(maxi);
		printf("Case #%d: %.6f\n",x,ans);
		
		
	}

	#ifdef Megamind
		//cout << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC * 1000 << " ms." << endl;
    #endif
}