/*
   (•_•)
   <) )>
    / \
   AUTHOR  : Peeyush Yadav
   Problem : 
*/
#include<bits/stdc++.h>
using namespace std; typedef long long ll; typedef pair<int,int> grp;
inline ll power(ll a,ll b)     { ll r=1; while(b){ if(b&1) r=r*a    ; a=a*a    ; b>>=1;} return r;}
inline ll power(ll a,ll b,ll m){ ll r=1; while(b){ if(b&1) r=(r*a)%m; a=(a*a)%m; b>>=1;} return r;}
void fast(){	
	#ifdef Megamind
		freopen("inp.txt","r",stdin);
		freopen("out.txt","w",stdout);
		#define trace(x)            cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
		#define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
		#define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
	#else
		#define trace(x)
		#define trace2(x,y)
		#define trace3(x,y,z)
	#endif
	
	#define fi						first
	#define se						second
	#define mp						make_pair
	#define pb(x)					push_back(x)
	#define s(x)					scanf("%d",&x);
	#define sl(x)					scanf("%lld",&x);
	#define p(x)					printf("%d\n",x);
	#define f(a,b,c)				for(int a=b;a<c;a++)
	#define r(a,b,c)				for(int a=b;a>c;a--)
	#define p2(x,y)					printf("%d %d\n",x,y);
	#define pl(x)					printf("%lld\n",x);
	#define pl2(x,y)				printf("%lld %lld\n",x,y);
	#define p1d(a,n)				for(int ix=0;ix<n;ix++) printf("%d ",a[ix]); printf("\n");
	#define p2d(a,n,m)				for(int ix=0;ix<n;ix++){ for(int jx=0;jx<m;jx++) printf("%d ",a[ix][jx]); printf("\n");}
	#define TimeElapsed				(double)clock()/CLOCKS_PER_SEC
}
/*........................................................END OF TEMPLATES.......................................................................*/

int main(){
	fast(); 
	int t=1,v1,len,ind;
	string s;
    ll ans = 0;
    bool flag = 0;
	s(v1)
	while(t <= v1){

		  ind = ans = 0;
		  cin>>s;
		  len = s.size();
		  flag = 0;
		  if(s[0] == '-'){
			  	ans++;
			  	while(ind < len && s[ind] == '-') ind++;
		  }
		  
		  while(ind < len){

		  		if(s[ind] == '-' && flag) {
		  			ans+=2;
		  			flag = 0;
		  		}
		  		else if(s[ind] == '+'){
		  			flag = 1;
		  		}

		  		ind++;
		  	}

		  
	      printf("Case #%d: %lld\n",t,ans);
		  t++;
	}
	trace(TimeElapsed)
	
}  