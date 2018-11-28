// @adi28galaxyak
// Content:
 
#include "bits/stdc++.h"
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector< vi > vii;
typedef vector< ll > VLL;
typedef pair<int, int> pii;
#define FF first
#define SS second
#define pb(v) push_back(v)
#define mp(x,y) make_pair(x, y)
 
#define NITRO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define s(n) scanf("%d",&n)
#define rep(i,start,end) for(int i = start;i<end;i++)
 
const int MAX = 10;

void update(int val, vector<bool> &A){
	while(val){
		A[val%10] = true;
		val/=10;
	}
}

bool isAns(vector<bool> &A){
	rep(i,0,10)
		if(A[i]==false) return false;
	return true;
}

int main(){
    #ifndef ONLINE_JUDGE
        freopen("A-large.in", "r", stdin);
        freopen("ans1_large.out", "w", stdout);
    #endif // ONLINE_JUDGE

	NITRO;
	
	int tt, n, gen, test = 0;
	cin>>tt;
	while(tt--){
		test++;
		vector<bool> A(10, false);
		cin>>n;
		rep(i,1,101){
			gen = i*n;
			update(gen, A);
			if(isAns(A)) break;
		}

		if(isAns(A)) printf("Case #%d: %d\n", test, gen);
		else printf("Case #%d: INSOMNIA\n", test);
	}
} 