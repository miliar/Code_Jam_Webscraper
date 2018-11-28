#include <bits/stdc++.h>

using namespace std;

#define len(x) ((int)(x).size())
#define pb push_back
#define mp make_pair
#define debug(x) cerr << #x << " is " << x << endl;
#if ( ( _WIN32 || __WIN32__ ) && __cplusplus < 201103L)
    #define lld "%I64d"
#else
    #define lld "%lld"
#endif

typedef long long ll;
typedef pair <int,int> pi;

const long double EPS = 1e-10;
const ll MOD = 1e9 + 7;
const ll INF = 1e18;
const long double PI = 3.1415926535897932384626433832795028841;

bool TST = 0;
ll powmod(ll a,ll b) {ll res=1;a%=MOD;for(;b;b>>=1){if(b&1)res=res*a%MOD;a=a*a%MOD;}return res;}
void Show(int *QQ,int N){ if (not TST){ return; } for (int x = 0;x < N;x++){ cout << QQ[x]; if (x != N-1){ cout << ','; } } cout << '\n'; }
void ShowLL(ll *QQ,int N){ if (not TST){ return; } for (int x = 0;x < N;x++){ cout << QQ[x]; if (x != N-1){ cout << ','; } } cout << '\n'; }

void KMPinit(char *P,int Plen , int *Arr){
	int a = 0;
	int i = 1;
	Arr[0] = 0;
	while (i < Plen){
		if (P[i] == P[a]){
			a ++ ;
			Arr[i] = a; 
			i ++ ;
		}else if (a == 0){
			Arr[i] = 0; 
			i ++;
		}else{
			a = Arr[a-1];
		}
	}
}
int KMPRun(char *P,char *T,int *Arr){
	int Plen = strlen(P);
	int Tlen = strlen(T);
	int a = 0 , b = 0 , sol = 0;
	KMPinit(P , Plen , Arr);
	while (b < Tlen){
		if (P[a] == T[b]){
			a ++;
			b ++;
		}
		if (a == Plen){
			a = Arr[a-1];
			sol ++;
		}else if(P[a] != T[b]){
			if (a != 0){
				a = Arr[a-1];
			}else{
				b ++;
			}
		}
	}
	return sol;
}

typedef pair< char , int> pchar;

char W[2000];
char S[2000];

bool U[2000];

struct compare{
	bool operator()(pchar a,pchar b){
		if (a.first != b.first){
			return a.first < b.first;
		}else{
			return a.second > b.second;
		}
	}
};
int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w+",stdout);
	int T; cin >> T;
	for (int x = 1; x <= T;x++){
		cin >> W;

		//if (x != 5){ continue; }
		priority_queue <pchar , vector <pchar> , compare> Q;
		int wlen = strlen(W);
		//reverse(W,W+wlen);
		int d;
		for (int i = 0;i < wlen;i++){
			Q.push(pair<char,int>( W[i] , wlen-i-1) );
			U[i] = 0;
		}
		d = -1;

		string a = "";
		string b = "";
		
		int sz = 0;
		while (sz < wlen and not Q.empty()){
			pchar act = Q.top(); Q.pop();
			//cout << "process " << act.first << ' ' << act.second << '\n';
			if (U[act.second]){ /*cout << "used\n";*/continue; } //already used
			//cout << d+1 << ' ' << act.second << '\n';
			//return 0;
			for (int i = d+1;i < act.second;i++){
				if (U[i]){ continue; }
				U[i] = 1;
				b = W[wlen-i-1] + b; //add in begining
				sz ++;
			}

			a = a + W[wlen-act.second-1];
			sz ++;

			d = act.second;
			U[act.second] = 1;
		//	cout << sz << '\n';

		}
		//cout << sz << ' ' << wlen << '\n';
		string ans = a + b;
		//reverse(ans.begin(),ans.end());
		cout << "Case #"<<x<<": "<< ans<< '\n';
	}
}