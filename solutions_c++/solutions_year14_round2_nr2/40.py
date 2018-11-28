

#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <set>
#include <cstdlib>
#include <hash_map>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define rep(i,s,e) for(int i=s;i<e;i++)
#define sz(X) ((int)(X.size()))
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
//---------------------------------------------------------------



int get(int mask, int A, int ma) {
	if((A&mask) == (ma&mask)) return A-ma+1;
	return (~mask) + 1;
}


LL get(int A, int B, int K, int mask, int ma, int mb) {
	//cout<<mask<<endl;
	int w;
	for(w=31;w>=0;w--) {
		if((mask & (1<<w)) == 0) break;
	}
	//cout<<w<<endl;
	
	if((ma&mb) < (K&mask)) 
		return get(mask, A, ma) * (LL) get(mask, B, mb);
	if((ma&mb) > (K&mask))
		return 0;
	if(w<0) return 1;
// 	if((A&(1<<w))==0 && (B&(1<<w))==0)
// 		return get(A, B, K, mask|(1<<w), ma, mb);
	LL ret = 0;
	for(int i=0;i<2;i++) if(ma + (1<<w)*i <= A) {
		for(int j=0;j<2;j++) if(mb + (1<<w)*j <= B) {
			ret += get(A, B, K, mask|(1<<w), ma+(1<<w)*i, mb + (1<<w)*j);
		}
	}
	return ret;
}


LL force(int A, int B, int K) {
	LL ret = 0;
	for(int i=0;i<A;i++) for(int j=0;j<B;j++) if((i&j) < K) ret ++;
	return ret;
}



int main() {
	freopen("F:/TDDOWNLOAD/B-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/B-large.out", "w", stdout);

	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++) {
		int A, B, K;
		cin>>A>>B>>K;
// 		A = rand()*rand()%100000;
// 		B = rand()*rand()%100000;
// 		K = rand()*rand()%100000;


		printf("Case #%d: ", te);
		cout<<get(A-1, B-1, K-1, 0x80000000, 0, 0)<<endl;

// 		LL A1 = get(A-1, B-1, K-1, 0x80000000, 0, 0);
// 		LL A2 = force(A, B, K);
// 		if(A1 != A2) {
// 			cout<<A<<' '<<B<<' '<<K<<" fuck!!!"<<endl;
// 			break;
// 		}
	}
}








