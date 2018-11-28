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

string s;

int main(){
	fast_io();
	int T;
	cin >> T;
	for(int test = 1; test <= T; test++){
	    cin >> s;
	    string res = "";
	    for(int i = 0; i < s.length(); i++){
	        string tmp1; tmp1.pb(s[i]);
	        tmp1 += res;
	        string tmp2 = res;
	        tmp2+= s[i];
	        if(tmp1 < tmp2){
	            res = tmp2;
	        }else{
	            res = tmp1;
	        }
	    }
	    cout<<"Case #"<<test<<": "<<res<<endl;
	
	}
	

	return 0;
}
