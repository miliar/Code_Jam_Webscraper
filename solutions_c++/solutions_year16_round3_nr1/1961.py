#include <bits/stdc++.h>

//#define NDEBUG
#ifdef NDEBUG
#define debug(x);
#define print(x);
#else
#define debug(x) cerr<< #x << ": "<<x<<endl;
#define print(x) cerr<< x<<endl;
#endif

#define mp make_pair
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define rall(x) (x).rbegin() , (x).rend()
#define REP(i,x,y) for(int i=x;i<y;i++)
#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define fst first
#define snd second
#define sqr(x) ((x)*(x))

#define fastio ios_base::sync_with_stdio(0);cin.tie(0);
#define ones(x) __builtin_popcount(x)
using namespace std;

typedef pair<int,int> ii ;
typedef long long ll ;
typedef vector<int> vi;
typedef vector<ii> vii;

int N,n;
int arr[26];
int getMax(int ig){
	int maxi = 0;
	int id = -1;
	REP(i,0,N){
		if(i == ig) continue;
		if(arr[i] > maxi){
			maxi = arr[i];
			id = i;
		}
	}
	return id;
}
int main(){
	fastio;
	int T;
	cin >> T;
	for(int test = 1; test <= T; test++){
		cin >> N;
		n = 0;
		REP(i,0,N) {cin >> arr[i];if(arr[i] > 0) n++;}
		vii ans;
		while(n >= 3){
			int id1 = getMax(-1);
			int id2 = getMax(id1);
		//	cerr<<id1<<" "<<id2<<" "<<n<<endl;
			if(arr[id1] == 1 && arr[id2] == 1 && n == 3){
				break;
			}
			arr[id1]--;
			arr[id2]--;
			if(arr[id1] == 0) n--;
			if(arr[id2] == 0) n--;
			ans.pb(mp(id1,id2));
		}
		/*debug(ans.size());
		REP(i,0,N){
			cerr<<arr[i]<<" " ;
		}cerr<<endl;
*/
		if(n == 3){
			int id1 = getMax(-1);
			ans.pb(mp(id1,-1));
			n--;
			arr[id1]--;
			id1 = getMax(-1);
			int id2 = getMax(id1);
			ans.pb(mp(id1,id2));
			n-=2;
		}
		else if(n == 2){
			int id1 = getMax(-1);
			int id2 = getMax(id1);
			int cant = arr[id1];
			REP(i,0,cant){
				ans.pb(mp(id1,id2));
			}
		}
		cout<<"Case #"<<test<<":";
		REP(i,0,ans.size()){
			int a = ans[i].fst;
			int b = ans[i].snd;
			if(b == -1){
				char e = a+'A';
				cout<<" "<<e;
			}else{
				char e = a+'A';
				char d = b+'A';
				cout<<" "<<e<<d;
			}
		}
		cout<<endl;
	}

	return 0;
}

