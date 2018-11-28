#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define f(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define fiter(it,con) for(auto (it)=(con).begin(); (it)!=(con).end();++(con))
#define x first
#define y second

using namespace std;

typedef pair<int,int> pii;
typedef pair<long long, long long> pll;
typedef long long ll;
typedef vector<int> vi;
typedef vector<bool> vb;

bool isgood(int n, vector<vector<bool> > can) {
	vector<int> arr(n), ass(n);
	f(i,0,n) {
		arr[i]=i;
		ass[i]=i;
	}
	unordered_set<int> occ;
	do {
		do {
			occ.clear();
			f(i,0,n) {
				if(can[arr[i]][ass[arr[i]]]){
					occ.insert(ass[arr[i]]);
				} else {
					bool alter=false;
					f(j,0,n) {
						if(can[arr[i]][j] && !occ.count(j)>0) {
							alter=true;
						}
					}
					if(!alter) {
						return false;
					}
				}
			}
		} while(next_permutation(ass.begin(),ass.end()));
	} while(next_permutation(arr.begin(),arr.end()));
	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	f(cas,1,t+1) {
		int n;
		cin>>n;
		vector< vector<bool> > canop(n);
		f(i,0,n) {
			canop[i]=vector<bool>(n);
			string s;
			cin>>s;
			f(j,0,n) {
				canop[i][j]=(s[j]=='1');
			}
		}
		int la = 1<<(n*n);
		int best = n*n;
		f(mask,0,la) {
			bool go=true;
			vector< vector<bool> > act(n);
			int cnt=0;
			f(i,0,n) {
				act[i]=vector<bool>(n);
				f(j,0,n) {
					bool curr = mask&(1<<i*n+j);
					if(curr) ++cnt;
					if(canop[i][j]&&curr) {
						go=false;
						break;
					}
					act[i][j]=canop[i][j]||curr;
				}
				if(!go) break;
			}
			if(go && cnt<best) {
				if(isgood(n,act)) {
					best=cnt;
				}
			}
		}
		cout<<"Case #"<<cas<<": "<<best;
		cout<<'\n';
	}
	return 0;
}
