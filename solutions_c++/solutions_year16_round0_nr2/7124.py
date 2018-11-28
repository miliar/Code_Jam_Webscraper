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
 
int getans(int i, int j, string A){
	int rt = 0;
	while (i<=j and i<=A.size()){
		if(A[i]=='+'){
			rt++;
			while(A[i]!='-' and i<A.size() and i<=j) i++;
		}
		else{
			rt++;
			while(A[i]!='+' and i<A.size() and i<=j) i++;
		}
	}
	return rt;
}

int main(){
    #ifndef ONLINE_JUDGE
        freopen("B-large.in", "r", stdin);
        freopen("blarge.out", "w", stdout);
    #endif // ONLINE_JUDGE

	NITRO;
	int tt, test = 0;
	cin>>tt;
	while(tt--){
		test++;
		string A;
		cin>>A;

		int last = A.size() -1;
		while(A[last]!='-' and last>=0) last--;

		printf("Case #%d: %d\n", test, getans(0, last, A));
	}
} 