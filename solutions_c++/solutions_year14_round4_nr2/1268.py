#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define f first
#define s second

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

const int MAX = 1001;
const int inf = 1000000001;

int s[MAX];

void swap(int i, int j){
	int c = s[i];
	s[i] = s[j];
	s[j] = c;
}

int tree[4*MAX],M;

void update(int a, int b){
	int x=M+a-1;
	tree[x]=b;

	while(x>1){
		x/=2;
		tree[x] = tree[2*x] + tree[2*x+1];
	}
}

int calc(int a, int b){
	if(a>b) return 0;

	int xa=M+a-1;
	int xb=M+b-1;

	int res = tree[xa];
	if(xa != xb) res += tree[xb];

	while(xa/2!=xb/2){
		if(xa%2==0) res += tree[xa+1];
		if(xb%2==1) res += tree[xb-1];
		xa/=2;
		xb/=2;
	}

	return res;
}

void testcase(){
	int n;
	cin >> n;

	int t[MAX];

	M = 1;
	while(M <= n) M *= 2;

	REP(i,n){
		cin >> t[i];
		s[i] = t[i];
	}

	sort(s,s+n);

	int r[MAX];

	int res = 10000;

	do{
		int moves = 0;
		int i = 0;
		int j = n-1;
		REP(i,n) r[i] = s[i];
		while(i<n-1 && s[i]<s[i+1]) ++i;
		while(j>0 && s[j]<s[j-1]) --j;

		if(j-i>1) continue;

		REP(i,n){
			REP(j,n)
				if(s[j]==t[i]){
					FORD(k,j,i+1){
						swap(k,k-1);
						++moves;
					}
				}
		}

		REP(i,n) s[i] = r[i];
		res = min(res,moves);
	}
	while(next_permutation(s,s+n));

	cout << res;
	return;
/*
	map<int,int> m;

	int j = 1;
	REP(i,n) m[s[i]] = j++;

	REP(i,n) t[i] = m[t[i]];

	int idx;

	REP(i,n)
		if(t[i] == n) idx = i;

	int res = 1000001;

	REP(i,n){
		REP(j,n) s[j] = t[j];

		int swaps = 0;
		
		FOR(j,min(idx,i),max(idx,i)-1){
			++swaps;
			swap(j,j+1);
		}

		FOR(j,1,2*M) tree[j] = 0;

		REP(j,idx){
			update(s[j],1);
			swaps += calc(s[j]+1,n);
		}

		FOR(j,1,2*M) tree[j] = 0;

		FOR(j,idx+1,n-1){
			update(s[j],1);
			swaps += calc(1,s[j]-1);
		}

		res = min(res,swaps);
	}

	cout << res;
*/
}

int main(){
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;

	FOR(i,1,t){
		cout << "Case #" << i << ": ";
		testcase();
		cout << endl;
	}

	return 0;
}
