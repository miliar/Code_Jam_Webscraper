#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <string>
using namespace std;

#define fu(i,m,n) for(int i=m; i<n; i++)
typedef long long i64;

int doit(const vector<int>& S, const vector<int>& M, vector<int>& highest, int i) {
	//cout << i << endl;
	int& ret = highest[i];
	//if(ret==-2) return ret=S[0]+10000000;
	if(ret+1) return ret;
	//ret=-2;
	if(i==0) return ret=S[i];
	return ret = max(S[i], doit(S,M,highest,M[i]));
}

int doit2(const vector<int>& S, const vector<int>& M, vector<int>& lowest, int i) {
	//cout << i << endl;
	int& ret = lowest[i];
	//if(ret==-2) return ret=S[0]+10000000;
	if(ret+1) return ret;
	//ret=-2;
	if(i==0) return ret=S[i];
	return ret = min(S[i], doit2(S,M,lowest,M[i]));
}


int main(void) {
	int TS;
	cin >> TS;
	fu(ts,0,TS) {
		cout << "Case #" << ts+1 << ": ";
		int N,D;
		cin >> N >> D;
		vector<int> S(N), M(N);
		long As,Cs,Rs,Am,Cm,Rm;
		cin >> S[0] >> As >> Cs >> Rs;
		cin >> M[0] >> Am >> Cm >> Rm;
		fu(i,0,N-1) {
			S[i+1] = (S[i]*As + Cs)%Rs;
			M[i+1] = (M[i]*Am + Cm)%Rm;
		}
		fu(i,0,N) {
			if(i) M[i] = M[i]%i;
			//cout << i << " " << S[i] << " " << M[i] << endl;
		}
		M[0]=-1;
		vector<int> highest(N,-1), lowest(N,-1);
		fu(i,0,N) highest[i] = doit(S, M, highest, i);
		fu(i,0,N) lowest[i] = doit2(S, M, lowest, i);
		vector<pair<int,int > > ls(2*N);
		fu(i,0,N) ls[i] = make_pair(highest[i], -1-i);
		fu(i,0,N) ls[N+i] = make_pair(lowest[i]+D, i);
		sort(ls.begin(), ls.end());
		//fu(i,0,N) cout << ls[i].first << " " << ls[i].second << endl;
		bool ceo=false;
		int best=0; int cur=0;
		fu(i,0,2*N) {
			int x = ls[i].second;
			if(x<0) x=-1-x;
			if(highest[x]>lowest[x]+D) {
				//cout << "Skipping " << x << " " << lowest[x] << "+" << D << "<" << highest[x] << endl;
				continue;
			}
			if(ls[i].second<0) {
				cur++;
				if(x==0) ceo=true;
				//cout << "Adding " << x << " " << ls[i].first << endl;
			} else {
				cur--;
				if(x==0) ceo=false;
				//cout << "Dropping " << x << " " << ls[i].first << endl;
			}
			if(ceo) best=max(best,cur);
		}
		cout << best << endl;
	}

}
