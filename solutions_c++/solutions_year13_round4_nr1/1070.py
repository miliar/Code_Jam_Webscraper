#include<stdio.h>
#include<string.h>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;

struct node {
	int S, E;
	node() {}
	node(int A, int B) {
		S = A;
		E = B;
	}
	bool operator < (const node t) const {
		return S < t.S;
	}
} ;

vector<node> V;

int main() {
	int T, A, B, C;
	int N, M;
	scanf("%d", &T);
	int Case = 1;
	while ( T-- ) {
		scanf("%d%d", &N, &M);
		V.clear();
		int origin = 0;
		for ( int i = 0 ; i < M ; i++ ) {
			scanf("%d%d%d", &A, &B, &C);
			for ( int j = 0 ; j < C ; j++ ) {
				V.push_back(node(A, B));
			}
			int X = B-A;
			origin += (N+N-X+1)*X/2*C;
		}
		sort(V.begin(), V.end());
		for ( int i = 0 ; i < V.size() ; i++ ) {
			for ( int j = i+1 ; j < V.size() ; j++ ) {
				if ( V[j].S <= V[i].E && V[i].S < V[j].S && V[i].E < V[j].E ) {
					int tmp = V[j].E;
					V[j].E = V[i].E;
					V[i].E = tmp;
				}
			}
		}
		int sum = 0;
		for ( int i = 0 ; i < V.size() ; i++ ) {
			int X = (V[i].E-V[i].S);
			sum += (N+N-X+1)*X/2;
		}
		
		printf("Case #%d: %d\n", Case++, (origin-sum)%1000002013);
	}
	return 0;
}

