#include <bits/stdc++.h>

using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define FOR(i,n) REP(i,0,(int)n-1)
#define mp make_pair
#define ll long long
#define pb push_back
#define pii pair<int,int>
#define VI vector<int>
#define fi first
#define se second
#define pss pair<short int, short int>

const int INF = 9999999;
bool M[52][52];
int n;

pii getnext(pii pos) {
	if(pos.se < n-1) pos.se ++;
	else {
		pos.se = 0;
		pos.fi++;
	}
	return pos;
}

bool checkvalid() {
	/*FOR(i,n) {
		FOR(j,n) cout<<M[i][j];
		cout<<endl;
	}*/
	//cout<<endl;
	FOR(i,n) {
		bool ok = 0;
		FOR(j,n) if(M[i][j] == 1) ok = 1;
		if(!ok) {/*cout<<"false\n";*/ return false;}
	}
	vector<int> workers;
	FOR(i,n) workers.pb(i);
	do {
    	vector<int> machines;
    	FOR(i,n) machines.pb(i);
    	do {
    		vector<int> occ;
    		FOR(i,n) occ.pb(0);
        	FOR(i,n) {
        		int w = workers[i], m = machines[i];
        		bool ok = 0;
        		FOR(j,n) if(M[w][j] == 1 && occ[j] == 0) ok = 1;
        		if(occ[m] == 0 && M[w][m]) occ[m] = 1;
        		else if(ok) continue;
        		else {
        			//FOR(p,n) cout<<workers[p]<<" ";
        			//cout<<endl;
        			//FOR(p,n) cout<<machines[p]<<" ";
        			//cout<<endl;
        			//cout<<"false\n";
        			return false;
        		} 

        	}
    	} while(next_permutation(machines.begin(), machines.end()));    
    } while(next_permutation(workers.begin(), workers.end()));
    //cout<<"true\n";
    return true;
}

int cost(pii pos, int C) {
	int w = pos.fi, m = pos.se;
	if(w == n) {
		if(checkvalid() == true) return C;
		else return INF;
	}
	else if(M[w][m] == 1) return cost(getnext(pos), C);
	else {
		int temp2 = cost(getnext(pos), C);
		M[w][m] = 1;
		//cout<<"LOL\n";
		int temp3 = cost(getnext(pos), C+1);
		M[w][m] = 0;
		return min(temp2, temp3);
	}
}

void solve() {
	cin>>n;
	FOR(i,n) {
		string s;
		cin>>s;
		FOR(j,n) {
			if(s[j] == '1') M[i][j] = 1;
			else M[i][j] = 0;
		}
	}	
	cout<<cost(mp(0,0), 0)<<"\n";

}

int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	for(int i=1; i<=t; i++) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}