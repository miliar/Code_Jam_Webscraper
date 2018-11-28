#include <bits/stdc++.h>

//#define NDEBUG ;
#ifdef NDEBUG
#define debug(x) ;
#define print(x) ;
#else
#define debug(x) cerr << #x << ": " << x << endl;
#define print(x) cerr<<x<<endl;
#endif

#define mp make_pair
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define rall(x) (x).rbegin() , (x).rend()
#define f(i,a,b) for(int i = a ; i < b ; i++)
#define REP(i,x,y) for(int i=x;i<y;i++)
//#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define fst first
#define snd second
#define sqr(x) ((x)*(x))

#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0);
#define ones(x) __builtin_popcount(x)
using namespace std;

typedef pair<int,int> ii ;
typedef long long ll ;
typedef vector<int> vi;
typedef vector<ii> vii;

int main(){
	fast_io();
	
	int t;
	cin >> t;
	
	REP(caso,0,t){
		int K, C,S;
		cin >> K >> C >> S;
		cout<<"Case #"<<caso+1<<":";
		if(C == 1){
			if(S < K){
				cout<<" IMPOSSIBLE"<<endl;
			}else{
				REP(i,0,K){
					cout<<" "<<i+1;
				}
				cout<<endl;
			}
		}else{
			int techo = K%2 == 0? K/2 : K/2 + 1;
			if(S >= techo){
				
				ll delta = 0;
				ll id = 2;
				ll maxi = K*K;
				
				REP(i,0,techo){
					ll val = delta*K+id;
					if(val>= maxi) val--;
					
					cout<<" "<<val;
					delta+=2;
					id+=2;
					
				}
				
				cout<<endl;
				
			}else{
				cout<<" IMPOSSIBLE"<<endl;
			}
		}
		
		
	}
	
	return 0;
}
