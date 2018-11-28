using namespace std;
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cassert>
#include<cstring>
#include<cmath>

typedef long double D; typedef long long LL; typedef pair<int,int> pii;
#define ALL(v) (v).begin(),(v).end()
#define REP(i, n) for (int i (0); i < (n); i ++)
#define FORIT(a,b, it) for(__typeof(b)it(a);it!=(b);++it)
#define FOREACH(v, it) FORIT((v).begin(),(v).end(),it)
#define len(v) ((int)(v).size())
#define append push_back
#define _ make_pair
#define fi first
#define se second
#define add insert
#define remove erase
#define TWO(x) (1<<(x))
#define UNIQUE(v) (v).erase(unique(ALL(v)),(v).end())
const int infInt (1010101010);
const LL  infLL  (4 * LL (infInt) * LL (infInt));

template<class T>void pv(T a,T b){FORIT(a,b,it)cout<<*it<<" ";cout<<endl;}

inline void chmin(int&x,int y){x=min(x,y);}
inline void chmax(int&x,int y){x=max(x,y);}

vector<int> calcA(int n, vector<int> v) {
	vector<int> re (n);
	for (int i=0; i<n; i++) {
		re[i] = 1;
		for (int j=0; j<i; j++) if (v[j] < v[i]) chmax(re[i], re[j] + 1);
	}
	return re;
}

vector<int> calcB(int n, vector<int> v) {
	vector<int> re (n);
	for (int i=n-1; i>=0; i--) {
		re[i] = 1;
		for (int j=n-1; j>i; j--) if (v[j] < v[i]) chmax(re[i], re[j] + 1);
	}
	return re;
}

vector<int> solve(int n, vector<int> a, vector<int> b) {
	vector<int> solution (n, -1);
	for (int i = 1; i <= n; i ++) {
		static int aa[2005];
		static int bb[2005];
		static int min_a_from_right[2005];
		static int min_b_from_left[2005];
		{
			int cur = 1;
			for (int idx = 0; idx < n; idx ++) {
				aa[idx] = -1;
				if (solution[idx] == -1) aa[idx] = cur; else { cur = std::max(cur, a[idx] + 1); }
			}
			int curmin = 1e9;
			for (int idx = n - 1; idx >= 0; idx --) {
				if (solution[idx] == -1) chmin(curmin, a[idx]);
				min_a_from_right[idx] = curmin;
			}
			// printf("i = %d, aa = ", i); pv(aa, aa + n);
		}
		{
			int cur = 1;
			for (int idx = n - 1; idx >= 0; idx --) {
				bb[idx] = -1;
				if (solution[idx] == -1) bb[idx] = cur; else { cur = std::max(cur, b[idx] + 1); }
			}
			int curmin = 1e9;
			for (int idx = 0; idx < n; idx ++) {
				if (solution[idx] == -1) chmin(curmin, b[idx]);
				min_b_from_left[idx] = curmin;
			}
			// printf("i = %d, bb = ", i); pv(bb, bb + n);
		}
		bool ok = false;
		for (int idx = 0; idx < n; idx ++) {
			if (solution[idx] == -1 and a[idx] == aa[idx] and b[idx] == bb[idx]) {
				if (idx != n - 1 and min_a_from_right[idx + 1] <= a[idx]) continue;
				if (idx != 0     and min_b_from_left [idx - 1] <= b[idx]) continue;
				solution[idx] = i;
				ok = true;
				break;
			}
		}
		if (not ok) throw;
		//pv(ALL(solution));
	}
	return solution;
}

int main() {
	int T;
	scanf("%d",&T);
	for (int case_nr=1; case_nr<=T; case_nr++) {
		int n;
		scanf("%d",&n);
		vector<int> A (n);
		for (int i=0; i<n; i++) {
			scanf("%d",&A[i]);
		}
		vector<int> B (n);
		for (int i=0; i<n; i++) {
			scanf("%d",&B[i]);
		}
		vector<int> X = solve(n, A, B);
		assert(calcA(n, X) == A);
		assert(calcB(n, X) == B);
		printf("Case #%d:", case_nr);
		for (int i=0; i<n; i++) {
			printf(" %d", X[i]);
		}
		printf("\n");
	}
}
