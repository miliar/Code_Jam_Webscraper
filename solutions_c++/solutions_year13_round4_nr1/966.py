#include <iostream>
#include <algorithm>
using namespace std;

struct P {
	long long x;
	long long p;
};

bool psorter(P const& lhs, P const& rhs) { return lhs.x < rhs.x; }


long long N,M;
P A[1000],B[1000],S[1000];
long long basescore;
long long bestscore;
	
long long score(long long o, long long e) {
	if(o==e)
		return 0;
	long long z = e-o;
	return (z*N+(z-1ll)*(z)/2ll);
}
		
void handle_input() {
	bestscore = basescore = 0;
	int o,e,p;
	cin >> N >> M;
	for(int i = 0; i < M; i++) {
		cin >> o >> e >> p;
		A[i].x=o;
		A[i].p = p;
		B[i].x=e;
		B[i].p = p;
		basescore += p*score(o,e);
	}
	sort(A,A+M,&psorter);
	sort(B,B+M,&psorter);
	// for(int i = 0; i < M; i++) {
		// cout << A[i].x << " " << A[i].p << " " << B[i].x << " " << B[i].p << endl;
	// }
}
	
int main() {
	int testcases; 
	cin >> testcases;
	for(int curtestcase = 1; curtestcase <= testcases; curtestcase++) {
		handle_input();
		int a=0,b=0,t=-1;
		while(a < M || b < M) {
			if(a < M && A[a].x <= B[b].x) {
				S[++t].x = A[a].x;
				S[t].p = A[a++].p;
			}
			else {
				long long n = min(S[t].p, B[b].p);
				bestscore += n*score(S[t].x,B[b].x);
				S[t].p-=n;
				B[b].p-=n;
				if(S[t].p==0)
					t--;
				if(B[b].p==0)
					b++;
			}
		}
		cout << "Case #" << curtestcase << ": " << bestscore - basescore << endl;
	}
}