/*
  /\     /\
  | ).|.( |
  |  >-<  |
  =========
It's AdilkhanKo miaaaaaau
*/
#include<bits/stdc++.h>

#define ll long long
#define pb push_back
#define endl "\n"
#define foreach(it, S) for(__typeof (S.begin()) it = S.begin(); it != S.end(); it++)
#define mp make_pair
#define f first
#define s second
#define name ""
#define _ ios_base::sync_with_stdio(false);cin.tie(0);

using namespace std;

const int MaxN = int (1e5);
const int INF = int(1e9);
const int mod = (int)(1e9) + 7;
const double pi = 3.1415926535897932384626433832795;
ll n, m, t, ans = -INF, a[11], p[20][50];

int main () { _
	#ifdef ONLINE_JUDGE
//		freopen (name".in","r",stdin);
//		freopen (name".out","w",stdout);
	#else
		freopen (".in","r",stdin);
		freopen (".out","w",stdout);
	#endif
	cin >> t;
	for(int i = 2; i <= 10; i++){
		p[0][i] = 1;
	}	
	for(int i = 1; i <= 18; i++){
		for(int j = 2; j <= 10; j++){
			p[i][j] = p[i - 1][j] * j;	
		}	
	}
	for(int T = 1; T <= t; T++){
		cin >> n >> m;
		cout << "Case #" << T << ":" << endl;
		vector<pair<int, vector<int> > > V;
		for(int i = (1 << (n - 1)) + 1; i <= (1 << n); i+=2){
			bool Ok = 1;          
			memset(a, 0, sizeof a);
			for(int j = 0; j < n; j++){
				for(int k = 2; k <= 10; k++){
					if((i & (1 << j))){
						a[k] += p[j][k];												
					}     
				}
			}
			vector<int> v;
			for(int j = 2; j <= 10; j++){
				bool ok = 0;
				for(ll k = 2; k * k <= a[j]; k++){
					if(a[j] % k == 0){
						ok = 1;
						v.pb(k);
						break;
					}
				}
				if(!ok){
					Ok = 0;
					break;
				}
			}
			if(Ok == 1){
				if(V.size() == m)break;
				V.pb(mp(i, v));        
				if(V.size() == m)break;
			}
		}
		for(int i = 0; i < V.size(); i++){
			vector<int> v;
			int x = V[i].first;
			vector<int> q = V[i].second;
			while(x){
				v.pb(x % 2);
				x /= 2;
			}
			for(int j = v.size() - 1; j >= 0; j--)cout << v[j];	
			cout << " ";
			for(int j = 0; j < q.size(); j++){
				cout << q[j] << " ";
			}
			cout << endl;
		}
	}
}
