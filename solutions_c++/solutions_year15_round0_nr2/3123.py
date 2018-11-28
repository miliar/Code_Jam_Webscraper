///////////////////////////////
// Template By: Agus Sentosa //
//       17 - 5 - 2014       //
///////////////////////////////
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <cassert>
#include <cstring>
#include <cmath>
#include <functional>
#include <utility>

//I/O
#include <cstdio>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <istream>
#include <ostream>

//Data Type
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <bitset>

//Data Type
#define pii pair<int,int>
#define pll pair<LL,LL>
#define pdd pair<double,double>
#define LL long long
#define ULL unsigned long long

//Data Type Properties
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define popb pop_back

//Macro
#define sqr(x) ((x) * (x))
#define all(v) (v).begin(),(v).end()
#define sortv(v) sort(all(v))
#define num(x) ((x)-'0')
#define ch(x) ((x)+'0')
#define bit_count __builtin_popcount
#define bit_countll __builtin_popcountll
#define THIS (*this)

//Output
#define endl '\n'

//Compiling & Debugging
#ifdef DEBUG
#define DO_IF_DEBUG_FLAG_IS_ON 1
#else
#define DO_IF_DEBUG_FLAG_IS_ON 0
#endif
#define DoDebug if(DO_IF_DEBUG_FLAG_IS_ON)

//???????????????????
#define Fokus using
#define Tahun_Terakhir namespace std;

Fokus Tahun_Terakhir;

#ifdef _WIN32
#define getchar_unlocked getchar
#endif
#define g getchar_unlocked
template<class T>
bool io(T &res){
	static char c=' ';
	while(c == ' ' || c == '\n')c = g();
	if(c == -1)return 0;
	res = num(c);
	while((c=g()) && c != ' ' && c != '\n' && c!=-1){ res = (res << 3) + (res << 1) + num(c); }
	return 1;
}

template<class T>
string inttostr(T x){
	string res="";
	while(x){
		char t=ch(x%10); x/=10; res=t+res;
	}
	return res;
}

template<class T>
T strtoint(string x){
	T res=0;
	for(int i=0;i<x.size();i++){
		res=(res<<3)+(res<<1)+num(x[i]);
	}
	return res;
}
void open(string a){
	freopen((a+".in").c_str(),"r",stdin);
	freopen((a+".out").c_str(),"w",stdout);
}
void close(){
	fclose(stdin);
	fclose(stdout);
}

//Constant
#define INF 1000000007
#define LINF 1000000000000000007ll
#define DINF 1000000000000000007.00
#define INV (-INF)
#define LINV (-LINF)
#define DINV (-DINF)
#define EPS 1e-9
#define MOD 1000000007
///////////////////////////////
//      End of Template      //
///////////////////////////////

#define MX 1000


int solve(){
	int res = INF;
	int n; cin >> n;

	vector<int> V;
	for(int i = 0 ; i < n ; i++){
		int x; cin >> x;
		V.pb(x);
	}

	for(int lmt = 1 ; lmt <= 1000 ; lmt++){
		int tmp = lmt;
		for(int i = 0 ; i < V.size() ; i ++){
			tmp += (V[i]-1) / lmt;
		}

		res = min(res , tmp);
	}

	return res;
}

int main(){
	int t,no = 0; cin >> t;
	while(t--){
		cout << "Case #" << ++no << ": " << solve() << endl;
	}

	return 0;
}