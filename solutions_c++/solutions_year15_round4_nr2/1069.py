#include<stdio.h>
#include<iostream>
#include<vector>
#include<string.h>
#include<algorithm>
#include<deque>
#include<map>
#include<set>
#include<stdlib.h>
#include<math.h>
#include<queue>
#include<stack>
#include<functional>
using namespace std;
#define ll long long
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define sd(x) scanf("%lf",&x)
#define sc(x) scanf("%c",&x)
#define ss(x) scanf("%s",x)
#define vl vector<ll>
#define vi vector<int>
#define vvl vector< vl >
#define vvi vector< vi >
#define pb push_back
#define mod 1000000007
#define mem(x,y) memset(x,y,sizeof(x))
#define f(i,a,b) for(int i=(a);i<(b);i++)
#define max_int_value 2147483647
#define max_long_value 9223372036854775807
#define ub(X,v) upper_bound(X.begin(),X.end(),v)
#define lb(X,v) lower_bound(X.begin(),X.end(),v)



//qsort(ww,cc,sizeof(tp),compare);
/*int compare(const void *a,const void *b){
	ll y=((((tp*)a)->w)-(((tp*)b)->w));
	if(y>0)return 1;
	else if(y==0)return 0;
	else return -1;
}

//return true if in correct positions
bool way(ii x,ii y){
	return x.first<y.first or x.first==y.first and x.second<y.second;
}

//return false if in correct positions
struct OrderBy
{
    bool operator() (ii a, ii b) { return a.S < b.S; }
};
priority_queue<ii, std::vector<ii >, OrderBy> Q;


ll modpow(ll base, ll exponent,ll modulus){
	if(base==0&&exponent==0)return 0;
	ll result = 1;
	while (exponent > 0){
		if (exponent % 2 == 1)
		    result = (result * base) % modulus;
		exponent = exponent >> 1;
		base = (base * base) % modulus;
	}
	return result;
}

#define getchar_unlocked getchar
using namespace std;
inline int scan(){
    char c = getchar_unlocked();
    int x = 0;
    while(c<'0'||c>'9'){
        c=getchar_unlocked();
    }
    while(c>='0'&&c<='9'){
        x=(x<<1)+(x<<3)+c-'0';
        c=getchar_unlocked();
    }
    return x;
}

*/


#define MAXN 100010
#define ls (node<<1)
#define rs ((node<<1)+1)
#define ii pair<int,int>
#define F first
#define S second


double V,v1,v2,T,t1,t2,R,r1,r2;



int N;


inline void ReadInput(void){
	si(N); 
	sd(V); sd(T);
	if(N==1){
		sd(r1); sd(t1);
	}else{

		sd(r1); sd(t1);
		sd(r2); sd(t2);	
	}
}

inline void solve(int turn){
    //cout<<turn<<endl;
	if(N==1 or (N==2 and t1==t2)){
        if(N==2)r1=r1+r2;
		if(T!=t1){
			printf("Case #%d: IMPOSSIBLE\n",turn );
		}else{
			double times=V/r1;
			printf("Case #%d: %.9lf\n",turn,times);
		}
	}
	else{
		double foo=V*T;
		foo-=(V*t2);
		double aa=(t1-t2);
		double v1=foo/aa;
        foo=V*(T-t1);
        aa=t2-t1;
        v2=foo/aa;
        //cout<<v1<<" "<<v2<<endl;
		double ans=max((v1/r1),(v2/r2));
        
		if(v1<0 or v2<0)printf("Case #%d: IMPOSSIBLE\n",turn );
		else
			printf("Case #%d: %.9lf\n",turn,ans);
	}
}

inline void Refresh(void){
	
}

int main()
{	
	ios_base::sync_with_stdio(false);
	int t; si(t);
	for(int i=1;i<=t;i++){
		ReadInput();
		solve(i);
	}
    return 0;
}


//A man got to have a code