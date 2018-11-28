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
int len;
string getString(int mask){
	string s = "";
	int m = 0;
	REP(i,0,len){
		if(mask & (1<<i)){
			s+='1';
			m = i;
		}else{
			s+='0';
		}
	}
	m++;
	s = s.substr(0,m);
	reverse(all(s));
	string vacio = "";
	REP(i,0,len-s.length()){
		vacio+='0';
	}
	string res = s + vacio + vacio + s;
	return res;
}

ll getNum(int mask, ll b){
	ll res = 0;
	ll pot = 1;
	REP(i,0,len){
		if(mask & (1 << i)){
			res += pot;
		}
		pot *= b;
	}
	return res;
}

int main(){
	fast_io();
	
	int t; cin >> t;
	int n; //n par
	int J;
	cin >> n >> J;
	
	

	cout<<"Case #1:"<<endl;
	len= n/2;
	int cnt = 0;
	for(int mask = 2; mask < (1 << len); mask++){
		if(cnt >= J) continue;
		if(mask & 1){
	
			string s = getString(mask);
			cout<<s;
			REP(i,2,11){
				ll num = getNum(mask,i);
				cout<<" "<<num;
			}
			cout<<endl;
			cnt++;	
		}
	}
	
	
	return 0;
}
