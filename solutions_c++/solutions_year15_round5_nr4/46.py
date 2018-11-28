#include <iostream>
#include <map>
#include <cassert>
#include <string>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

#define fu(i,m,n) for(int i=m; i<n; i++)
typedef long long i64;

long factor_out(vector<long>& f, vector<long>& e) {
	int i=0;
	int N=f.size();
	while(i<N && f[i]==0) i++;
	if(i==N) return -1;
	int j=i;
	if(f[i]==1) {
		j++;
		while(j<N && f[j]==0) j++;
		if(j==N) return -1;
	}
	long d = e[j]-e[i];
	//cout << "Found " << i << " and " << j << " Factoring 1+x^" << d << endl;
	if(d==0) {
		fu(i,0,N) {
			if(f[i]%2) return -2;
			f[i]/=2;
		}
	} else {
		int k=i, l=i;
		for(int k=i; k<N; k++) if(f[k]) {
			while(l<N && e[l]<e[k]+d) l++;
			if(l==N || e[l]!=e[k]+d) return -2;
			f[l]-=f[k];
		}
	}
	//fu(i,0,N) cout << f[i] << "*x^" << e[i] << " "; cout << endl;
	return d;
}

int main(void) {
	int TS;
	cin >> TS;
	fu(its,0,TS) {
		cout << "Case #" << its+1 << ":";
		int P; cin >> P;
		vector<long> f(P), e(P);
		fu(i,0,P) cin >> e[i];
		fu(i,0,P) cin >> f[i];
		vector<long> s;
		for(;;) {
			long status = factor_out(f, e);
			if(status==-1) break;
			if(status==-2) { cout << "oops" << endl; break; }
			s.push_back(status);
		}
		long ts=0;
		long tot=0;
		long d0=-1;
		fu(i,0,P) {
			assert(f[i]==0 || f[i]==1);
			tot += f[i];
			if(f[i]) d0=e[i];
		}
		int S = s.size();
		fu(i,0,S) ts+=s[i];
		sort(s.begin(),s.end());
		assert(tot==1);
		
		//cout << "Done" << endl;
		
		long target = d0;

		//cout << "Targetting " << target << endl;

		vector< map<long, long> > prods(S+1);

		prods[0][0]=1;

		fu(i,0,S) {
			for(const pair<long,long> j: prods[i]) {
				prods[i+1][j.first] += j.second;
				prods[i+1][j.first-s[i]] += j.second;
			}
		}

		vector<long> ret;
		for(int i=S-1; i>=0; i--) {
			if(prods[i][target+s[i]]) { target+=s[i]; ret.push_back(-s[i]); }
			else if(prods[i][target]) { ret.push_back(s[i]); }
			else { assert(false); cout << target << "X" << s[i]; }
			//cout << " ";
		}
		sort(ret.begin(),ret.end());
		fu(i,0,ret.size()) cout << " " << ret[i];
		cout << endl;
	}

}
