#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
#define f(a,b,c)                for(int a=b;a<c;a++)
#define s(x)                    scanf("%d",&x);
#define sl(x)                   scanf("%lld",&x);
#define p(x)                    printf("%d\n",x);

#ifdef TRACE
    #define trace(x)                       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)                    cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)                  cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
#else
    #define trace(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
 
#endif


int a[1200];
int main(){
	#ifdef Megamind
			#define TRACE
            freopen("inp.txt","r",stdin);
            freopen("out.txt","w",stdout);
    #endif
	
	int t,n;
	s(t);
	f(i1,1,t+1){
		s(n);
		f(i,0,n) s(a[i]);
		
		ll first=0,maxd=-1,second=0;
		f(i,0,n-1){
			if(a[i+1]<=a[i]) {
				first+=a[i] - a[i+1];
				if((a[i]-a[i+1])>maxd) maxd = a[i] - a[i+1];
			}
		}
		
		f(i,0,n-1){
			second += min(maxd,(ll)a[i]);
			//cout<<second<<" ";
		}
		printf("Case #%d: %lld %lld\n",i1,first,second);
	}
}