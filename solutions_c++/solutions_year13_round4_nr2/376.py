#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
using namespace std;

template<class T>inline void ChkMax(T &a,const T &b){if(a < b) a = b;}
template<class T>inline void ChkMin(T &a,const T &b){if(b < a) a = b;}
const int dx[]={ 0, 0,-1, 1,-1, 1,-1, 1};
const int dy[]={-1, 1, 0, 0,-1,-1, 1, 1};

typedef long long LL;
typedef pair<int, int> pii;

#define LOWBIT(v) ((v)&(-(v)))
#define POW2(p) (1<<(p))
#define KTH_BIT(v, k) ((v) & POW2(k))
#define MERGE_BIT(v, k) ((v) | POW2(k))
#define INF 0x3f3f3f3f
#define eps 1e-5

// -------------------------------------------

#define MAXN 
#define MOD 

int n;
LL p;
int arr[10];
int rem[10][10];
int fin[10];

void chk() {
	int all = 1<<n;
	int bits = all-1;

	int pos[10];
	int tmp[10];
	memcpy(tmp, arr, sizeof(tmp));
	for(int i=0; i<all; ++i) {
		pos[i] = i;
	}

	for(int i=1, offset = n*2; i<=n; ++i, --offset) {
		for(int j=0; j<all; j+=2) {
			int v0 = tmp[pos[j]&bits];
			int v1 = tmp[pos[j+1]&bits];

			if(v0 < v1) {
				pos[j+1] |= (1<<offset);
			} else {
				pos[j] |= (1<<offset);
			}
		}
		sort(pos, pos+all);
	}

	for(int i=0; i<all; ++i) {
		fin[i] = tmp[pos[i]&bits];
//		cout<<fin[i]<<" - ";
	}
//	cout<<endl;
}

void bf() {
	int all = 1<<n;
	for(int i=0; i<all; ++i) {
		arr[i] = i;
	}
	memset(rem, 0, sizeof(rem));
	int per = 0;
	do {
		chk();
		for(int i=0; i<all; ++i) {
			rem[i][ fin[i] ]++;
		}
		++per;
	} while(next_permutation(arr, arr+all));

	for(int p=1; p<all; ++p) {
		int key = -1;
		int key2 = -1;
		for(int i=0; i<all; ++i) {
			rem[p][i] += rem[p-1][i];
//			cout<<rem[p][i]<<" ~ ";
			if(rem[p][i] == per) {
				key = i;
			}
			if(rem[p][i] > 0) {
				key2 = i;
			}
		}
//		cout<<endl;
		cout<<n<<"\t"<<p+1<<"\t"<<key<<" "<<key2<<endl;
	}
	cout<<endl;
}

LL calc0(int n, LL p) {
	LL v = 0;
	for(LL i=n-1, offset = 1; i>=0; --i, ++offset) {
		p -= (1LL)<<i;
		if(p<=0) {
			return v;
		} else {
			v |= (1LL)<<offset;
		}
	}
	return v;
}

LL calc1(int n, LL p) {
	--p;
	LL v = 0;
	for(LL i=1, offset=n-1; i<n; ++i,--offset) {
		p -= (1LL)<<i;
		v |= (1LL)<<offset;
		if(p <= 0) {
			return v;
		}
	}
	return v;
}

void solve() {
	if(p == 1) {
		printf(" 0 0\n");
		return ;
	} else if(p == (1LL<<n)) {
		printf(" %lld %lld\n", p-1, p-1);
		return ;
	}

	printf(" %lld %lld\n", calc0(n, p), calc1(n, p));
}

int main() {
#ifndef ONLINE_JUDGE
//	freopen("in", "r", stdin);
	freopen("C:\\Users\\Tang\\Downloads\\B-large.in", "r", stdin);
	freopen("C:\\Users\\Tang\\Downloads\\b.out", "w", stdout);	
#endif

//	for(n=1; n<=3; ++n) {
//		bf();
//	}

//	return 0;
	
	int dataset;
	scanf("%d", &dataset);
	for(int cas=1; cas<=dataset; ++cas) {
		scanf("%d %lld", &n, &p);
		printf("Case #%d:", cas);
//		cout<<n<<"  "<<p<<" ";
		solve();
	}

	return 0;
}
