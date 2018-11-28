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
		string s;
		cin >> s;
		reverse(all(s));
		int cnt = 0;
		int res = 0;
		REP(i,0,s.length()){
			if(cnt % 2 == 0 && s[i] =='-'){
				cnt = 1-cnt;
				res++;
			}else if(cnt % 2 == 1 && s[i] == '+'){
				cnt = 1 -cnt;
				res++;
			}
		}
		
		
		cout<<"Case #"<<caso+1<<": "<<res<<endl;
	}
	
	return 0;
}
