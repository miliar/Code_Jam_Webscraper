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

map <string ,int> ssol;
void checkAdd(string vs){ if (ssol.find(vs) != ssol.end()){ return; } ssol[vs] = 1; }

bool TST = 0;
ll powmod(ll a,ll b) {ll res=1;a%=MOD;for(;b;b>>=1){if(b&1)res=res*a%MOD;a=a*a%MOD;}return res;}
void Show(int *QQ,int N){ if (not TST){ return; } for (int x = 0;x < N;x++){ cout << QQ[x]; if (x != N-1){ cout << ','; } } cout << '\n'; }
void ShowLL(ll *QQ,int N){ if (not TST){ return; } for (int x = 0;x < N;x++){ cout << QQ[x]; if (x != N-1){ cout << ','; } } cout << '\n'; }


const int maxn = 100005;
const int maxm = 100005;
const int maxk = 100005;

int T;
int p[1000];

int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w+",stdout);

	cin >> T;
	for (int ca = 1;ca <= T;ca++){
		int n; cin >> n;
		int pe = 0;
		for (int q = 0;q < n;q++){
			cin >> p[q];
			pe += p[q];
		}
		//cout << pe << '\n';
		cout << "Case #"<<ca<<": ";
		while (pe > 0){
			int hi = -1;
			int hv = 0;
			//cout << "Count = " << '\n';
			for (int i = 0;i < n;i++){
				//cout << i << ":" << p[i] << '\n';
				if (p[i] > hv){
					hi = i;
					hv = p[i];
				}
			}
			if (hv == 0){ break; } //no people
			int a = hi;
			int b = -1;
			p[a] --; //evacuate a
			pe--;
			for (int i = 0;i < n;i++){
				if (p[i] == hv and hv != 0){
					b = i;
				}
			}
			cout << char(a + 65);
			if (b != -1 and pe != 2){
				cout << char(b+65);
				pe--;
				p[b] --;
			}
			if (pe > 0){
				cout << " ";
			}
		}
		cout << '\n';
	}
}